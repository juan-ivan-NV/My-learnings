def street_fighter_selection(fighters, initial_position, moves):
    direct = {
        'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    result = []
    x, y = initial_position
    for move in moves:
        move_x, move_y = direct[move]
        x = min(max(move_x + x, 0), (len(fighters) - 1))
        y = (y + move_y) % (len(fighters[0]))
        result.append(fighters[x][y])
    return result