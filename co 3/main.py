from graphics import circle,rectngle
from graphics.threedgrapics.cuboid import *
from graphics.threedgrapics import sphere as s

r = int(input("Enter the radius:"))
print("Area of the given circle=", circle.area(r))
print("Perimeter of the given circle=", circle.perimeter(r))
print("____________________________________________________")

l = int(input("\nEnter length of the rectngle:"))
b = int(input("Enter the breadth of the rectngle:"))
print("Area of the given rectngle=", rectngle.area(l, b))
print("Perimeter of the given rectngle=", rectngle.perimeter(l, b))
print("____________________________________________________")

l = int(input("\nEnter length of the cuboid:"))
b=int(input("Enter breadth of the cuboid:"))
h=int(input("Enter height of the cuboid:"))
print("Area of the given cuboid=", area(l, b, h))
print("Perimeter of the given cuboid=", perimeter(l, b, h))
print("____________________________________________________")

r = int(input("\nEnter the radius of the sphere:"))
print("Area of the given sphere=", s.area(r))
print("Perimeter of the given circle=", s.perimeter(r))
print("____________________________________________________")