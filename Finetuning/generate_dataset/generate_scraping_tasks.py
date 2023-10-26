from generate_response import get_response
from bs4 import BeautifulSoup


def generate_scraping_tasks(link, website, category, HTML_string, num_tasks):
    """
    Generate text prompts for GPT-3.5 of what should be scraped from the given page.

    Parameters:
    link (str): The URL of the page to be scraped.
    website (str): The name of the website. E.g. twitter.
    category (str): The category of the page. E.g. stocks or social media.
    HTML_string (str): The HTML of the body of the page to be scraped.
    num_tasks (int): The number of tasks to generate.
    """

    # Load prompt templates from txt file
    system_prompt = open("prompts/generate_scraping_tasks_system_prompt.txt", "r").read()
    user_prompt = open("prompts/generate_scraping_tasks_user_prompt.txt", "r").read()

    # Fill in the templates
    user_prompt = user_prompt.format(link=link, category=category, HTML_string=HTML_string, num_tasks=num_tasks)

    # Get response from GPT
    response = get_response(system_prompt, user_prompt, "gpt-3.5-turbo")

    # Extract the tasks from the response
    tasks = response.split("\n")

    # Remove the "- " prefix from each task
    tasks = [task.split("- ")[1] if "- " in task else task for task in tasks]

    # Remove empty tasks (those that are less than 5 characters long)
    tasks = [task for task in tasks if len(task) > 5]

    # Save as a txt file
    with open(f"scraping_tasks/{website}.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")