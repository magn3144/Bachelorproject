import regex as re
from generate_response import get_response
import os


def generate_solution_code(website, HTML_file, category, HTML_string, task, task_i):
    """
    Generate a python script that solves the given scraping task, using GPT-4.

    Parameters:
    website (str): The name of the website (fx facebook).
    HTML_file (str): The local path to the HTML file.
    category (str): The category of the website (fx social media).
    HTML_string (str): Extract from the target HTML file.
    task (str): Description of what the scraper script should do.
    """

    # Load prompt templates from txt file
    system_prompt = open("prompts/generate_solution_code_system_prompt.txt", "r").read()
    user_prompt = open("prompts/generate_solution_code_user_prompt.txt", "r").read()

    # Fill in the templates
    user_prompt = user_prompt.format(website=website, HTML_file=HTML_file, category=category, HTML_string=HTML_string, task=task)

    # Get response from GPT-4
    response = get_response(system_prompt, user_prompt, "gpt-3.5-turbo")

    # Extract the code from the response
    scraper_code = re.search(r"(?<=```python\n)[\s\S]+?(?=\n```)", response)
    if scraper_code != None:
        scraper_code = scraper_code.group(0)
    else:
        scraper_code = response

    # Save as a .py file
    # If directory does not exist, create it
    if not os.path.exists(f"solution_code/{website}"):
        os.makedirs(f"solution_code/{website}")
    with open(f"solution_code/{website}/{website}_{task_i}.py", "w") as file:
        file.write(scraper_code)