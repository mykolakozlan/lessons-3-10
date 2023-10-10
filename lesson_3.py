# Bool, None types
# Logic operators
# Зведення типів
# Duck typing
# If statement (programming golf, Тернарний оператор)
# input()
# working with errors

######### NoneType #########

# value_none = None
#
# value_int = 123

# print(value_int)

# value_id = id(value_int)
# value_print = print(value_int)

# print(value_print, type(value_print))
# print(value_id, type(value_id))

######### Bool #########

# value_bool_1 = True
# value_bool_2 = False
#
# result_num = 11 > 2 # >, <, ==, !=, >=, <=
# result_str = "He" in "hello!" # ==, !=, <, >, <=, >=, in
#
# print(result_str)

######### Type #########

# value_int = 11
# value_str = "12"
#
# # f"{} {}"
# # str(value_int) + value_str
# result = value_int + float(value_str)
# print(result)

# value_int = 1
# value_float = 0.01
# value_str = "hello"
#
# # print(bool(value_str)*2)
#
# # value_bool = bool(value_str) # bool
# # value_int = value_bool * 2 # int
#
# print(bool(value_str)*2, type(bool(value_str)*2))


######## If statement #########

# if умова:
#     зроби це

# value_int = 2

# # #
# # and or not
# #
# # # if value_int > 0 and value_int < 10:
# if value_int is not True:
#     print(f"{value_int} is bigger then 0")
# elif value_int > 10:# else if
#     print(f"{value_int} is bigger then 10")
# else:
#     print(f"{value_int} is less then 0")

# print("end")

# golf, ternary operator, not

# value_str = ''
#
# print(bool(value_str)*2, type(bool(value_str)*2))




######### input() ###### ALWAYS STRING
# result = 0
# try:
#     value_1 = int(input("Please type a number(only number): "))
#     result = 1 / value_1
# # except ValueError:
# #     print("It should be a number")
# # except ZeroDivisionError:
# #     print("You can't divide to 0")
# except (ZeroDivisionError, ValueError):
#     print("Sorry, the system is busy right now. Try again later")
#
# print(result)

# value_2 = int(input("Please type another number: "))
#
# result = value_1 + value_2
#
# print(result)

########## Homework ###########


# if value_1 is int:
#     value_1 = int(value_1)
# else:
#     value_1 = 0

value_int_1 = input("Please type a number: ")
value_int_2 = input("Please type another number: ")
value_operator = input("Please choose an operator: \n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/' \nYour answer: ")

if value_operator == "1":
    result = value_int_1 + value_int_2

print(result)
