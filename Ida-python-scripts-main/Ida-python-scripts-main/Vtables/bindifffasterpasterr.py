import idaapi as api
import idc as idc
import json

# ask for the dumped file from dumper.py
path = api.ask_file(False, "*.json", "Input file, generated by dumper.py")

# dump dumper.py file into dict
with open(path, "r") as f:
    data = json.load(f)

# Iterate over each entry in the JSON data
for entry in data:
    first_name = entry["first_name"]
    second_name = entry["second_name"]
    
    # Find the address of the first name
    address = idc.get_name_ea_simple(first_name)
    if address != idc.BADADDR:
        # Rename the address with the second name and suppress warnings about '<'
        idc.set_name(address, second_name, idc.SN_NOWARN)
        print(f"Renamed {first_name} to {second_name}")
    else:
        print(f"Function {first_name} not found in the database")

api.msg(f"\nPasted Vtable")
