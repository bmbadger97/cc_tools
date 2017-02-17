import cc_data
import json


def make_cc_dat_from_json(json_file):
    cc_data_file = cc_data.CCDataFile()
    with open(json_file, 'r') as reader:
        json_data = json.load(reader)
    for json_level in json_data:
        cc_level = make_level_from_json(json_level)
        cc_data_file.add_level(cc_level)
    return cc_data_file

def make_level_from_json(json_data):
        cc_level = cc_data.CCLevel()
        cc_level.level_number = json_data["level_number"]
        cc_level.time = json_data["time"]
        cc_level.num_chips = json_data["num_chips"]
        cc_level.upper_layer = json_data["upper_layer"]
        cc_level.lower_layer = json_data["lower_layer"]
        cc_level.optional_fields = make_optional_fields_from_json(json_data["optional_fields"])
        return cc_level

def make_optional_fields_from_json(json_optional_fields):
    cc_fields = []
    for json_field in json_optional_fields:
        field_type = json_field["type"]
        if field_type == cc_data.CCMapTitleField.TYPE:  #field_type == 3
            cc_field = cc_data.CCMapTitleField(json_field["title"])
            cc_fields.append(cc_field)
        elif field_type == cc_data.CCTrapControlsField.TYPE:        #field_type == 4
            cc_traps = []
            for json_trap in json_field["traps"]:
                bx = json_trap["button"][0]
                by = json_trap["button"][1]
                tx = json_trap["trap"][0]
                ty = json_trap["trap"][1]
                cc_traps.append(cc_data.CCCoordinate(bx, by, tx, ty))
            cc_field = cc_data.CCTrapControlsField(cc_traps)
            cc_fields.append(cc_field)
        elif field_type == cc_data.CCCloningMachineControlsField.TYPE:  #field_type == 5
            cc_machines = []
            for json_machine in json_field["cloning_machines"]:
                bx = json_machine["button"][0]
                by = json_machine["button"][1]
                tx = json_machine["machine"][0]
                ty = json_machine["machine"][1]
                cc_machines.append(cc_data.CCCoordinate(bx, by, tx, ty))
            cc_field = cc_data.CCCloningMachineControlsField(cc_machines)
            cc_fields.append(cc_field)
        elif field_type == cc_data.CCEncodedPasswordField.TYPE:     #field_type == 6
            cc_field = cc_data.CCEncodedPasswordField(json_field["password"])
            cc_fields.append(cc_field)
        elif field_type == cc_data.CCMapHintField.TYPE:     #field_type == 7
            cc_field = cc_data.CCMapHintField(json_field["hint"])
            cc_fields.append(cc_field)
        elif field_type == cc_data.CCMonsterMovementField.TYPE:  #field_type == 10
            cc_monsters = []
            for json_mon in json_field["monsters"]:
                x = json_mon[0]
                y = json_mon[1]
                cc_monsters.append(cc_data.CCCoordinate(x, y))
            cc_field = cc_data.CCMonsterMovementField(cc_monsters)
            cc_fields.append(cc_field)
    return cc_fields
