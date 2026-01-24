### Questions:###

# Q.1: LOOPS concept:
# Print natural number upto n
# for i in range(1,n): srf n likhogi tw desire number se km hi aega q k woh last se pehle +1 kr k ruk jata hai

# n = int(input("Please put your lucky number here"))
# for i in range(1,n+1):
#  print(i)

# ___________________

# Q.2: LOOPS concept:
# Resverse for loop . print n to 1
# reverse loop m shuru main n and hmesha -1 use krenge end m, or jaha tk ulta le jana hai whaa se pehle wala number likhenge

# n = int(input("Please put your lucky number here"))

# for i in range(n,0,-1):
#  print(i)

# ___________________

# Q.3: LOOPS concept:
# Take a number as input and print its table

# Basic Concept:

# n = int(input("Which numbers table you want?"))
# for i in range(n,(n*10)+1,n):
#     print(i)

# Good level concept:

# n = int(input("Which numbers table you want?"))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

# ___________________

# Q.4: LOOPS concept:
# Sum upto n terms

# a = 1
# a = a + 2
# a = a + 3
# a = a + 4

# print (a) #10

# n = int(input("Enter the number for sum"))
# sum = 0

# for i in range (1,n+1):
#     sum = sum + i

# print(sum)

# ___________________

# Q.5: LOOPS concept:
# Factorial of a number

# n = int(input("Please tell your number"))

# fact = 1 #0 is liye nhi rkhenge wrna sb 0 hojaega

# for i in range(1,n+1):
#     fact = fact * i

# print(fact)
# ___________________


# Q.6: LOOPS Advance concept:
# prime numbers woh hote h jo apne ables m aate h baki composite number - factors woh hote h jo dyusrou k tables m bhi aate hai, jese  12 ab woh 1,2,3,4,6,12 in sb k tables m ataa hai. 
# logic m reminder 0 hoga tw factor warna prime
# Print all the factors of a number.

# n = int(input("Please give your number"))

# for i in range (1,n+1):
#     if n%i == 0:
#      print(i, end = " ") #iss end = " " ek line m ajaege next pr shift nhi houge
# ___________________

# Q.7: LOOPS Advance concept:
# Accept number and check it if perfect or not
# A number whose sum of factors(excluding number itself) = Number Ex - 6 = 1, 2 , 3 = 6
# sare factors jo nikle hai, apna number chrh k un sb ko sum krna hai

# n = int(input("Tell your number"))

# sum = 0
# for i in range (1,n):
#     if n%i == 0:
#        sum = sum + i

# print(sum)

# if we tell my number is strong number like perfect jis ka sum bhi original number ho us k liu=ye ye krenge.

# if sum == n:
#     print ("This is a perfect number")
# else:
#     print("This is not a perfect number")

# ___________________

# Q.8: LOOPS Advance concept:
# Check if the number is prime or not

# n = int(input("Tell your number"))

# count = 0
# for i in range (1,n+1):
#     if n%i == 0:
#         count = count + 1
# if count == 2:
#     print("This is prime number")
# else:
#     print("This is composite number")

# ___________________

# Q.9: LOOPS Advance concept:
# Separate each digit of a number and print it on the new line Ex - 123
# Mode division % apne last digit ko separate krdeta hai, flow division// apne last digit ko gyb krdeta hai

# a = 123
# print(a%10)
# a = a//10
# print(a%10)
# a = a//10
# print(a%10)
# a = a//10
# print(a%10)

# Condition k jaha pr zero ajega waha ruk jan hai tw hm while use krenge

# a = int(input("Tell your number"))

# while a > 0:
#     print(a%10)
#     a = a//10

# ___________________

# Q.10: LOOPS Advance concept:
# Accept number and check if it is a pallindromic number
# (if number and its reverse are equal)
# Ex - 12321 - Reverse - 12321

# n = int(input("Tell your number")) #123
# rev = 0
# while n > 0:
#     z = n%10
#     rev = rev*10 + z
#     n = n//10

# print (rev)

# abhi kahani khtmnhi hoi hai ye srf reverse arha hai, hme donou ko same bhi check krna hai.

# n = int(input("Tell your number")) #123
# copy = n
# rev = 0
# while n > 0:
#     z = n%10
#     rev = rev*10 + z
#     n = n//10

# if copy == rev:
#     print("PALLINDROMIC NUMBER")
# else:
#     print("Not PALLINDROMIC NUMBER")

# ___________________

# Q.11: LOOPS Advance concept:
# (Strong Number)
# Ek number Strong Number tab hota hai jab uske har ek digit ka factorial nikaal kar unhe jama (add) kiya jaye, aur answer wahi original number aaye.

a = int(input("Tell your number"))

temp = a

while a > 0:
    digit = a % 10

    