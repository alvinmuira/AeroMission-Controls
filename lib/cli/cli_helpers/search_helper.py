import click
from tabulate import tabulate

def mission():
    choice = click.prompt("\nDo you want to search a specific mission or view by status?\n (1) Specific Mission\n (2) By Status\n Enter choice", type=str)
    if choice == "1" or choice == "specific mission":
        _search_specific_mission()
    elif choice == "2" or choice == "by status":
        _search_by_status()

def engineer():
    from lib.models.engineer import Engineer
    value = click.prompt("\nEnter engineer name or id to view")
    if value.isdigit():
        engineer = Engineer.find_by_id(int(value))
    else:
        engineer = Engineer.find_engineer_by_name(value)
    try:
        if not engineer:
            raise ValueError(f"Engineer with name {value} does not exist.")
        click.echo(click.style(f"\n       =>Engineer details:\n ID: {engineer.id},\n Name: Eng.{engineer.name},\n Specialization: {engineer.specialization}\n", fg="cyan"))
    except ValueError as ve:
        click.echo(click.style(f"       ❌ Error: {ve}", fg="red"))

def equipment():
    from lib.models.equipment import Equipment
    value = click.prompt("\nEnter equipment name or id to view")
    if value.isdigit():
        equipment = Equipment.find_by_id(int(value))
    else:
        equipment = Equipment.find_equipment_by_name(value)
    try:
        if not equipment:
            raise ValueError(f"Equipment with name {value} does not exist.")
        click.echo(click.style(f"\n       =>Equipment details:\n ID: {equipment.id},\n Name: {equipment.name},\n Type: {equipment.type},\n Mission: {equipment.mission.name}\n", fg="cyan"))
    except ValueError as ve:
        click.echo(click.style(f"       ❌ Error: {ve}", fg="red"))

def _search_specific_mission():
    from lib.models.mission import Mission
    value = click.prompt("\nEnter mission name or id to view")
    if value.isdigit():
        mission = Mission.find_by_id(int(value))
    else:
        mission = Mission.find_mission_by_name(value)
    try:
        if not mission:
            raise ValueError(f"Mission with name {value} does not exist.")
        click.echo(click.style(f"\n       =>Mission details:\n ID: {mission.id},\n Name: {mission.name},\n Status: {mission.status},\n Launch Date: {mission.launch_date}\n", fg="cyan"))
    except ValueError as ve:
        click.echo(click.style(f"       ❌ Error: {ve}", fg="red"))

def _search_by_status():
    from lib.models.mission import Mission
    status = click.prompt("\nEnter mission status to filter by (Pending, Ongoing, Completed, Cancelled)", type=str)
    try:
        missions = Mission.get_missions_with_status(status)
        if not missions:
            raise ValueError(f"No missions found with status {status}.")
        click.echo(click.style(f"\n       =>Missions with status '{status}':\n", fg="cyan"))
        headers = ["ID", "Name", "Launch Date"]
        table = [ [mission.id, mission.name, mission.launch_date] for mission in missions ]
        click.echo(tabulate(table, headers=headers, tablefmt="fancy_grid"))
    except ValueError as ve:
        click.echo(click.style(f"       ❌ Error: {ve}", fg="red"))