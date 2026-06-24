"""
Program: Random Circles

This program creates a graphics canvas and draws several circles in random
positions with random colors.

Concepts practiced:
- Graphics Canvas
- Constants
- For loops
- Random numbers
- Helper functions
- Coordinates
- Drawing ovals
"""

# Code in Place IDE demo:
# Open this link and click Run to execute the program in the CIP IDE.
# https://codeinplace.stanford.edu/cip6/share/AkJdcgjzxiRG7TxwjXm6

from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20


def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Draw several circles by repeating the same helper function
    for i in range(N_CIRCLES):
        draw_random_circle(canvas)


def draw_random_circle(canvas):
    # Pick a random position that still keeps the circle inside the canvas
    left_x = random.randint(0, CANVAS_WIDTH - CIRCLE_SIZE)
    top_y = random.randint(0, CANVAS_HEIGHT - CIRCLE_SIZE)

    right_x = left_x + CIRCLE_SIZE
    bottom_y = top_y + CIRCLE_SIZE

    color = random_color()

    canvas.create_oval(left_x, top_y, right_x, bottom_y, color)


def random_color():
    """
    Returns one random color from a small list of color options.
    This keeps the drawing different each time the program runs.
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)


if __name__ == '__main__':
    main()
