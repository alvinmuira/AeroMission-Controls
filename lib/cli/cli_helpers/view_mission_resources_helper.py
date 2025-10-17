import click

def equipment():
    value = click.prompt("Enter mission name or id to view")
    from lib.models.mission import Mission
    if value.isdigit():
        mission = Mission.find_by_id(int(value))
    else:
        mission = Mission.find_mission_by_name(value)
    try:
        mission.view_mission_equipment()
        if not mission:
            raise ValueError(f"No equipment found on the {value} mission.")
    except ValueError as ve:
        click.echo(f"       ❌ Error: {ve}")
        return

def engineers():
    value = click.prompt("Enter mission name or id to view")
    from lib.models.mission import Mission
    if value.isdigit():
        mission = Mission.find_by_id(int(value))
    else:
        mission = Mission.find_mission_by_name(value)
    try:
        mission.view_mission_engineers()
        if not mission:
            raise ValueError(f"No engineers found on the {value} mission.")
    except ValueError as ve:
        click.echo(f"       ❌ Error: {ve}")
        return
