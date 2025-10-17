import click

def mission():
    from lib.models.mission import Mission
    value = click.prompt("Enter mission name or id to update")
    if value.isdigit():
        mission = Mission.find_by_id(int(value))
    else:
        mission = Mission.find_mission_by_name(value)
    try:
        if not mission:
            raise ValueError(f"Mission with name {value} does not exist.")
        click.echo(f"      =>Current mission details: Name: {mission.name}, Status: {mission.status}, Launch Date: {mission.launch_date}")
        id_ = mission.id
        name = click.prompt("Enter new mission name", type=str)
        status = click.prompt("Enter new mission status (Pending, Ongoing, Completed, Cancelled)", type=str)
        launch_date = click.prompt("Enter new mission launch date (YYYY-MM-DD)", type=str)
        mission.update(id=id_, name=name, status=status, launch_date=launch_date)
        click.echo(f"       ✅  Update of {mission.name} mission was successful!")
    except ValueError as ve:
        click.echo(f"       ❌ Error: {ve}")