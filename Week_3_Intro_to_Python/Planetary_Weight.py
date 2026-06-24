
# Code in Place IDE demo:
# Open this link and click Run to execute the program in the CIP IDE.
# https://codeinplace.stanford.edu/cip6/share/zk7g2eVRZiYN8rMiDrtt

"""
Program: Planetary Weight

This program asks for a weight on Earth and a planet name.
Then it prints the equivalent weight on the selected planet.

The planet name should be typed with the first letter uppercase.
For this exercise, the program assumes the user enters one of the valid planet names.

Concepts practiced:
- Constants
- User input
- Type conversion
- If / elif / else statements
- Arithmetic operations
- Rounding
- F-strings
"""


MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
EARTH_GRAVITY = 1.0


def main():
    # Ask for the user's weight on Earth as the starting value
    earth_weight = float(input("Enter a weight on Earth: "))

    # Ask which planet the user wants to compare with
    planet = input("Enter a planet: ")

    # Choose the correct gravity multiplier based on the planet name
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    else:
        # In this exercise, the remaining valid option is Neptune
        gravity_constant = NEPTUNE_GRAVITY

    # Multiply the Earth weight by the selected planet's gravity value
    planetary_weight = earth_weight * gravity_constant
    rounded_planetary_weight = round(planetary_weight, 2)

    # Print the result in a clear sentence
    print(f"The equivalent weight on {planet}: {rounded_planetary_weight}")


if __name__ == "__main__":
    main()
