# lets do this thing
import requests
from bs4 import BeautifulSoup
import csv
import time
from rich.console import Console

console = Console()

BASE_URL = "https://monsterhunterwiki.org/wiki"
HEADERS = {"User-Agent": "is310-course-scraper/1.0 (student project; ecampos3@illinois.edu)"}
REQUEST_DELAY = 1  

# fine i'll make functions. i should have done this sooner
def get_internal_links(content):
    links = []
    for link in content.find_all("a", href= True):
        href = link["href"]
        if href.startswith("/wiki/") and "#" not in href:
            links.append(href)
    return links

def count_links(links):
    internal_links = links
    unique_internal_links = []
    console.print("[blue]Doing math to count unique links...")
    for href in internal_links:
        if href not in unique_internal_links:
            unique_internal_links.append(href)
    return len(unique_internal_links)

def count_words(url):
    soup = fetch_soup(url)
    time.sleep(REQUEST_DELAY)
    console.print(f"[blue]Doing math to count words in {url}...")
    content = soup.select_one("#mw-content-text .mw-parser-output")
    article_text = content.get_text(" ", strip = True)
    time.sleep(REQUEST_DELAY)
    word_count = len(article_text.split())
    return word_count

def fetch_soup(url):
    if not url:
        console.print("[red] give up bro. no link found")
        return None
    response = requests.get(f"{BASE_URL}/{url}", headers = HEADERS, timeout=30)
    time.sleep(REQUEST_DELAY)
    if response.status_code != 200:
        console.print("[red] yeah not working bub. couldn't download.")
        return None
    return BeautifulSoup(response.text, "html.parser")

# it's working! takes in name of location. only works for MHWilds base url. 
def scrape_Monsters(location):
    console.print(f"[blue]Now scraping the {location} for Monsters...")
    response3 = requests.get(f"{BASE_URL}/{location}", headers = HEADERS, timeout = 30) #<-- im gonna stick with response3 since we're doing similar requests
    time.sleep(REQUEST_DELAY)

    if response3.status_code == 200:
        soup = BeautifulSoup(response3.text, "html.parser")
        monsters = soup.find_all("div", {"class": "iconpick"})
        monster_names = []

        # only interested in the big ones
        for monster in monsters:
            name = monster.get_text()
            name_separated = name.split("\n")
            for name in name_separated:
                if name != "":
                    console.print(f"[green]Found: {name}")
                    monster_names.append(name)
                    time.sleep(REQUEST_DELAY)
        
                

    return monster_names



def main():
    console.print("[blue]Now scraping monster locations...")

    # This requests will get the monster locations from MHWilds
    response2 = requests.get(f"{BASE_URL}/MHWilds/Monsters#tabber-By_Locale", headers = HEADERS, timeout = 30)
    time.sleep(REQUEST_DELAY)

    if response2.status_code == 200:

        soup = BeautifulSoup(response2.text, "html.parser")
        
        monster_locations = soup.find_all("h1")
        monster_location_names = []
    
    
        for location in monster_locations[21:27]: # <-- this is also lazy. i scrape only the location names
            name = location.get_text()
            if name not in monster_location_names:
                console.print(f"[green]Found monster location: {name}")
                time.sleep(REQUEST_DELAY)
                monster_location_names.append(name.replace(" ", "_"))


    time.sleep(REQUEST_DELAY)
    console.print("[blue]Building monster_list...")

    # this for loop gets the monsters from every locale
    list_of_monster_lists = []
    for locale in monster_location_names:
        temp = scrape_Monsters(locale)
        list_of_monster_lists.append(temp)

    # this for loop gets the word counts from each article
    list_of_total_words = []
    for locale in monster_location_names:
        temp = count_words(locale)
        list_of_total_words.append(temp)

    list_of_unique_links = []
    for locale in monster_location_names:
        temp = get_internal_links(fetch_soup(locale))
        list_of_unique_links.append(count_links(temp))

    monster_dict = {
        "location": monster_location_names,
        "monster_list" : list_of_monster_lists,
        "word_count": list_of_total_words,
        "number_of_links": list_of_unique_links
    }

    with open('super.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f,fieldnames=monster_dict.keys())
        writer.writeheader()
        writer.writerow(monster_dict)
    
    


main()