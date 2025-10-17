import click
import sys

@click.group()
def cli():
    pass

@cli.command()
def create():
    click.echo("Create new records:")
    click.echo("    1. Mission")
    click.echo("    2. Engineer")
    click.echo("    3. Equipment")
    
    while True:
        choice = click.prompt("Enter your choice").strip().lower()
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

@cli.command()
def delete():
    click.echo("Delete records:")
    click.echo("    1. Mission")
    click.echo("    2. Engineer")
    click.echo("    3. Equipment")
    
    while True:
        choice = click.prompt("Enter your choice").strip().lower()
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

@cli.command()
def update():
    click.echo("Update records:")
    click.echo("    1. Mission")
    click.echo("    2. Engineer")
    click.echo("    3. Equipment")
    
    while True:
        choice = click.prompt("Enter your choice").strip().lower()
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

@cli.command()
def viewanytable():
    click.echo("View any table details:")
    click.echo("    1. Missions")
    click.echo("    2. Engineers")
    click.echo("    3. Equipment")
    click.echo("    4. Engineer-Mission")

    while True:
        choice = click.prompt("Enter your choice").strip().lower()
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

@cli.command()
def search():
    click.echo("Search for records:")
    click.echo("    1. Mission")
    click.echo("    2. Engineer")
    click.echo("    3. Equipment")
    
    while True:
        choice = click.prompt("Enter your choice").strip().lower()
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

@cli.command()
def viewmissionsresources():
    click.echo("View mission resources:")
    click.echo("    1. Mission Equipment")
    click.echo("    2. Mission Engineers")
    
    while True:
        choice = click.prompt("Enter your choice").strip().lower()
        from lib.cli.cli_helpers import view_mission_resources_helper
        if choice == "1" or choice == "mission equipment":
            view_mission_resources_helper.equipment()
            break
        elif choice == "2" or choice == "mission engineers":
            view_mission_resources_helper.engineers()
            break

@cli.group()
def assign():
    pass

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

        if func == "exit":
            click.echo("Exiting CLI... Goodbye! 👋")
            break

        sys.argv = [sys.argv[0], func]

        try:
            cli()
        except SystemExit:
            pass
        except Exception as e:
            click.echo(f"Error: {e}")
