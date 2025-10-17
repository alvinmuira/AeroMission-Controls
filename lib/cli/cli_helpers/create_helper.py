import click

def mission():
    from lib.models.mission import Mission
    name = click.prompt("\nEnter mission name", type=str)
    status = click.prompt("\nEnter mission status (Pending, Ongoing, Completed, Cancelled)", type=str)
    launch_date = click.prompt("\nEnter mission launch date (YYYY-MM-DD)", type=str)
    try:
        mission = Mission.create(name=name, status=status, launch_date=launch_date)
        click.echo(click.style(f"       ✅  Creation of {mission.name} mission was successful!", fg="green"))
    except ValueError as ve:
        click.echo(click.style(f"       ❌ Error: {ve}", fg="red"))

def engineer():
    from lib.models.engineer import Engineer
    name = click.prompt("\nEnter engineer name", type=str)
    specialization = click.prompt("\nEnter engineer's specialization", type=str)
    try:
        engineer = Engineer.create(name=name, specialization=specialization)
        click.echo(click.style(f"       ✅  Creation of Eng.{engineer.name} was successful!", fg="green"))
    except ValueError as ve:
        click.echo(click.style(f"       ❌ Error: {ve}", fg="red"))

def equipment():
    from lib.models.equipment import Equipment
    from lib.models.mission import Mission
    name = click.prompt("\nEnter equipment name", type=str)
    type_ = click.prompt("\nEnter equipment type", type=str)
    mission = click.prompt("\nEnter mission name for this equipment", type=str)
    try:
        mission = Mission.find_mission_by_name(mission)
        if not mission:
            raise ValueError(f"Mission with name {mission} does not exist.")
        equipment = Equipment.create(name=name, type=type_, mission=mission)
        click.echo(click.style(f"       ✅  Creation of {equipment.name} for mission {equipment.mission.name} was successful!", fg="green"))
    except ValueError as ve:
        click.echo(click.style(f"       ❌ Error: {ve}", fg="red"))