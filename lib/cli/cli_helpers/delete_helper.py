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
        click.echo(click.style(f"       ✅  Deletion of '{mission.name}' mission was successful!", fg="green"))
    except ValueError as ve:
        click.echo(click.style(f"       ❌ Error: {ve}", fg="red"))

def engineer():
    from lib.models.engineer import Engineer
    value = click.prompt("\nEnter engineer name or id to delete")
    if value.isdigit():
        engineer = Engineer.find_by_id(int(value))
    else:
        engineer = Engineer.find_engineer_by_name(value)
    try:
        engineer.delete()
        click.echo(click.style(f"       ✅  Deletion of engineer 'Eng.{engineer.name}' was successful!", fg="green"))
    except ValueError as ve:
        click.echo(click.style(f"       ❌ Error: {ve}", fg="red"))

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
        click.echo(click.style(f"       ✅  Deletion of equipment '{equipment.name}' was successful!", fg="green"))
    except ValueError as ve:
        click.echo(click.style(f"       ❌ Error: {ve}", fg="red"))