# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print(num , "is even")
# else:
#     print(num , "is odd")


# num1 = int(input("Enter a number: "))

# if num1 == 0:
#     print("Number is zero")
# elif num1 > 0:
#     print("Number is positive")
# else:
#     print("Number is negative")
    


# num2 = int(input("Enter a number: "))
# num3 = int(input("Enter a number: "))

# print(num2 if num2 > num3 else num3)




# num4 = int(input("Enter a number: "))
# num5 = int(input("Enter a number: "))
# num6 = int(input("Enter a number: "))

# if num4 >= num5 and num4 >= num6:
#     print(num4)
# elif num5 >= num4 and num5 >= num6:
#     print(num5)
# else:
#     print(num6)


# num7 = int(input("Enter a number: "))
# num8 = int(input("Enter a number: "))
# operator = input("Enter an operator (+, -, *, /): ")

# if operator == "+":
#     result = num7 + num8
# elif operator == "-":
#     result = num7 - num8
# elif operator == "*":
#     result = num7 * num8
# elif operator == "/":
#     result = num7 / num8
# elif operator == "//":
#     result = num7 // num8
# elif operator == "%":
#     result = num7 % num8
# elif operator == "**":
#     result = num7 ** num8
# else:
#     print("Invalid operator")

# print(f"{num7} {operator} {num8} = {result}")






# num9 = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f"{num9} x {i} = {num9 * i}")




# number = int(input("Enter a number: "))

# sum = 0
# for i in range(1, number + 1):
#     sum += i

# print("The sum of the first", number, "natural numbers is:", sum)




# numbers = [10, 15, 22, 31, 40, 51, 60]

# count = 0

# for i in numbers:
#     if i % 2 == 0:
#         count += 1

# print("The number of even numbers in the list is:", count)



# text = "Hello World"

# print(text[::-1])




text2 = input("Enter a text: ")

for i in text2:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        print(i.upper())
