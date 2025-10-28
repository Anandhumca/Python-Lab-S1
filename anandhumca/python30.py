calculate_square_area=lambda side_length:side_length**2
calculate_rectangle_area=lambda length,width:length*width
calculate_triangle_area=lambda base,height:0.5*base*height
 
sqs=int(input("Enter The Side Of The Square:"))
print("Enter The Base and Height Of The Triangle")
ht=int(input("Height:"))
bs=int(input("Base:"))

print("Enter The Length and Breadth Of The Rectangle")
l=int(input("Length:"))
b=int(input("Breadth:"))

square_area=calculate_square_area(sqs)
print("Area Of The Square:",square_area)

triangle_area=calculate_triangle_area(bs,ht)
print("Area Of The Triangle:",triangle_area)

rectangle_area=calculate_rectangle_area(l,b)
print("Area Of The Rectangle:",rectangle_area)
