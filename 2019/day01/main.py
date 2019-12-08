from math import floor
tanks = 0

with open("input", 'r') as f:
    for mass_str in f.readlines():
        mass = float(mass_str)
        tanks = tanks + int(floor(mass / 3e0)) - 2
print("Part 1:", tanks)

tanks = 0
with open("input", 'r') as f:
    for mass_str in f.readlines():
        mass = float(mass_str)
        required_fuel = mass
        total_fuel = 0
        while required_fuel > 0:
            required_fuel = int(floor( required_fuel / 3e0 )) - 2
            if required_fuel <= 0:
                continue
            total_fuel = total_fuel + required_fuel
            pass
        tanks = tanks + total_fuel
        pass
    pass
print("Part 2:", tanks)
