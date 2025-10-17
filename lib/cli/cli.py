import click
import sys

@click.group()
def cli():
    pass

back_choices = ["back", "return", "exit", "quit", "main menu", "menu"]

@cli.command()
def create():
    click.echo("Create new records:")
    click.echo("    1. Mission")
    click.echo("    2. Engineer")
    click.echo("    3. Equipment")
    click.echo("    4. Back")
    
    while True:
        choice = click.prompt("\nEnter your choice").strip().lower()
        from lib.cli.cli_helpers import create_helper
        if choice == "1" or choice == "mission":
            create_helper.mission()
            break
        elif choice == "2" or choice == "engineer":
            create_helper.engineer()
            break
        elif choice == "3" or choice == "equipment":
            create_helper.equipment()
            break
        elif choice == "4" or choice in back_choices:
            click.echo("\nReturning to main menu...")
            break

@cli.command()
def delete():
    click.echo("Delete records:")
    click.echo("    1. Mission")
    click.echo("    2. Engineer")
    click.echo("    3. Equipment")
    click.echo("    4. Back")
    
    while True:
        choice = click.prompt("\nEnter your choice").strip().lower()
        from lib.cli.cli_helpers import delete_helper
        if choice == "1" or choice == "mission":
            delete_helper.mission()
            break
        elif choice == "2" or choice == "engineer":
            delete_helper.engineer()
            break
        elif choice == "3" or choice == "equipment":
            delete_helper.equipment()
            break
        elif choice == "4" or choice in back_choices:
            click.echo("\nReturning to main menu...")
            break

@cli.command()
def update():
    click.echo("Update records:")
    click.echo("    1. Mission")
    click.echo("    2. Engineer")
    click.echo("    3. Equipment")
    click.echo("    4. Back")
    
    while True:
        choice = click.prompt("\nEnter your choice").strip().lower()
        from lib.cli.cli_helpers import update_helper
        if choice == "1" or choice == "mission":
            update_helper.mission()
            break
        elif choice == "2" or choice == "engineer":
            update_helper.engineer()
            break
        elif choice == "3" or choice == "equipment":
            update_helper.equipment()
            break
        elif choice == "4" or choice in back_choices:
            click.echo("\nReturning to main menu...")
            break

@cli.command()
def view_any_table():
    click.echo("View any table details:")
    click.echo("    1. Missions")
    click.echo("    2. Engineers")
    click.echo("    3. Equipment")
    click.echo("    4. Engineer-Mission")
    click.echo("    5. Back")

    while True:
        choice = click.prompt("\nEnter your choice").strip().lower()
        from lib.cli.cli_helpers import view_helper
        if choice == "1" or choice == "missions":
            view_helper.mission()
            break
        elif choice == "2" or choice == "engineers":
            view_helper.engineer()
            break
        elif choice == "3" or choice == "equipment":
            view_helper.equipment()
            break
        elif choice == "4" or choice == "engineer-mission":
            view_helper.engineer_mission()
            break
        elif choice == "5" or choice in back_choices:
            click.echo("\nReturning to main menu...")
            break

@cli.command()
def search():
    click.echo("Search for records:")
    click.echo("    1. Mission")
    click.echo("    2. Engineer")
    click.echo("    3. Equipment")
    click.echo("    4. Back")
    
    while True:
        choice = click.prompt("\nEnter your choice").strip().lower()
        from lib.cli.cli_helpers import search_helper
        if choice == "1" or choice == "mission":
            search_helper.mission()
            break
        elif choice == "2" or choice == "engineer":
            search_helper.engineer()
            break
        elif choice == "3" or choice == "equipment":
            search_helper.equipment()
            break
        elif choice == "4" or choice in back_choices:
            click.echo("\nReturning to main menu...")
            break

@cli.command()
def view_missions_resources():
    click.echo("View mission resources:")
    click.echo("    1. Mission Equipment")
    click.echo("    2. Mission Engineers")
    click.echo("    3. Back")
    
    while True:
        choice = click.prompt("\nEnter your choice").strip().lower()
        from lib.cli.cli_helpers import view_mission_resources_helper
        if choice == "1" or choice == "mission equipment":
            view_mission_resources_helper.equipment()
            break
        elif choice == "2" or choice == "mission engineers":
            view_mission_resources_helper.engineers()
            break
        elif choice == "3" or choice in back_choices:
            click.echo("\nReturning to main menu...")
            break

@cli.command()
def assign():
    click.echo("Assign resources:")
    click.echo("    1. Assign Engineer to Mission")
    click.echo("    2. Assign Equipment to Mission")
    click.echo("    3. Back")
    
    while True:
        choice = click.prompt("\nEnter your choice").strip().lower()
        from lib.cli.cli_helpers import assign_helper
        if choice == "1" or choice == "assign engineer to mission":
            assign_helper.engineer_to_mission()
            break
        elif choice == "2" or choice == "assign equipment to mission":
            assign_helper.equipment_to_mission()
            break
        elif choice == "3" or choice in back_choices:
            click.echo("\nReturning to main menu...")
            break

if __name__ == '__main__':
    while True:
        click.echo("\nWelcome to the 🚀 AeroMission Controls ⚙️ CLI!")
        click.echo("\nAvailable commands:")
        click.echo("    1.Create")
        click.echo("    2.Delete")
        click.echo("    3.Update")
        click.echo("    4.View Any Table")
        click.echo("    5.Search")
        click.echo("    6.View Missions Resources")
        click.echo("    7.Assign")
        click.echo("    8.Exit")

        func = click.prompt(
            "\nEnter function to execute",
            type=str
        ).strip().lower()

        commands = {
            "create": "create",
            "delete": "delete",
            "update": "update",
            "view any table": "view-any-table",
            "search": "search",
            "view missions resources": "view-missions-resources",
            "assign": "assign",
            "exit": "exit",
            "1": "create",
            "2": "delete",
            "3": "update",
            "4": "view-any-table",
            "5": "search",
            "6": "view-missions-resources",
            "7": "assign",
            "8": "exit"
        }

        func = commands.get(func, func)

        if func == "exit":
            click.echo("\nExiting CLI... Goodbye! 👋\n")
            break

        sys.argv = [sys.argv[0], func]

        try:
            cli()
        except SystemExit:
            pass
        except Exception as e:
            click.echo(f"Error: {e}")
