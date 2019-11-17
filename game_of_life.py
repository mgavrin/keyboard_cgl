### Conway's Game of Life, to be displayed in the lights on a fancy keyboard. ###

### Note: the keyboard is treated as a grid despite not being exactly aligned on one. Cells that do not correspond to any real key are inserted outside the 

# If kWrapAround is true, the bottom of the grid wraps around to the top,
# and the right to the left, as if the keyboard was a torus.
kWrapAround = False
kKeyboardWidth = 21
kKeyboardHeight = 6
keyboard = [[False]*kKeyboardWidth]*kKeyboardHeight

key_map = {'esc': (0,0), 'f1': (0,1), 'f2': (0,2), 'f3': (0,3), 'f4': (0,4),
           'f5': (0,5), 'f6': (0,6), 'f7': (0,7), 'f8': (0,8), 'f9': (0,9),
           'f10': (0,10), 'f11': (0,11), 'f12': (0,12), 'printscreen': (0,13),
           'scrolllock': (0,14), 'pause': (0,15)}
#fill the rest in later; skip numbers for e.g. the nonexistent key underneath delete

def update_cell(x,y):
    ''' Calculates the value of a cell from the values of its neighbors.
    x: the row of the cell to be updated.
    y: the column of the cell to be updated.
    '''
    neighbors = set((x-1, y-1), (x-1, y), (x-1, y+1),
                    (x, y-1), (x, y+1),
                    (x+1, y-1), (x+1, y), (x+1, y+1))
    if !kWrapAround:
        neighbors = exclude_out_of_bounds_neighbors(neighbors)

def exclude_out_of_bounds_neighbors(neighbors):
    if x == 0:
        pass
    if y == 0:
        excluded = set((x-1, y-1))
    if x == kKeyboardWidth-1:
        excluded = set((x+1, y-1), (x+1, y), (x+1, y+1))
    if y == kKeyboardHeight-1:
        excluded = set((x-1, y+1), (x, y+1), (x+1, y+1))
