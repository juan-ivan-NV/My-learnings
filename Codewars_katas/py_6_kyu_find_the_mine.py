def mineLocation(field):
    loc = [ [x,y] for x in range(len(field)) for y in range(len(field[x])) if field[x][y] == 1 ]
    return loc[0]