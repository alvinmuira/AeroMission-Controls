import os
import click
import sys
from lib.cli.cli import cli

def banner():
    click.echo(click.style(r"""
:::'###::::'########:'########:::'#######::'##::::'##:'####::'######:::'######::'####::'#######::'##::: ##::'######::
::'## ##::: ##.....:: ##.... ##:'##.... ##: ###::'###:. ##::'##... ##:'##... ##:. ##::'##.... ##: ###:: ##:'##... ##:
:'##:. ##:: ##::::::: ##:::: ##: ##:::: ##: ####'####:: ##:: ##:::..:: ##:::..::: ##:: ##:::: ##: ####: ##: ##:::..::
'##:::. ##: ######::: ########:: ##:::: ##: ## ### ##:: ##::. ######::. ######::: ##:: ##:::: ##: ## ## ##:. ######::
:#########: ##...:::: ##.. ##::: ##:::: ##: ##. #: ##:: ##:::..... ##::..... ##:: ##:: ##:::: ##: ##. ####::..... ##:
:##.... ##: ##::::::: ##::. ##:: ##:::: ##: ##:.:: ##:: ##::'##::: ##:'##::: ##:: ##:: ##:::: ##: ##:. ###:'##::: ##:
:##:::: ##: ########: ##:::. ##:. #######:: ##:::: ##:'####:. ######::. ######::'####:. #######:: ##::. ##:. ######::
..:::::..::........::..:::::..:::.......:::..:::::..::....:::......::::......:::....:::.......:::..::::..:::......:::
::::::::::::::::'######:::'#######::'##::: ##:'########:'########:::'#######::'##::::::::'######:::::::::::::::::::::
:::::::::::::::'##... ##:'##.... ##: ###:: ##:... ##..:: ##.... ##:'##.... ##: ##:::::::'##... ##::::::::::::::::::::
::::::::::::::: ##:::..:: ##:::: ##: ####: ##:::: ##:::: ##:::: ##: ##:::: ##: ##::::::: ##:::..::::::::::::::::::::: 
::::::::::::::: ##::::::: ##:::: ##: ## ## ##:::: ##:::: ########:: ##:::: ##: ##:::::::. ######::::::::::::::::::::: 
::::::::::::::: ##::::::: ##:::: ##: ##. ####:::: ##:::: ##.. ##::: ##:::: ##: ##::::::::..... ##:::::::::::::::::::: 
::::::::::::::: ##::: ##: ##:::: ##: ##:. ###:::: ##:::: ##::. ##:: ##:::: ##: ##:::::::'##::: ##:::::::::::::::::::: 
:::::::::::::::. ######::. #######:: ##::. ##:::: ##:::: ##:::. ##:. #######:: ########:. ######::::::::::::::::::::: 
::::::::::::::::......::::.......:::..::::..:::::..:::::..:::::..:::.......:::........:::......:::::::::::::::::::::: 
    """, fg="magenta", bold=True) )

def initialize_app():
    from db_setup import setup_database
    setup_database()
    click.echo(click.style("📦 Database checked and ready!", fg="green"))

def run_cli():
    while True:
        click.echo(click.style("\n" + "="*50, fg="magenta", bold=True))
        click.echo(click.style("\nWelcome to the 🚀 AeroMission Controls ⚙️ CLI!", fg="magenta", bold=True))
        click.echo(click.style("="*50, fg="magenta", bold=True))
        click.echo(click.style("\nAvailable commands:", fg="blue", bold=True))
        click.echo(click.style("    1.Create", fg="cyan"))
        click.echo(click.style("    2.Delete", fg="cyan"))
        click.echo(click.style("    3.Update", fg="cyan"))
        click.echo(click.style("    4.View Any Table", fg="cyan"))
        click.echo(click.style("    5.Search", fg="cyan"))
        click.echo(click.style("    6.View Missions Resources", fg="cyan"))
        click.echo(click.style("    7.Assign", fg="cyan"))
        click.echo(click.style("    8.Exit", fg="red", bold=True))

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
            click.echo(click.style("\nExiting CLI... Goodbye! 👋\n", fg="green", bold=True, italic=True))
            break

        sys.argv = [sys.argv[0], func]

        try:
            cli()
        except SystemExit:
            pass
        except Exception as e:
            click.echo(f"Error: {e}")

def main():
    banner()
    initialize_app()
    run_cli()

if __name__ == "__main__":
    main()
