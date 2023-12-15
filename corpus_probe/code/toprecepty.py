import requests as requests
from bs4 import BeautifulSoup
import json

def get_recipe_structure(url: str) -> dict:
    """
    Returns a JSON-LD structure of the recipe from the given URL.
    TO DO: ApetitOnline is one indentation level deeper than TopRecepty.
    """
    recipe_page = requests.get(url=url)
    soup = BeautifulSoup(recipe_page.content, "html.parser")
    our_tag: list = soup.find("script", {"type": "application/ld+json"}).contents
    recipe_structure: dict = json.loads("".join(our_tag)) #json_ld: str = "".join(our_tag)
    return recipe_structure

def random_recipe_collector():
    """
    Scrapes through the random recipes page and returns a list of 25 random recipe links from toprecepty.cz.
    It takes all 25 links from the first loading of the dedicated random recipe page on the website.
    The page loads more recipes as you scroll down, ad infinitum.
    """
    results_page = requests.get("https://www.toprecepty.cz/nahodny_recept.php", timeout=30)
    soup = BeautifulSoup(results_page.content, "html.parser")
    recipe_list = soup.find_all(class_="b-recipe__link link-mask")
    recipes = []
    for item in recipe_list:
        link = item["href"]
        recipes.append(link)
    return recipes


def get_instructions(recipe_structure: dict) -> dict:
    """
    Returns the recipe instructions from the given URL.
    TODO: What format should the instructions be in?
    """
    return recipe_structure["recipeInstructions"]

def main():
    for i in range(20):
        urls: list[str] = random_recipe_collector()
        for url in urls:
            url = "https://www.toprecepty.cz" + url
            recipe_structure: dict = get_recipe_structure(url)
            print(f"autor\t{recipe_structure['author']['name']}")
            print(f"url\t{url}")
            for ins in get_instructions(recipe_structure):
                print(ins["text"])
            print("###")

    return 0

if __name__ == "__main__":
    main()
