from rich.console import Console
from rich.table import Table

console = Console()
console.print("Here is a table about video games and it's initial data:", style = "bold green")

# Yeah I know how to comment what about it 
# we add our columns and then rows to our freshly initialized table
table = Table(title = "Video Games")
table.add_column("Title", style = "cyan", no_wrap = True )
table.add_column("Developer", style = "turquoise4") # okay so turquoise4 is supported by rich, but not 'orange'. sure dude
table.add_column("Release Date", style = "aquamarine3", justify = "right")

# yeah we be adding our rows
table.add_row("The Legend of Zelda: Breath of the Wild", "Nintendo", "March 3, 2017")
table.add_row("God of War", "Santa Monica Studio", "April 20, 2018")
table.add_row("Red Dead Redemption 2", "Rockstar Games", "October 26, 2018")

console.print(table)
console.print("\n[bold green] Enter your own video game data below:[/bold green]")

