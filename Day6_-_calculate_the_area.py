#Write a program that takes radius of the circle and outputs the area of the circle to 2 decimal digits

PI = 3.14
radius = float(input("Enter the radius of the circle: "))
area =  PI * (radius ** 2) 
print(f"The area of the circle is: {area:.2f}")
