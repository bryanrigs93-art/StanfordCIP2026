# Code in Place IDE demo:
# Open this link and click Run to execute the program in the CIP IDE.
# https://codeinplace.stanford.edu/cip6/share/7a1nHq3myBuqEpMFbcno
"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

# Gravity constant ratio for the conversion
MARS_MULTIPLE = 0.378

def main():
    earth_weight_str = input('Enter a weight on Earth: ')

    # Convert the string input to a float for math operations
    earth_weight = float(earth_weight_str)

    # Calculate the conversion and round to two decimal places
    mars_weight = earth_weight * MARS_MULTIPLE
    rounded_mars_weight = round(mars_weight, 2)

    # Display the final calculated result using an f-string
    print(f'The equivalent weight on Mars: {rounded_mars_weight}')

if __name__ == '__main__':
    main()
