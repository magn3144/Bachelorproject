from lxml import etree
from io import StringIO
from bs4 import BeautifulSoup
import random
import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4")


def extract_text_objects(html_content):
    # Parse the HTML using lxml
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(html_content), parser)
    
    # Get all elements that have text directly inside them
    elements_with_text = [elem for elem in tree.xpath('//*') if elem.text and not elem.getchildren()]

    # Exclude script and style tags
    elements_with_text = [elem for elem in elements_with_text if elem.tag not in ['script', 'style']]
    
    # Extract the HTML and xpath for each element
    htmls = [etree.tostring(elem, encoding='unicode') for elem in elements_with_text]
    xpaths = [tree.getpath(elem) for elem in elements_with_text]
    
    return htmls, xpaths

def get_first_n_tokens(text, n):
    text = text[:min(n*10, len(text))]
    tokens = encoding.encode(text)
    tokens = tokens[:n]
    text = encoding.decode(tokens)
    return text

def extract_relevant_information(HTML_file):
    """
    Returns a list of HTML objects and XPaths, that are relevant for the scraping task.
    The procedure is as follows:

    1. Generate a list of HTML objects and XPaths.
    2. Divide them into different lists by tag.
    3. Divide each list into two lists, one with long text and one with short text.
    4. Now we want to add one element from each list to a new list. We want to add them in a way that the new list is balanced.
    5. This should be repeated until we have added all the elements from the lists.
    6. Remove all HTML attributes from the objects except for class and id.
    7. Remove all the elements children that are not text.
    8. The text should be truncated if it is longer than 100 characters.
    9. Each element should be truncated if it is too long.
    10. The total amount of tokens in the resulting text should not exceed a maximum.

    Parameters:
    HTML_file (str): The path to the HTML file.
    """

    # Generate a list of HTML objects and XPaths.
    html = open(HTML_file, 'r').read()

    # Extract the body
    soup = BeautifulSoup(html, 'html.parser')
    html = str(soup.body)

    htmls, xpaths = extract_text_objects(html)

    # Divide them into different lists by tag.
    htmls_by_tag = {}
    for html, xpath in zip(htmls, xpaths):
        tag = xpath.split('/')[-1].split('[')[0]

        if tag not in htmls_by_tag:
            htmls_by_tag[tag] = []

        htmls_by_tag[tag].append((html, xpath))
    
    # Divide each list into two lists, one with long text and one with short text.
    split_length = 25
    htmls_by_tag_split = {}
    for tag in htmls_by_tag:
        htmls_by_tag_split[tag] = [[], []]
        for html, xpath in htmls_by_tag[tag]:
            text = BeautifulSoup(html, 'html.parser').text
            if len(text) > split_length:
                htmls_by_tag_split[tag][0].append((html, xpath))
            elif len(text) <= split_length:
                htmls_by_tag_split[tag][1].append((html, xpath))

    # Shuffle the lists for each tag. The HTML and XPath should till correspond.
    for tag in htmls_by_tag_split:
        random.shuffle(htmls_by_tag_split[tag][0])
        random.shuffle(htmls_by_tag_split[tag][1])

    # Now we want to add one element from each list to a new list.
    # This should be repeated until we have gone through the list.
    long_texts_added = 0
    short_texts_added = 0
    allowed_difference = 10
    htmls_balanced = []
    allowed_tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'td', 'th', 'dt', 'dd', 'blockquote', 'cite', 'figcaption', 'a', 'span', 'label', 'legend', 'pre', 'caption', 'td', 'th', 'div', 'title']
    for _ in range(len(htmls)):
        for tag in htmls_by_tag_split:
            if tag in allowed_tags:
                if len(htmls_by_tag_split[tag][0]) > 0 and long_texts_added < short_texts_added + allowed_difference:
                    htmls_balanced.append(htmls_by_tag_split[tag][0].pop())
                    long_texts_added += 1
                if len(htmls_by_tag_split[tag][1]) > 0 and short_texts_added < long_texts_added + allowed_difference:
                    htmls_balanced.append(htmls_by_tag_split[tag][1].pop())
                    short_texts_added += 1
    
    # Clean each HTML element.
    for i, (html, xpath) in enumerate(htmls_balanced):
        soup = BeautifulSoup(html, 'html.parser')
        # Remove all HTML attributes from the objects except for class and id.
        for tag in soup.find_all(True):
            attrs = dict(tag.attrs)
            for attr in attrs:
                if attr not in ["class", "id"]:
                    del tag.attrs[attr]

            # Remove all the elements children that are not text.
            for child in list(tag.children):
                if child.name:  # if it's a tag and not a text node
                    child.decompose()

            # The text should be truncated if it is longer than 100 characters.
            max_text_length = 50
            if tag.string and len(tag.string) > max_text_length:
                tag.string = tag.string[:max_text_length]

        htmls_balanced[i] = (str(soup), xpath)

    # Each element should be truncated if it is too long.
    max_length = 300
    for i, (html, xpath) in enumerate(htmls_balanced):
        if len(html) > max_length:
            htmls_balanced[i] = (html[:max_length], xpath)
    
    # Remove all linebraks and empty strings.
    htmls_balanced = [(html.replace('\n', '').replace('\r', ''), xpath) for html, xpath in htmls_balanced if html.replace('\n', '').replace('\r', '') != '']
    
    # # The total length of the HTMLs should not exceed max_total_characters.
    # # Add the HTMLs and xpaths to a new list until the total length is exceeded.
    # max_total_chars = 6000
    # total_chars = 0
    # i = 0
    # while total_chars < max_total_chars:
    #     total_chars += len(htmls_balanced[i][0])
    #     i += 1
    # htmls_balanced = htmls_balanced[:i]

    # # Make a new list without the xpaths, so only the HTMLs are left.
    # htmls_balanced = [html for html, xpath in htmls_balanced]

    # Concatenate the HTMLs and XPaths into one string.
    html_string = ''
    for html, xpath in htmls_balanced:
        html_string += html + '\n'
        html_string += xpath + '\n'
        html_string += '----------------\n'
    
    # The total amount of tokens in the resulting text should not exceed max_total_tokens.
    return '\n'.join(str(get_first_n_tokens(html_string, 2000)).split('\n')[:-1])