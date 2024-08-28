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


def get_all_entries_from(area, index, grid_state):
    # Area should be either 'box', 'column', or 'row'
    # index should be an integer 0-8
    
    desired_entries = []

    for entry in grid_state:
        if entry[area] == index:
            desired_entries.append(entry)

    return desired_entries


def update_entry_to_solved(entry, solved_num=None):
    entry['entry'] = solved_num
    entry['candidates'] = []
    entry['solved'] = True


# def showcase_swordfish_placement():
#     global grid_state
#     for entry in grid_state:
#         if entry['index'] in [10, 15, 33, 35, 46, 48, 66, 71]:
#             print(entry['entry'])

def block_and_column_or_row_interaction_technique():
    global grid_state

    # Block and column / Row Interaction: If in this box there are are only two places a number could possibly appear, AND those two numbers are in the same row or in the same column, that means that that number should be removed from the list of potentials in any tile in the same row or column respectively. (if they are same row, remove from rows, vice versa)
    