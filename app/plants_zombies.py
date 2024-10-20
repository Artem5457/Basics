def plants_zombies_battle(zombies: list[int], plants: list[int]) -> bool:
    plants_initial_power = sum(plants)
    zombies_initial_power = sum(zombies)

    plant_survivors = 0
    zombie_survivors = 0

    for i in range(max(len(plants), len(zombies))):
        plant_power = plants[i] if i < len(plants) else 0
        zombie_power = zombies[i] if i < len(zombies) else 0

        if plant_power > zombie_power:
            plant_survivors += 1
        elif zombie_power > plant_power:
            zombie_survivors += 1

    if plant_survivors > zombie_survivors:
        return True
    elif zombie_survivors > plant_survivors:
        return False
    else:
        if plants_initial_power > zombies_initial_power:
            return True
        elif zombies_initial_power > plants_initial_power:
            return False
        else:
            return True
