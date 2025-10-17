import click
import sys

@click.group()
def cli():
    pass

@cli.command()
def create():
    pass

@cli.command()
def delete():
    pass

@cli.command()
def update():
    pass

@cli.command()
def view_any_table():
    pass

@cli.command()
def search():
    pass

@cli.command()
def view_missions_resources():
    pass

@cli.command()
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
