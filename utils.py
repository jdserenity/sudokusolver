# This function can be used just to simply print the puzzle in the command line, nicely formatted with grid lines, starting from the raw database format
def print_puzzle(puzzle, format=None):
    if format not in ['raw', 'grid_state']:
        return print("error. must pass in either format='raw' or format='grid_state' to print puzzle.\n")
    
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('------+-------+------')
        row = ''
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row += '| '
            row += (puzzle[i * 9 + j]['entry'] if format == 'grid_state' else puzzle[i * 9 + j]) + ' '
        print(row)
    print('\n')


def is_puzzle_solved(grid_state):
    for entry in grid_state:
        if entry['solved'] == False:
            return False
    return True
