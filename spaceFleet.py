docking_bays = [
    {"id": 1, "size": "small", "schedule": []},
    {"id": 2, "size": "medium", "schedule": []},
    {"id": 3, "size": "large", "schedule": []},
]

spaceships = [
    {"name": "Alpha", "size": "small", "arrival": "12:00", "departure": "14:00"},
    {"name": "Alpha", "size": "medium", "arrival": "13:00", "departure": "15:00"},
    {"name": "Alpha", "size": "large", "arrival": "14:00", "departure": "16:00"},
]

def get_availible_bays(ship_size):
    return [bay["id"] for bay in docking_bays if bay["size"] == ship_size]

def check_time_conflict(bay, arrival, departure):
    for scheduled_ship in bay["schedule"]:
        if not (departure <= scheduled_ship["arrival"] or arrival >= scheduled_ship["departure"]):
            return False
    return True

def assign_bay(ship):
    for bay in docking_bays:
        if bay["size"] == ship["size"] and check_time_conflict(bay, ship["arrival"], ship["departure"]):
            bay["schedule"].append({"name":ship["name"], "arrival": ship["arrival"], "depature": ship["depature"]})
            return f"{ship['name']} assigned to Bay {bay['id']}"
    return f"No availible bay for {ship['name']}"

def optimize_schedule():
    spaceships.sort(key=lambda x: x["arrival"])
    for ship in spaceships:
        print(assign_bay(ship))

def print_schedule():
    for bay in docking_bays:
        print(f"Bay {bay['id']} Schedule:")
        for ship in bay["schedule"]:
            print(f" - {ship['name']}: {ship['arrival']} to {ship['departure']}")