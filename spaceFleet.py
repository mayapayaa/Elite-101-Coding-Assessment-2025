# docking bay schedule (bay size and availability)
docking_bays = {
    "Bay 1": {"size": "small", "schedule": []},
    "Bay 2": {"size": "medium", "schedule": []},
    "Bay 3": {"size": "large", "schedule": []},
}

# incoming spaceships with size and docking time
spaceships = [
    {"name": "Shuttle Alpha", "size": "small", "arrival": 12, "departure": 14},
    {"name": "Freighter Beta", "size": "large", "arrival": 15, "departure": 18},
    {"name": "Cruiser Gamma", "size": "medium", "arrival": 13, "departure": 16},
]

def find_available_bays(ship):
    """Finds bays that match the ship's size."""
    available_bays = []
    for bay, details in docking_bays.items():
        if details["size"] == ship["size"]:
            available_bays.append(bay)
    return available_bays

def check_time_conflict(bay, arrival, departure):
    """Checks if the bay is available for the given time window."""
    for schedule in docking_bays[bay]["schedule"]:
        if not (departure <= schedule["arrival"] or arrival >= schedule["departure"]):
            return False  # Conflict found
    return True

def assign_docking_bay(ship):
    """Assigns a docking bay based on size and availability."""
    for bay in find_available_bays(ship):
        if check_time_conflict(bay, ship["arrival"], ship["departure"]):
            docking_bays[bay]["schedule"].append(ship)
            return f"{ship['name']} assigned to {bay} from {ship['arrival']}:00 to {ship['departure']}:00"
    return f"No available bay for {ship['name']}"

def schedule_ships():
    """Schedules all ships in the list."""
    results = []
    for ship in spaceships:
        results.append(assign_docking_bay(ship))
    return results

def print_schedule():
    """Prints the docking schedule in a readable format."""
    for bay, details in docking_bays.items():
        print(f"{bay}:")
        if not details["schedule"]:
            print("  No scheduled dockings.")
        else:
            for ship in details["schedule"]:
                print(f"  {ship['name']} - {ship['arrival']}:00 to {ship['departure']}:00")
        print()

# Run the scheduling and print results
schedule_results = schedule_ships()
for result in schedule_results:
    print(result)

print("\nFinal Docking Schedule:")
print_schedule()