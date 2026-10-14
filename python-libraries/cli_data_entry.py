from rich.console import Console
from rich.table import Table
import csv
import os

console = Console()
console.print("Here is a table about video games and it's initial data:", style = "bold green")

# Yeah I know how to comment what about it 
# we add our columns and then rows to our freshly initialized table
table = Table(title = "Video Games")
table.add_column("Title", style = "cyan", no_wrap = True )
table.add_column("Developer", style = "turquoise4") # okay so turquoise4 is supported by rich, but not 'orange'. sure dude
table.add_column("Release Date", style = "aquamarine3", justify = "right")

# lets make a dictionary to hold our data, but we will not use it for the table, just for the csv file
##game_data = [
##    {"Title": "The Legend of Zelda: Breath of the Wild", "Developer": "Nintendo", "Release Date": "March 3, 2017"},
##    {"Title": "God of War", "Developer": "Santa Monica Studio", "Release Date": "April 20, 2018"},
##    {"Title": "Red Dead Redemption 2", "Developer": "Rockstar Games", "Release Date": "October 26, 2018"}
##]

# if the csv file exists, we can read from it and populate our dictionary with the data.
# so we make an if statement to check if the csv exists, else we generate it with our starting data
if os.path.exists("csvfile.csv"):
    game_data = []
    with open("csvfile.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            game_data.append(row)
else:
    game_data = [
        {"Title": "The Legend of Zelda: Breath of the Wild", "Developer": "Nintendo", "Release Date": "March 3 2017"},
        {"Title": "God of War", "Developer": "Santa Monica Studio", "Release Date": "April 20 2018"},
        {"Title": "Red Dead Redemption 2", "Developer": "Rockstar Games", "Release Date": "October 26 2018"}
    ]

# yeah we be adding our rows with a for loop from our dictionary
for game in game_data:
    table.add_row(game["Title"], game["Developer"], game["Release Date"])
        
"""okay so this probably unnecessary, but I couldn't pull data out of the rich table.
I think because the rich table doesn't actually hold data that way? So the dictionary
was made so I can write to the csv file."""        

console.print(table)
console.print("\n[bold green] Enter your own video game data below:[/bold green]")

# we use a while loop to let the user enter more than one row 
while True:

    game_title = input("Enter the title of the video game (or type 'exit' to quit): ") 

    if game_title.lower() == 'exit':                                                    # we use .lower in case we type with capitals 
        break                                                                           # this gets us out of the loop

    game_developer = input("Enter the developer of the video game: ")
    game_release_date = input("Enter the release date of the video game: ")

    # we gotta ask if the submission is good
    confirmation = input(f"Are you sure you want to add '{game_title}' by '{game_developer}' released on '{game_release_date}'? (yes/no): ")

    if confirmation.lower() == 'yes':
        table.add_row(game_title, game_developer, game_release_date)
        console.print("Entry added. Add another row.", style = "bold green")

        with open("csvfile.csv", "a") as file:                                  
            file.write(f"{game_title},{game_developer},{game_release_date}\n") # we write to the csv file

    else:
        console.print("Entry not added. Please try again.", style = "bold red")

console.print(table)
console.print(f"\n[bold green]This program wrote data to 'csvfile.csv' at {os.path.abspath('csvfile.csv')} [/bold green]")