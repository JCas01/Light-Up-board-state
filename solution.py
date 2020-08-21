def get_type(i, j, board):
    tile = board[i][j]
    if tile is ".":  # we check for tiles
        return "tile"
    if tile is "X":  # we check for blocks
        return "wall"
    if tile is "L":  # we check for lights
        return "light"
    if tile is "0":
        return "wall"
    if tile is "1":
        return "wall"
    if tile is "2":
        return "wall"
    if tile is "3":
        return "wall"
    if tile is "4":
        return "wall"


def scan_light(i, j, board):
    size = len(board)
    # North
    index = i
    while index > 0:
        index += -1
        tile = get_type(index, j, board)
        if tile is "light":  # when lamp, return true
            return True
        elif tile is "wall":  # when block, stop searching on path
            break
    # East
    index = j
    while index < size-1:
        index += 1
        tile = get_type(i, index, board)
        if tile is "light":  # when lamp, return true
            return True
        elif tile is "wall":  # when block, stop searching on path
            break
    # South
    index = i
    while index < size-1:
        index += 1
        tile = get_type(index, j, board)
        if tile is "light":  # when lamp, return true
            return True
        elif tile is "wall":  # when block, stop searching on path
            break
    # West
    index = j
    while index > 0:
        index += -1
        tile = get_type(i, index, board)
        if tile is "light":  # when lamp, return true
            return True
        elif tile is "wall":  # when block, stop searching on path
            break
    return False  # no lamp, so we ain't lit up, "happy" is the best we can hope for


def scan_wall(i,j,board,number):
    size = len(board)
    count = 0
    #Key: 0 unhappy, 1 happy, 2 solved
    #North
    if i > 0:
        if get_type(i-1,j,board) == "light":
            count += 1
    #East
    if j < size-1:
        if get_type(i,j+1,board) == "light":
            count += 1
    #South
    if i < size-1:
        if get_type(i+1,j,board) == "light":
            count += 1
    #west
    if j > 0:
        if get_type(i,j-1,board) == "light":
            count += 1
    if count < number:
        return 1
    elif count > number:
        return 0
    elif count == number:
        return 2

def scan_board(i, j, tileType, board):
    if tileType is "tile":
        return scan_light(i, j, board)
    elif tileType is "light":
        return scan_light(i,j,board) #if it has a light we unhappy
    elif tileType is "wall":
        number = board[i][j]
        if number == "X":
            return 2
        else:
            return scan_wall(i,j,board,int(number))


def get_board_state(board):
    size = len(board)
    solved = True
    current_tile_solved = True

    for i in range(0, size):  # we checking rows
        for j in range(0, size):  # we checking collums
            tile = board[i][j]  # we checking every single tile
            number = None
            tile = get_type(i, j, board)
            if tile is "tile":
                current_tile_solved = scan_board(i, j, "tile", board)
            if tile is "light":
                if scan_board(i,j,"light",board):
                    return "unhappy"
            if tile is "wall":
                num = scan_board(i,j,"wall",board)
                if num == 0:
                    return "unhappy"
                elif num == 1:
                    current_tile_solved = False
                elif num == 2:
                    current_tile_solved = True

            if not current_tile_solved:
                solved = current_tile_solved
    if solved:
        return "solved"
    else:
        return "happy"


if __name__ == '__main__':
  # Example board, happy state.
  print(get_board_state('''
...1.0.
X......
..X.X..
X...L.X
..X.3..
.L....X
L3L2...'''.strip().split('\n')))
  # Example board, solved state.
  print(get_board_state('''
..L1.0.
X...L..
L.X.X.L
X...L.X
..XL3L.
.L....X
L3L2L..'''.strip().split('\n')))
  # Example board, unhappy state.
  print(get_board_state('''
L..1L0.
X.L....
L.X.X.L
X...L.X
..XL3L.
.L....X
L3L2L..'''.strip().split('\n')))
  # Different board, happy state.
  print(get_board_state('''
L1.L.
..L3L
..X1.
.1...
.....'''.strip().split('\n')))
