import click

def engineer_to_mission():
    from lib.models.mission import Mission
    mission = click.prompt("Enter mission name or id", type=str)
    if mission.isdigit():
        mission = Mission.find_by_id(int(mission))
    else:
        mission = Mission.find_mission_by_name(mission)
    if not mission:
        raise ValueError(f"Mission with name {mission} does not exist.")
    engineer = click.prompt("Enter engineer's name or id", type=str)
    from lib.models.engineer import Engineer
    if engineer.isdigit():
        engineer = Engineer.find_by_id(int(engineer))
    else:
        engineer = Engineer.find_engineer_by_name(engineer)
    if not engineer:
        raise ValueError(f"Engineer with name {engineer} does not exist.")
    role = click.prompt("Enter engineer's role in the mission", type=str)
    try:
        mission.assign_an_engineer(engineer, role)
        click.echo(f"       ✅  Assignment of Eng.{engineer.name} to {mission.name} mission as {role} was successful!")
    except ValueError as ve:
        click.echo(f"       ❌ Error: {ve}")