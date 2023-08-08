def roll_call_dwarves(dwarves):
    for index, dwarf in enumerate(dwarves, start=1):
        print(f"{index}. {dwarf}")


def summon_captain_planet(vegetables):
    return [f"{vegetable.capitalize()}!" for vegetable in vegetables]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True

    return False


def find_the_cheese(foods):
    if "cheddar" in foods:
        return "cheddar"

    return None
