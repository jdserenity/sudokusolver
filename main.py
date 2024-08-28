import config, utils

# TODO: 
# - reimplement "Unique candidate" technique
# - implement "Block and column / Row Interaction" technique (only 2 potentials and in the same column or row in the same box)
# - continue implementing candidate reducing techniques
# - add error handling codebase wide

grid_state = []


def set_initial_grid_state(puzzle):
    """
    Initializes the grid state from the raw puzzle data.

    Transforms the raw puzzle input into a structured array of objects, each representing a grid entry with 
    associated useful data. The grid state is stored globally and used throughout the solving process.
    """
    global grid_state

    for i, entry in enumerate(puzzle):
        grid_state.append({
            'entry': entry,
            'index': i,
            'column': (column := i % 9),
            'row': (row := i // 9),
            'box': (row // 3) * 3 + (column // 3),
            'solved': (solved := entry != '.'),
            'candidates': [] if solved else [str(i) for i in range(1, 10)]
        })


def iterative_solve():
    """ 
    My approach is to create algorithms that model known deductive reasoning techniques, and then iterate through them one by one until I have chipped away at the amount of 'candidates' or possible numbers for each tile until there is only 1. If there is only 1 possible candidate for a tile, then that tile is solved. Using this strategy, I will solve any sudoku puzzle that is used as input.
    """
    
    global grid_state; is_solved = False; iterations = 0

    while iterations < 10000 or not is_solved:
        basic_candidate_removal()
        
        unique_candidate_technique()
        block_and_column_or_row_interaction_technique()
        
        update_solved_entries()
        
        is_solved = utils.is_puzzle_solved(grid_state)
        iterations += 1


def basic_candidate_removal():
    """
    This function updates the candidate numbers for unsolved entries in the grid.
    
    For each unsolved entry, it checks all other entries in the same row, column, or box.
    If a neighboring entry is solved and its number is present in the current entry's list of candidates, 
    that number is removed from the candidate list for the current entry. This process helps narrow down 
    the possible numbers that can be placed in each unsolved entry based on the Sudoku rules.
    """
    global grid_state

    for current_entry in grid_state:
        if not current_entry['solved']:
            for area in ['box', 'column', 'row']:
                for comparison_entry in grid_state:
                    if comparison_entry['solved'] and comparison_entry['entry'] in current_entry['candidates']:
                        if comparison_entry[area] == current_entry[area]:
                            current_entry['candidates'].remove(comparison_entry['entry'])

def unique_candidate_technique():
    global grid_state

    # Unique Candidate: If any of the the current box, column, or row have a tile with a candidate that is unique (meaning no other tile in that area has it as a candidate), it means that this unique number is the solved number for that tile.


def block_and_column_or_row_interaction_technique():
    global grid_state

    # Block and column / Row Interaction: If in this box there are are only two places a number could possibly appear, AND those two numbers are in the same row or in the same column, that means that that number should be removed from the list of potentials in any tile in the same row or column respectively. (if they are same row, remove from rows, vice versa)


def update_solved_entries():
    """
    Updates the status of grid entries that have been solved.

    If an entry has only one candidate left, this function sets that candidate as the final entry value.
    It then marks the entry as solved by clearing the candidates list and updating the solved status.
    """
    global grid_state
    
    for current_entry in grid_state:
        if len(current_entry['candidates']) == 1:
            current_entry['entry'] = current_entry['candidates'][0]
            current_entry['candidates'] = []
            current_entry['solved'] = True
    

# def showcase_swordfish_placement():
#     global grid_state
#     for entry in grid_state:
#         if entry['index'] in [10, 15, 33, 35, 46, 48, 66, 71]:
#             print(entry['entry'])


def main():
    # Get a puzzle from the database
    with open(config.puzzles_database) as data:
        puzzles = data.readlines()
        puzzle_raw = puzzles[1].strip()

    # Print the unsolved puzzle
    utils.print_puzzle(puzzle_raw, format='raw')
    
    # Populate the grid state array with the puzzle data
    set_initial_grid_state(puzzle_raw)

    # Solve the puzzle
    iterative_solve()
    
    # Print the solved puzzle
    utils.print_puzzle(grid_state, format='grid_state')


if __name__ == '__main__':
    main()
