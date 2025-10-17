import click
from tabulate import tabulate

def mission():
    from lib.models.mission import Mission
    missions = Mission.get_all_missions()
    if not missions:
        click.echo(click.style("       ❌ No missions found.", fg="red"))
        return
    headers = ["ID", "Name", "Status", "Launch Date"]
    table = [ [mission.id, mission.name, mission.status, mission.launch_date] for mission in missions ]
    click.echo(click.style("\n       ✅  All Missions:\n", fg="green"))
    click.echo(tabulate(table, headers=headers, tablefmt="fancy_grid"))

def engineer():
    from lib.models.engineer import Engineer
    engineers = Engineer.get_all_engineers()
    if not engineers:
        click.echo(click.style("       ❌ No engineers found.", fg="red"))
        return
    headers = ["ID", "Name", "Specialization"]
    table = [ [engineer.id, engineer.name, engineer.specialization] for engineer in engineers ]
    click.echo(click.style("\n       ✅  All Engineers:\n", fg="green"))
    click.echo(tabulate(table, headers=headers, tablefmt="fancy_grid"))

def equipment():
    from lib.models.equipment import Equipment
    equipment_list = Equipment.get_all_equipment()
    if not equipment_list:
        click.echo(click.style("       ❌ No equipment found.", fg="red"))
        return
    headers = ["ID", "Name", "Type", "Mission"]
    table = [ [eq.id, eq.name, eq.type, eq.mission.name] for eq in equipment_list ]
    click.echo(click.style("\n       ✅  All Equipment:\n", fg="green"))
    click.echo(tabulate(table, headers=headers, tablefmt="fancy_grid"))

def engineer_mission():
    from lib.models.engineer_mission import EngineerMission
    engineer_missions = EngineerMission.get_all_engineer_missions()
    if not engineer_missions:
        click.echo(click.style("       ❌ No engineer-mission assignments found.", fg="red"))
        return
    headers = ["ID", "Engineer ID", "Engineer Name", "Mission ID", "Mission Name", "Engineer Role"]
    table = [ [em.id, em.engineer.id, em.engineer.name, em.mission.id, em.mission.name, em.role] for em in engineer_missions ]
    click.echo(click.style("\n       ✅  All Engineer-Mission Assignments:\n", fg="green"))
    click.echo(tabulate(table, headers=headers, tablefmt="fancy_grid"))
