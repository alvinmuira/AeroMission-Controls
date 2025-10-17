import click

def mission():
    from lib.models.mission import Mission
    name = click.prompt("Enter mission name", type=str)
    status = click.prompt("Enter mission status (Pending, Ongoing, Completed, Cancelled)", type=str)
    launch_date = click.prompt("Enter mission launch date (YYYY-MM-DD)", type=str)
    try:
        mission = Mission.create(name=name, status=status, launch_date=launch_date)
        click.echo(f"       ✅  Creation of {mission.name} mission was successful!")
    except ValueError as ve:
        click.echo(f"       ❌ Error: {ve}")

def engineer():
    from lib.models.engineer import Engineer
    name = click.prompt("Enter engineer name", type=str)
    specialization = click.prompt("Enter engineer's specialization", type=str)
    try:
        engineer = Engineer.create(name=name, specialization=specialization)
        click.echo(f"       ✅  Creation of Eng.{engineer.name} was successful!")
    except ValueError as ve:
        click.echo(f"       ❌ Error: {ve}")

def equipment():
    from lib.models.equipment import Equipment
    from lib.models.mission import Mission
    name = click.prompt("Enter equipment name", type=str)
    type_ = click.prompt("Enter equipment type", type=str)
    mission = click.prompt("Enter mission name for this equipment", type=str)
    try:
        mission = Mission.find_mission_by_name(mission)
        if not mission:
            raise ValueError(f"Mission with name {mission} does not exist.")
        equipment = Equipment.create(name=name, type=type_, mission=mission)
        click.echo(f"       ✅  Creation of {equipment.name} for mission {equipment.mission.name} was successful!")
    except ValueError as ve:
        click.echo(f"       ❌ Error: {ve}")