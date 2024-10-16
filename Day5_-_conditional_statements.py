# 1. Write a program that reads an integer as user input and prints whether the number is Odd or Even to the console
# 2. Write a program that takes three numbers as input and prints the largest among them
# 3. Write a program that checks if a given input year is a leap year or not
# 4. Write a program that reads the percentage and then prints their corresponding letter grade (A, B, C, D, or F)

#Program1
number = int(input("Type a number: "))
if number % 2 == 0:
    print(f'{number} is Even.')
else:
    print(f'{number} is Odd.')

#Program2
number1 = int(input("Type the first number: "))
number2 = int(input("Type the second number: "))
number3 = int(input("Type the third number: "))
print(f"The max of the numbers is {max(number1, number2, number3)}")

#Program3
year = int(input("Type a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
 print(f"{year} is not a leap year.")

#Program4
percentage_input = input("Type the percentage: ")
percentage = float(percentage_input.replace('%', ''))

if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"The letter grade is {grade}.")
