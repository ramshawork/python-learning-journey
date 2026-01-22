### Questions:###

# Q.1: If else concept:
# Accept two numbers and print the greates between them

num_a = int(input("Write your first number"))
num_b = int(input("Write your second number"))

if num_a > num_b:
    print(f"{num_a} is greater than {num_b}")
elif num_b > num_a:
    print(f"{num_b} is greater than {num_a}")
else:
    print("Both values are same")

# ___________________

# Q.2: If else concept:
# Accept the gender from the user as char ( F or M) and print the repective greeting message
# Ex- Good morning Sir (on the basis of genders)

gender = input("Provide me your gender as F or M")

if gender == "M" or gender == "m":
    print("Hello, Good Morning Sir")
elif gender == "F" or gender == "f":
    print("Hello, Good Morning Mam")
else:
    print("Wrong Input")

# ___________________

# Q.3 If else concept:
# Accept an integer and check wheather it is in even number or odd

a = int(input("Provide me any integar let's guess is it odd or even"))

if a % 2 == 0:
    print("This is even number")
elif a % 2 == 1:
    print("This number is odd")
else:
    print("Use integer please!")

# ___________________

# Q.4 If else concept:
# Accept name and age from the user for Valid vote

name = input("Write your name here")
age = int(input("Now tell me your age"))

if age >= 18:
    print(f"hello {name} you are a valid voter")
elif age < 18 and age > 0:
    print(f"hello {name} you are not a valid voter")
else:
    print("giva a valid age please!")

# ___________________

# Q.5 If else concept:
# Accept an year and check if a leap year or not

year = int(input("Plaese tell me your year to check"))

if year % 4 == 0 and year % 100 != 0:
    print("this is a leap year")
elif year % 400 == 0 and year % 100 == 0:
    print("this is a century leap year")
else:
    print("This is not a leap year")

# ___________________

# Q.6 If else concept:
# Accept an english alphabet from user and check if it is a constant or a vowel
# use string case for easy method: using IN instead fo == bht mba hojaega agr agr sb ko krenge

z = input("Give any character to check")

if z in "a,e,i,o,u,A,E,I,O,U":
    print("This is a vowel")
else:
    print("This is a consonent")

# ___________________
