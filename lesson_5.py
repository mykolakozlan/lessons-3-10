# homework review
# debuger
# for (range, enumerate)
# str methods(isalpha, rfind, replace, startwith)

##### Homework sample ###########

# result = None
# first_number = None
# second_number = None
# operator = None
#
# print("Welcome to calculator.")
#
# try:
#     first_number = float(input("Enter first number: "))
# except ValueError:
#     print("ValueError 1")
#
# try:
#     second_number = float(input("Enter second number: "))
# except ValueError:
#     print("ValueError 2")
#
# action = input("Please choose an operation. \n1 - '+'\n2 - '-'\n3 - '*'\n4 - '/': ")
#
# if action not in "1234" or len(action) != 1:
# # if action not in ["1", "2", "3", "4"]:
# # if action not in ("1", "2", "3", "4"):
#     print("Incorrect choice of operation")
#
# if action == '1':
#     result = first_number + second_number
#     operator = "+"
# elif action == '2':
#     result = first_number - second_number
#     operator = "-"
# elif action == '3':
#     result = first_number * second_number
#     operator = "*"
# elif action == '4':
#     if second_number == 0:
#         print("ZeroDivisionError")
#     result = first_number / second_number
#     operator = "/"
#
# print(f"{first_number} {operator} {second_number} = {result}")

######### for (range, enumerate) ############

# value_str = "Hello"
# index = 0

# while index < len(value_str):
#     print(value_str[index])
#     index += 1

# ["H", "e", "l"]
#
# for letter in value_str:
#     print(letter)
#     print(value_str.index(letter))


# range(10) # видача від 0 до 10 (0-9)
# range(5, 10) # видача від 5 до 10(виключно) (5-9)
# range(5, 10, 2) # видача від 5 до 10(виключно) (5-9)

# value_str = "Hello"

# for index in range():
#     print(index)

# for index in range(len(value_str)):
#     print(index)

# for index in range(len(value_str)):
#     print(index, value_str[index])


# enumerate

# for index, letter in enumerate(value_str):
#     print(index, letter)

# for value in enumerate(value_str):
#     print(value[0], value[1])

# for i in range(10):
#     print(i)

# value_str = "hello.jpg"
# # value_str.startswith("h")
# # value_str.endswith(".jpeg")
# print(value_str)
#
# value_str = value_str.replace("hello", "test")
# print(value_str)
# for letter in value_str:
#     if letter.isalpha():
#         print(letter)


value_str = "HeEllo.jpg"
for letter in value_str:
    if letter.lower() in "eyuioa" and letter.isalpha() and not letter.isspace():
        print(letter)
