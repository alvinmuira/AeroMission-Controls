import click

def mission():
    from lib.models.mission import Mission
    value = click.prompt("Enter mission name or id to view")
    if value.isdigit():
        mission = Mission.find_by_id(int(value))
    else:
        mission = Mission.find_mission_by_name(value)
    try:
        if not mission:
            raise ValueError(f"Mission with name {value} does not exist.")
        click.echo(f"\n       =>Mission details:\n ID: {mission.id},\n Name: {mission.name},\n Status: {mission.status},\n Launch Date: {mission.launch_date}\n")
    except ValueError as ve:
        click.echo(f"       ❌ Error: {ve}")

def engineer():
    from lib.models.engineer import Engineer
    value = click.prompt("Enter engineer name or id to view")
    if value.isdigit():
        engineer = Engineer.find_by_id(int(value))
    else:
        engineer = Engineer.find_engineer_by_name(value)
    try:
        if not engineer:
            raise ValueError(f"Engineer with name {value} does not exist.")
        click.echo(f"\n       =>Engineer details:\n ID: {engineer.id},\n Name: Eng.{engineer.name},\n Specialization: {engineer.specialization}\n")
    except ValueError as ve:
        click.echo(f"       ❌ Error: {ve}")

def equipment():
    from lib.models.equipment import Equipment
    value = click.prompt("Enter equipment name or id to view")
    if value.isdigit():
        equipment = Equipment.find_by_id(int(value))
    else:
        equipment = Equipment.find_equipment_by_name(value)
    try:
        if not equipment:
            raise ValueError(f"Equipment with name {value} does not exist.")
        click.echo(f"\n       =>Equipment details:\n ID: {equipment.id},\n Name: {equipment.name},\n Type: {equipment.type},\n Mission: {equipment.mission.name}\n")
    except ValueError as ve:
        click.echo(f"       ❌ Error: {ve}")