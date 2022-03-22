# This file contains all the objects which will be used in the app
import numpy as np
from PIL import Image

class Rectangle:

    def __init__(self, x, y, width, height, red, green, blue):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.red = red
        self.green = green
        self.blue = blue


class Square:

    def __init__(self, x, y, side, red, green, blue):
        self.x = x
        self.y = y
        self.side = side
        self.red = red
        self.green = green
        self.blue = blue


class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
    
    def generate(self, rects, sqrs):
        data = np.zeros((self.width, self.height, 3), dtype=np.uint8)

        if self.color == 'white':
            data[:] = [255, 255, 255]

        # Add rectangles on the image if the list isn't empty
        if len(rects) > 0:
            for rect in rects:
                data[rect.x : rect.x + rect.width, rect.y : rect.y + rect.height] = [rect.red, rect.green, rect.blue]

        # Add squares on the image if the list isn't empty
        if len(sqrs) > 0:
            for sqr in sqrs:
                data[sqr.x : sqr.x + sqr.side, sqr.x : sqr.y + sqr.side] = [sqr.red, sqr.green, sqr.blue]
        
        img = Image.fromarray(data, 'RGB')
        name = 'canvas.png'
        img.save(name)
        print(f'{name} was succesfully generated.')
