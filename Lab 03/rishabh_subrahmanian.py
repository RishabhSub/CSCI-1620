import math


# Calculating the area of a circle
def area_circle(radius: float) -> float:
    if type(radius) != int and type(radius) != float:
        raise TypeError('Type error')
    if radius <= 0:
        raise ValueError('Negative/Zero area')
    area = math.pi * math.pow(radius, 2)
    return area


# Calculating the area of a rectangle
def area_rectangle(length: float, width: float) -> float:
    if type(length) != int and type(length) != float:
        raise TypeError('Type error')
    if length <= 0:
        raise ValueError('Negative/Zero area')
    if type(width) != int and type(width) != float:
        raise TypeError('Type error')
    if width <= 0:
        raise ValueError('Negative/Zero area')
    area = length * width
    return area


# Calculating the area of a square
def area_square(length: float) -> float:
    if type(length) != int and type(length) != float:
        raise TypeError('Type error')
    if length <= 0:
        raise ValueError('Negative/Zero area')
    area = math.pow(length, 2)
    return area


# Calculating the area of a triangle
def area_triangle(base: float, height: float) -> float:
    if type(base) != int and type(base) != float:
        raise TypeError('Type error')
    if base <= 0:
        raise ValueError('Negative/Zero area')
    if type(height) != int and type(height) != float:
        raise TypeError('Type error')
    if height <= 0:
        raise ValueError('Negative/Zero area')
    area = base * height * 0.5
    return area

# Ask how to display numbers to 2 decimal places every time