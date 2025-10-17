import click

def mission():
    from lib.models.mission import Mission
    value = click.prompt("\nEnter mission name or id to update")
    if value.isdigit():
        mission = Mission.find_by_id(int(value))
    else:
        mission = Mission.find_mission_by_name(value)
    try:
        if not mission:
            raise ValueError(f"Mission with name {value} does not exist.")
        click.echo(f"      =>Current mission details: Name: {mission.name}, Status: {mission.status}, Launch Date: {mission.launch_date}")
        id_ = mission.id
        name = click.prompt("\nEnter new mission name", type=str)
        status = click.prompt("\nEnter new mission status (Pending, Ongoing, Completed, Cancelled)", type=str)
        launch_date = click.prompt("\nEnter new mission launch date (YYYY-MM-DD)", type=str)
        mission.update(id=id_, name=name, status=status, launch_date=launch_date)
        updated_mission = Mission.find_by_id(id_)
        click.echo(f"       ✅  Update of {mission.name} to {updated_mission.name} mission was successful!")
        click.echo(f"            New Status: {updated_mission.status}, New Launch Date: {updated_mission.launch_date}")
    except ValueError as ve:
        click.echo(f"       ❌ Error: {ve}")

def engineer():
    from lib.models.engineer import Engineer
    value = click.prompt("\nEnter engineer name or id to update")
    if value.isdigit():
        engineer = Engineer.find_by_id(int(value))
    else:
        engineer = Engineer.find_engineer_by_name(value)
    try:
        if not engineer:
            raise ValueError(f"Engineer with name {value} does not exist.")
        click.echo(f"      =>Current engineer details: Name: Eng.{engineer.name}, Specialization: {engineer.specialization}")
        id_ = engineer.id
        name = click.prompt("\nEnter new engineer name", type=str)
        specialization = click.prompt("\nEnter new engineer specialization", type=str)
        engineer.update(id=id_, name=name, specialization=specialization)
        updated_engineer = Engineer.find_by_id(id_)
        click.echo(f"       ✅  Update of Eng.{engineer.name} to Eng.{updated_engineer.name} was successful!")
        click.echo(f"            New Specialization: {updated_engineer.specialization}")
    except ValueError as ve:
        click.echo(f"       ❌ Error: {ve}")

def equipment():
    from lib.models.equipment import Equipment
    value = click.prompt("\nEnter equipment name or id to update")
    if value.isdigit():
        equipment = Equipment.find_by_id(int(value))
    else:
        equipment = Equipment.find_equipment_by_name(value)
    try:
        if not equipment:
            raise ValueError(f"Equipment with name {value} does not exist.")
        click.echo(f"      =>Current equipment details: Name: {equipment.name}, Type: {equipment.type}, Mission: {equipment.mission.name}")
        id_ = equipment.id
        name = click.prompt("\nEnter new equipment name", type=str)
        type_ = click.prompt("\nEnter new equipment type", type=str)
        mission_name = click.prompt("\nEnter new mission name for this equipment", type=str)
        from lib.models.mission import Mission
        mission = Mission.find_mission_by_name(mission_name)
        if not mission:
            raise ValueError(f"Mission with name {mission_name} does not exist.")
        equipment.update(id=id_, name=name, type=type_, mission=mission)
        updated_equipment = Equipment.find_by_id(id_)
        click.echo(f"       ✅  Update of {equipment.name} to {updated_equipment.name} was successful!")
        click.echo(f"            New Type: {updated_equipment.type}, New Mission: {updated_equipment.mission.name}")
    except ValueError as ve:
        click.echo(f"       ❌ Error: {ve}")