# This file contains the CUI this app uses
from objs import Rectangle, Square, Canvas

print('Hey! Let\'s create an image together!')
print('For this enter canvas\' width and height.')

width = int(input('Width: '))
height = int(input('Height: '))

print('All right! Now enter what color you want your canvas to be (black or white).')
canvas_color = input('> ')

canvas = Canvas(width, height, canvas_color)

print('Great! Now let\'s create some objects on it!')

while True:
    print('Type \'rectangle\' to add a rectangle and \'square\' to add a square (or smth else to quit).')
    figure = input('> ')

    # Get out of the loop if input isn't 'square' or 'rectangle'
    if figure != 'square' and figure != 'rectangle':
        break
    
    if figure == 'square':
        x = int(input('Enter square\'s x: '))
        y = int(input('Enter square\'s y: '))
        side = int(input('Enter square\'s side length: '))
        red = input('Enter Red value 0-255: ')
        green = input('Enter Green value 0-255: ')
        blue = input('Enter Blue value 0-255: ')
        square = Square(x, y, side, red, green, blue)
        # Here should be a line which adds a newly created square to the canvas
        continue
    
    if figure == 'rectangle':
        x = int(input('Enter rectangle\'s x: '))
        y = int(input('Enter rectangle\'s y: '))
        width = int(input('Enter rectangle\'s width: '))
        length = int(input('Enter rectangle\'s height: '))
        red = input('Enter Red value 0-255: ')
        green = input('Enter Green value 0-255: ')
        blue = input('Enter Blue value 0-255: ')
        rect = Rectangle(x, y, width, height, red, green, blue)
        # Here should be a line which adds a newly created rectangle to the canvas
        continue

# Generate a png file from Canvas instance
