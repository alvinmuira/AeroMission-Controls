import click
from tabulate import tabulate

def mission():
    from lib.models.mission import Mission
    missions = Mission.get_all_missions()
    if not missions:
        click.echo("       ❌ No missions found.")
        return
    headers = ["ID", "Name", "Status", "Launch Date"]
    table = [ [mission.id, mission.name, mission.status, mission.launch_date] for mission in missions ]
    click.echo("\n       ✅  All Missions:\n")
    click.echo(tabulate(table, headers=headers, tablefmt="fancy_grid"))

def engineer():
    from lib.models.engineer import Engineer
    engineers = Engineer.get_all_engineers()
    if not engineers:
        click.echo("       ❌ No engineers found.")
        return
    headers = ["ID", "Name", "Specialization"]
    table = [ [engineer.id, engineer.name, engineer.specialization] for engineer in engineers ]
    click.echo("\n       ✅  All Engineers:\n")
    click.echo(tabulate(table, headers=headers, tablefmt="fancy_grid"))

def equipment():
    from lib.models.equipment import Equipment
    equipment_list = Equipment.get_all_equipment()
    if not equipment_list:
        click.echo("       ❌ No equipment found.")
        return
    headers = ["ID", "Name", "Type", "Mission"]
    table = [ [eq.id, eq.name, eq.type, eq.mission.name] for eq in equipment_list ]
    click.echo("\n       ✅  All Equipment:\n")
    click.echo(tabulate(table, headers=headers, tablefmt="fancy_grid"))

def engineer_mission():
    from lib.models.engineer_mission import EngineerMission
    engineer_missions = EngineerMission.get_all_engineer_missions()
    if not engineer_missions:
        click.echo("       ❌ No engineer-mission assignments found.")
        return
    headers = ["ID", "Engineer ID", "Mission ID", "Engineer Role"]
    table = [ [em.id, em.engineer_id, em.mission_id, em.role] for em in engineer_missions ]
    click.echo("\n       ✅  All Engineer-Mission Assignments:\n")
    click.echo(tabulate(table, headers=headers, tablefmt="fancy_grid"))
