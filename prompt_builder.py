def generate_prompt(link, elements, scraper_description_text):
    intro = """Wite a python webscraper script for this website:"""
    elements_explanation = f"""The script should make use of the following {len(elements)} types of elements ([...] means that the code inside the element was omitted):\n\n"""
    for element in elements:
        elements_explanation += str(element) + "\n"
    scraper_description = f"""Description of the scraper script:
{scraper_description_text}"""
    final_remark = """You only have the information given above, so don't make any additional assumptions about the structure of the HTML code on the page. Don't assume to have information about the classes or other attributes of elements. Preferably you should find a solution that doesn't include searching for x-paths."""

    prompt = f"""{intro}
{link}
{elements_explanation}{scraper_description}

{final_remark}"""
    
    return prompt