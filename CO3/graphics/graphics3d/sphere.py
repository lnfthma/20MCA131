import math

__all__ = ["area", "perimeter"]

def area(radius):
    # surface area of the sphere
    return round(4 * math.pi * radius ** 2, 2)

def perimeter(radius):
    # circumference of the great circle
    return round(2 * math.pi * radius, 2)
