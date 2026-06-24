# Open this link and click Run to execute the program in the CIP IDE.
# https://codeinplace.stanford.edu/cip6/share/j0APqaisXEFgqKmYXIda

from karel.stanfordkarel import *

"""
Program: Beeper Spreader
Karel starts facing a stack of beepers, picks them up one by one, 
and spreads them out along the row until the stack is empty.
"""

def main():
    move()
    spread()
    step_back()
    
def spread():
    """
    Main logic to distribute the beepers.
    Loops through the stack, takes one, moves it to the current end 
    of the line, and goes back to repeat the process.
    """
    while beepers_present():
        pick_beeper()
        if beepers_present():
            move_to_end()
            put_beeper()
            reset()
    put_beeper()

def move_to_end():
    """
    Walks forward across the already placed beepers 
    to find the next empty spot in the row.
    """
    while beepers_present():
        move()

def reset():
    """
    Turns around and walks all the way back to the starting wall, 
    then resets orientation to face east again.
    """
    turn_around()
    move_to_wall()
    turn_around()
    move()

def move_to_wall():
    while front_is_clear():
        move()

def turn_around():
    turn_left()
    turn_left()
    
def step_back():
    """
    Moves Karel one step backward to finish the execution 
    in the correct final position.
    """
    turn_around()
    move()
    turn_around()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
