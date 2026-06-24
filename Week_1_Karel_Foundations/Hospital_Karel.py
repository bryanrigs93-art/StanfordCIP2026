# Code in Place IDE demo:
# Open this link and click Run to execute the program in the CIP IDE.
# https://codeinplace.stanford.edu/cip6/share/j0APqaisXEFgqKmYXIda

"""
Program: Hospital Karel
This program makes Karel walk all the way across 1st Street from west to east,
looking for a beeper to build a hospital on that spot.
"""
from karel.stanfordkarel import *

def main():
    while front_is_clear():
        if beepers_present():
            build_hospital()
        safe_move()


def build_hospital():
    """
    Main function to build the complete hospital (both columns).
    It picks up the starting beeper, builds the first column, moves one space,
    and then builds the second column.
    """
    # Pick up the supply beeper before starting construction
    pick_beeper()
    do_one_column()
    move()
    do_one_column()


def do_one_column():
    """
    Handles building a single column for the hospital.
    Turns north, places three beepers, goes back down to the ground,
    and faces east again to keep moving forward.
    """
    turn_left()
    put_three_beepers()
    return_to_base()
    turn_left()


def put_three_beepers():
    """
    Places three beepers in a vertical row.
    It drops a beeper and moves up one step until all three are placed.
    """
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()


def return_to_base():
    """
    Makes Karel turn around and walk straight down until hitting the floor.
    Ends up facing south right at the bottom of the column.
    """
    turn_around()
    move_to_wall()


def move_to_wall():
    while front_is_clear():
        move()


def safe_move():
    if front_is_clear():
        move()


def turn_around():
    turn_left()
    turn_left()


# Note: This function isn't called above, but it's here as a reference just in case.
def turn_right():
    for i in range(3):
        turn_left()

    

if __name__ == '__main__':
    main()
