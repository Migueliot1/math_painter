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
