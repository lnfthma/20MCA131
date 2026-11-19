__all__ = ["area", "perimeter"]

def area(length, breadth, height):
    # surface area of the cuboid
    return 2 * (length * breadth + breadth * height + height * length)

def perimeter(length, breadth, height):
    # total length of all 12 edges
    return 4 * (length + breadth + height)
