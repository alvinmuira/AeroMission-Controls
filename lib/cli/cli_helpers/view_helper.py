import click

def mission():
    from lib.models.mission import Mission
    missions = Mission.get_all_missions()
    if not missions:
        click.echo("       ❌ No missions found.")
        return
    for mission in missions:
        click.echo(f"      =>Name: {mission.name}, Status: {mission.status}, Launch Date: {mission.launch_date}")