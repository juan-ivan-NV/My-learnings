def calc_fuel(n):
    values = {"lava": 800, "blaze rod": 120, "coal": 80, "wood": 15, "stick": 1 }
    time = n*11
    items = {"lava": 0, "blaze rod": 0, "coal": 0, "wood": 0, "stick": 0}
    for x,y in values.items():
        i = 0
        while time >= y:
            i += 1
            time -= y  
            items[x] = i
    return items