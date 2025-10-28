from graphics.rectangle import area as rect_area,perimeter as rect_perimeter
from graphics.circle import area as circle_area,perimeter as circle_perimeter
from graphics._3D_graphics.cuboid import surface_area as cuboid_surafce_area,volume as cuboid_volume
from graphics._3D_graphics.sphere import surface_area as sphere_surface_area,volume as sphere_volume
print("Enter The Length and Breadth of The Rectangle:")
l=int(input("Length:"))
b=int(input("Breadth:"))
print("Rectangle Area:",rect_area(l,b))
print("Rectangle Perimeter:",rect_perimeter(l,b))
print("\n\n")

print("Enter The Radius Of The Circle:")
radius=int(input("Radius:"))
print("Circle Area:",circle_area(radius))
print("Circle Perimeter:",circle_perimeter(radius))
print("\n\n")

print("Enter The Dimensions Of The Cuboid:")
length=float(input("Length:"))
width=float(input("Width:"))
height=float(input("Height:"))
print("Cuboid Surface Area:",cuboid_surafce_area(length,width,height))
print("Cuboid Volume:",cuboid_volume(length,width,height))
print("\n\n")

print("Enter The Radius Of The Sphere:")
radius=float(input("Radius:"))
print("Sphere Surface Area:",sphere_surface_area(radius))
print("Sphere Volume:",sphere_volume(radius))

