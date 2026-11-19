import math
import random

print("Square root of 49 :", math.sqrt(49))
print("Value of pi       :", round(math.pi, 4))
print("Factorial of 5    :", math.factorial(5))
print("2 raised to 5     :", math.pow(2, 5))
print("Ceil of 4.2       :", math.ceil(4.2))
print("Floor of 4.8      :", math.floor(4.8))

colors = ["red", "green", "blue", "yellow"]
print("Random integer (1-10):", random.randint(1, 10))
print("Random float (0-1)   :", round(random.random(), 3))
print("Random colour        :", random.choice(colors))
random.shuffle(colors)
print("Shuffled list        :", colors)
