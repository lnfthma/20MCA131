# 1. import the whole module
import graphics.rectangle
print("Rectangle area      :", graphics.rectangle.area(5, 3))
print("Rectangle perimeter :", graphics.rectangle.perimeter(5, 3))

# 2. selective import of a module from the package
from graphics import circle
print("Circle area         :", circle.area(4))
print("Circle perimeter    :", circle.perimeter(4))

# 3. selective import of functions (with alias) from the sub-package
from graphics.graphics3d.cuboid import area as cuboid_area, perimeter as cuboid_perimeter
print("Cuboid surface area :", cuboid_area(4, 3, 2))
print("Cuboid perimeter    :", cuboid_perimeter(4, 3, 2))

# 4. import a module from the sub-package
from graphics.graphics3d import sphere
print("Sphere surface area :", sphere.area(3))
print("Sphere perimeter    :", sphere.perimeter(3))

# 5. import * (imports area() and perimeter() of rectangle)
from graphics.rectangle import *
print("Rectangle (import *):", area(10, 4), perimeter(10, 4))
