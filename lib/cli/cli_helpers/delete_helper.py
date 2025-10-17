import click

def mission():
    from lib.models.mission import Mission
    value = click.prompt("\nEnter mission name or id to delete")
    if value.isdigit():
        mission = Mission.find_by_id(int(value))
    else:
        mission = Mission.find_mission_by_name(value)
    try:
        mission.delete()
        click.echo(f"       ✅  Deletion of '{mission.name}' mission was successful!")
    except ValueError as ve:
        click.echo(f"       ❌ Error: {ve}")

def engineer():
    from lib.models.engineer import Engineer
    value = click.prompt("\nEnter engineer name or id to delete")
    if value.isdigit():
        engineer = Engineer.find_by_id(int(value))
    else:
        engineer = Engineer.find_engineer_by_name(value)
    try:
        engineer.delete()
        click.echo(f"       ✅  Deletion of engineer 'Eng.{engineer.name}' was successful!")
    except ValueError as ve:
        click.echo(f"       ❌ Error: {ve}")

def equipment():
    from lib.models.equipment import Equipment
    value = click.prompt("\nEnter equipment name or id to delete")
    if value.isdigit():
        equipment = Equipment.find_by_id(int(value))
    else:
        equipment = Equipment.find_equipment_by_name(value)
    if not equipment:
        raise ValueError(f"Equipment with name {value} does not exist.")
    try:
        equipment.delete()
        click.echo(f"       ✅  Deletion of equipment '{equipment.name}' was successful!")
    except ValueError as ve:
        click.echo(f"       ❌ Error: {ve}")