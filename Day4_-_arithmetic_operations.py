# 1. Write a program that declares two integer variables and perform basic arithmetic operations (addition, subtraction, multiplication, division) on them. Print the results to the console.
# 2. Write a program that calculates the area of a rectangle. Prompt the user to input the length(integer) and width(integer) of the rectangle, calculate the area (length * width), and print the result.
# 3. Modify the above program to read decimal numbers as the length and width, and output the area to two decimal points


#Program1
grade1 = 9
grade2 = 8

print('The sum of the grades is:',grade1 + grade2)
print('The subtraction of the grades is:',grade1 - grade2)
print('The multiplication of the grades is:',grade1 * grade2)
print('The division of the grades is:',grade1 / grade2)

#Program2
length = int(input('Enter the length: '))
width = int(input('Enter the width: '))

area = length * width

print(f'The area of the rectangle is: {area:.2f}')

