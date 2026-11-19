import math

__all__ = ["area", "perimeter"]

def area(radius):
    return round(math.pi * radius ** 2, 2)

def perimeter(radius):
    return round(2 * math.pi * radius, 2)
