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




# text2 = input("Enter a text: ")

# for i in text2:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#         print(i.upper())



# ------------------------------------*------------------------------------*------------------------------------



# INTERMEDIATE EXERCISES



# ------------------------------------*------------------------------------*------------------------------------




# numbers2 = [1, 4, 7, 10, 13, 16, 19, 22, 25]

# new_list = [num for num in numbers2 if num % 2 == 0]
# print(new_list)





# ------------------------------------*------------------------------------*------------------------------------





# numbers4 = [1, 2, 3, 4, 5, 6, 7]

# new_list2 = [i ** 2 for i in numbers4 if i % 2 != 0]
# print(new_list2)




# ------------------------------------*------------------------------------*------------------------------------





# numbers5 = [1, 2, 2, 3, 4, 4, 5, 5, 5]

# new_list3 = set(numbers5)
# print(list(new_list3))






# ------------------------------------*------------------------------------*------------------------------------



# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}

# c = a.union(b)
# d = a.intersection(b)
# e = a.difference(b)
# e2 = b.difference(a)
# f = a.symmetric_difference(b)

# print(c)
# print(d)
# print(e)
# print(e2)
# print(f)





# ------------------------------------*------------------------------------*------------------------------------






# def average_marks(marks):
    
#     total = sum(marks)
#     average = (total / len(marks))
#     grade = ""
#     if average >= 90:
#         grade = "A"
#     elif average >= 80:
#         grade = "B"
#     elif average >= 70:
#         grade = "C"
#     elif average >= 60:
#         grade = "D"
#     elif average >= 50:
#         grade = "E"
#     elif average < 50:
#         grade = "F"
#     return average, grade

# marks = [78, 85, 92, 66, 88]

# print(average_marks(marks))





# ------------------------------------*------------------------------------*------------------------------------





# numbers5 = [10, 5, 25, 8, 17]

# def find_largest(numbers):
    
#     big_one = 0
#     for i in numbers:
#         if i > big_one:
#             big_one = i
#     return big_one

# print(find_largest(numbers5))





# ------------------------------------*------------------------------------*------------------------------------





# def palindrome_checker(word):
    
#     reversed = word[::-1]

#     return reversed == word 

# word = input("Enter your word: ")
# print(palindrome_checker(word))




# ------------------------------------*------------------------------------*------------------------------------






# numbers6 = [10, 5, 25, 8, 17]

# def statistics(nums):

#     even_count = 0
#     odd_count = 0
#     minimum = min(nums)
#     maximum = max(nums)    
#     total = sum(nums)
#     average = total / len(nums)
#     for i in nums:
#         if i % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1
#     return f"Minimum: {minimum} - Maximum: {maximum} - Sum: {total} - Average: {average} - Odd Count: {odd_count} - Even Count: {even_count}" 


# print(statistics(numbers6))               





# ------------------------------------*------------------------------------*------------------------------------





# words = ["Python", "JavaScript", "SQL", "React"]

# new_words = { i : len(i) for i in words}

# print(new_words)




# ------------------------------------*------------------------------------*------------------------------------



# ADVANCE EXERCISES



# ------------------------------------*------------------------------------*------------------------------------





# numbers = [10, 5, 20, 8, 20, 15]

# new_numbers = set(numbers)

# largest_num = 0
# sec_larg_num = 0

# for i in new_numbers:
#     if i > largest_num:
#         sec_larg_num = largest_num
#         largest_num = i
#     elif i > sec_larg_num and i < largest_num:
#         sec_larg_num = i    


# print(sec_larg_num, largest_num)        





# ------------------------------------*------------------------------------*------------------------------------





# word1 = input("Enter first word: ")
# word2 = input("Enter second word: ")

# dict1 = {x: word1.lower().count(x) for x in word1.lower().strip()}
# dict2 = {x: word2.lower().count(x) for x in word2.lower().strip()}


# def anagrams_checker(word1, word2):
#     if word1 == word2:
#         return "Anagram Approved"
#     else:
#         return "Not an Anagram"


# print(anagrams_checker(dict1, dict2))







# ------------------------------------*------------------------------------*------------------------------------





# text1 = "proggramming"

# dict2 =  {x: text1.count(x) for x in text1}

# largest_frequency = {"alph":[],"count":0}

# for i,j in dict2.items():

#     if largest_frequency["alph"] == []:
        
#         largest_frequency["alph"] = [i]
#         largest_frequency["count"] = j
        
#     elif largest_frequency["count"] == j:
        
#         largest_frequency["alph"].append(i)
#         largest_frequency[f"count-{i}"] = j

#     elif largest_frequency["count"] < j:

#         largest_frequency["alph"] = [i]
#         largest_frequency["count"] = j
        
#     print(i,j)


# print(largest_frequency)





# ------------------------------------*------------------------------------*------------------------------------






# text = "python is easy and python is powerful"   

# list1 = text.split(" ")

# dict4 = {x: list1.count(x) for x in list1}

# print(dict4)





# ------------------------------------*------------------------------------*------------------------------------





# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def divider():

#     dict_num = {"even":[], "odd": []}


#     for i in numbers:
#         if i % 2 == 0:
#             dict_num["even"].append(i)
#         else:
#             dict_num["odd"].append(i)

#     return dict_num        

# print(divider())






# ------------------------------------*------------------------------------*------------------------------------






# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# arr = []

# for i in matrix:
#     for j in i:
#         arr.append(j)

# print(arr)





# ------------------------------------*------------------------------------*------------------------------------



# ?????????????????????????????????????????????????????????????????????????????????????


# 27


# ------------------------------------*------------------------------------*------------------------------------






# numbers = [4, 2, 4, 1, 2, 5, 1]

# dict1 = {x: numbers.count(x) for x in numbers}

# list1 = [x for x in dict1.keys()]

# print(list1)






# ------------------------------------*------------------------------------*------------------------------------





# numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]

# dict1 = {x: numbers.count(x) for x in numbers if numbers.count(x) > 1}

# list1 = [x for x in dict1.keys()]

# print(list1)





# ------------------------------------*------------------------------------*------------------------------------





cart = [
    {"name": "Laptop", "price": 1000, "quantity": 1},
    {"name": "Mouse", "price": 50, "quantity": 2},
    {"name": "Keyboard", "price": 100, "quantity": 1}
]

def calculator():

    sum = 0
    price = 0

    for i in cart:
        for j, k in i.items():
            if j == "price":
                price = k
            elif j == "quantity":
                sum += price * k

    return sum                


print(calculator())


