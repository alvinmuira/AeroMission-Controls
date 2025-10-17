from lib.models.equipment import Equipment
for e in Equipment.get_all_equipment():
    print(e.name, e.type, e.mission.name)

from lib.models.mission import Mission
for m in Mission.get_all_missions():
    print(m.name, m.status, m.launch_date)