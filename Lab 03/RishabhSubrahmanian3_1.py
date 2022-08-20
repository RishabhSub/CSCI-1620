# Part 1
# Import the necessary module (use an alias name during importation to help with code readability)
import rishabh_subrahmanian as rishsub


def selection():
    print('----------------------')
    print('SELECT SHAPE')
    print('----------------------')
    print('1 - Circle')
    print('2 - Rectangle')
    print('3 - Square')
    print('4 - Triangle')

    # Code to check that a valid shape has been selected
    shape = int(input('Shape number: '))
    while shape < 1 or shape > 4:
        shape = int(input('Shape number (1-4): '))

    return shape


def main():
    while True:
        # Delete this statement and use the comments below to fill out the missing code

        # Part 2
        # Determine which shape the user selected by calling the selection() function
        # Determine which area should be computed based off the value returned by the selection() function
        shape = selection()
        if shape == 1:
            radius = float(input('Circle radius: '))
            print(f'Circle area = {rishsub.area_circle(radius):.2f}')

        elif shape == 2:
            length = float(input('Rectangle length: '))
            width = float(input('Rectangle width: '))
            print(f'Rectangle area = {rishsub.area_rectangle(length, width):.2f}')

        elif shape == 3:
            length = float(input('Square length: '))
            print(f'Square area = {rishsub.area_square(length):.2f}')

        else:
            base = float(input('Triangle base: '))
            height = float(input('Triangle height: '))
            print(f'Triangle area = {rishsub.area_triangle(base, height):.2f}')

        # Part 3
        # Ask the user if they want to continue
        # If they enter 'n', break out of the loop and display 'PROGRAM DONE'
        # If they enter 'y' the loop should be repeated (go back to the top of the loop)
        # Use a loop to check that they are entering a valid response (y/n)
        yes_no = input('Continue (y/n): ').lower().strip()
        while yes_no not in ['y', 'n']:
            yes_no = str(input('Enter \'y\' or \'n\': '))

        if yes_no == 'n':
            print('PROGRAM DONE')
            break


if __name__ == '__main__':
    main()
