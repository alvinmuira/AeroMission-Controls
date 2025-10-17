import click

def engineer_to_mission():
    from lib.models.mission import Mission
    mission = click.prompt("\nEnter mission name or id", type=str)
    if mission.isdigit():
        mission = Mission.find_by_id(int(mission))
    else:
        mission = Mission.find_mission_by_name(mission)
    if not mission:
        raise ValueError(f"Mission with name {mission} does not exist.")
    engineer = click.prompt("\nEnter engineer's name or id", type=str)
    from lib.models.engineer import Engineer
    if engineer.isdigit():
        engineer = Engineer.find_by_id(int(engineer))
    else:
        engineer = Engineer.find_engineer_by_name(engineer)
    if not engineer:
        raise ValueError(f"Engineer with name {engineer} does not exist.")
    role = click.prompt("\nEnter engineer's role in the mission", type=str)
    try:
        mission.assign_an_engineer(engineer, role)
        click.echo(f"       ✅  Assignment of Eng.{engineer.name} to {mission.name} mission as {role} was successful!")
    except ValueError as ve:
        click.echo(f"       ❌ Error: {ve}")

def equipment_to_mission():
    from lib.models.mission import Mission
    mission = click.prompt("\nEnter mission name or id", type=str)
    if mission.isdigit():
        mission = Mission.find_by_id(int(mission))
    else:
        mission = Mission.find_mission_by_name(mission)
    if not mission:
        raise ValueError(f"Mission with name {mission} does not exist.")
    from lib.models.equipment import Equipment
    name = click.prompt("\nEnter equipment name", type=str)
    type_ = click.prompt("\nEnter equipment type", type=str)
    try:
        equipment = Equipment.create(name=name, type=type_, mission=mission)
        click.echo(f"       ✅  Creation of {equipment.name} for mission {equipment.mission.name} was successful!")
    except ValueError as ve:
        click.echo(f"       ❌ Error: {ve}")