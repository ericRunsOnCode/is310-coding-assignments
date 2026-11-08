import time
import json
import csv
import apikey
import requests
from bs4 import BeautifulSoup
from rich.console import Console
console = Console()
HEADERS = {
    "User-Agent": "is310-course/1.0 (https://ericRunsOnCode.github.io; ecampos3@illinois.edu)"
}

API_URL = "https://slay-the-spire.fandom.com/api.php"
STEAM_API = "https://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid=440&format=xml"
COUNT = 1

# returns two lists, one of achievement names and one of achievement descriptions. from https://slay-the-spire.fandom.com/wiki/Achievements
def get_achievements():
    params= {
        "action": "parse",
        "page": "Achievements",
        "prop": "text",
        "format": "json",

    }

    category_response = requests.get(
        API_URL,
        params = params,
        headers=HEADERS,
        timeout = 15 
    )


    if category_response.status_code == 200:
        data = category_response.json()
        # we look for the table and get the name and description of each achievement.
        html_content = data["parse"]["text"]["*"]
        soup = BeautifulSoup(html_content, "html.parser")
        achievements = soup.find_all("tr")[1:]  # Skip the header row
        achievement_name_list = []
        achievement_description_list = []
        for achievement in achievements:
            names = achievement.get_text()
            names = names.strip()
            names = names.split("\n")
            achievement_name_list.append(names[0].replace(" ", "_").lower()) # <-- doing this to get in it line with the formatting of the steam api
            # achievement_description_list.append(names[2]) # we dont need the descriptions 

    json_str = json.dumps(data)
    with open ("FandomWiki.json", "w") as f:
        f.write(json_str)

    return achievement_name_list


# returns two lists. a list of booleans(if the achievement was found), a list of steam api achievements
def getGlobalAchievementData(achievements):
    category_response = requests.get(
            "https://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid=646570&format=json",
            headers=HEADERS,
            timeout = 15 
        )

    
    global_achievement_names = []
    booleans = []
    if category_response.status_code == 200:
        data = category_response.json()
        for achievement in data["achievementpercentages"]["achievements"]:
            global_achievement_names.append(achievement["name"].lower())
        global_achievement_names.sort()

        for achievement in global_achievement_names:
            if achievement in achievements:
                booleans.append(True)
            else: booleans.append(False)
        return global_achievement_names, booleans
    else:
        console.print("[red]Failed to fetch global achievement data.")
        return None

    



# takes in a villain's page text. return a count of words with no definition, a count of words with a definition, and a list of words with no defintion
def get_def(pageText):
    return None
                

def main():
    console.print("[yellow]Getting list of achievements and their descriptions from the Slay The Spire Fandom Wiki...")
    achievementNames = get_achievements()
    achievementNames.sort()

    console.print("[yellow]Getting global achievement data from the Steam API...")
    global_List, boolean_List = getGlobalAchievementData(achievementNames)

    sortedSteam = []
    sortedWiki = []
    sortedBoolean = []

    for achievement in global_List:
        if achievement in achievementNames:
            sortedSteam.append(achievement)
            sortedWiki.append(achievement)
            sortedBoolean.append(True)
        else: 
            sortedSteam.append(achievement)
            sortedWiki.append("NULL")
            sortedBoolean.append(False)


    
    fieldnames = ["Steam API Achievements", "MediaWiki API Achievements", "Query Boolean"]
    with open("achievement_data.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(sortedSteam)):
            writer.writerow({
                "Steam API Achievements": sortedSteam[i],
                "MediaWiki API Achievements": sortedWiki[i] if i < len(sortedWiki) else "",
                "Query Boolean": sortedBoolean[i] if i < len(sortedBoolean) else ""
            })

    

main()