import random
from gui import *

def assign_nations(nations, names):
    output_dict = {}
    for name in names:
        selected_nation = random.choice(nations)
        nations.remove(selected_nation)
        output_dict[name] = selected_nation
    return output_dict

def limit_nations(player_count):
    if player_count == 7:
        return ["Austria", "England", "France", "Germany", "Italy", "Russia", "Turkey"]
    if player_count == 6:
        return ["Austria", "England", "France", "Germany", "Russia", "Turkey"]
    if player_count == 5:
        return ["Austria", "England", "France", "Russia", "Turkey"]
    if player_count == 4:
        return ["England", "France", "Russia", "Turkey"]
    if player_count == 3:
        return ["France", "Germany", "Austria"]
    if player_count == 2:
        return ["France", "Austria"]

def get_player_names(player_count):
    names = []
    for player_number in range(1, player_count + 1):
        names.append(get_player_name(player_number))
    random.shuffle(names)
    return names

def main():
    while True:
        player_count = get_player_count()
        names = get_player_names(player_count)
        assigned_nations = assign_nations(limit_nations(player_count), names)
        show_results(assigned_nations)
        break

if __name__ == "__main__":
    main()