# 3 stages of programming

# if statement not
# ternary operator
# while (True, flag, value)
# break, continue
# while else
# str methods

# value = "ffff"

# if (value == "+") or (value == "-"):
#     print("!!!!!")
# else:
#     print("????")

# not

# if not value: # value is not True
#     print("ssss")

# value = 10

# if (value % 2) == 0 and (value % 5) == 0:
#     print(value)
#
# if not (value % 2) and not (value % 5):
# if not (value % 2 == 0 and value % 5 == 0):
#     print(value)

#
# if not (value % 2 and value % 5):
# if not (value % 2 and value % 5):
#     print(value)

# print("end")

# logged = True
#
# if not logged:
#     print("Please logged in")
# else:
#     print("Welcome")

############# ternary operator ############

# a = 2
# b = 330
#
# # print("A") if a > b else print("B")
#
# result = True if a > b else False
#
# print(result)

############# while (True, flag, value) ############
# value = 1
# is_true = True


# while True:
#     value += 1 # value = value + 1
#     print(value)
#     if value > 10:
#         break


# while value < 10:
#     value += 1  # value = value + 1
#     if value % 2:
#         continue
#
#     print(value)


# while is_true:
#     value += 1  # value = value + 1
#     print(value)
#
#     if value > 10:
#         is_true = False

############### break, continue
# condition_1 = True
# condition_2 = False
# condition_3 = False
#
# while condition_1:
#     print("1111")


############# while else ############

# value = 1
#
# while value < 10:
#     value += 1  # value = value + 1
#     if value % 2:
#         continue
#
#     # print(value)
# else:
#     print(value)
# #
# print("end")

############# str methods ############
#
# value_str = "quesrty"
# index = 4
#
# # value_str[2:2:2] - [початок, кінець, крок]
#
# # print(value_str[20]) #адреса (номер символу)
# # print(value_str[1:10]) # з - включно, до - виключно
# # print(value_str[19:]) # з - включно, до кінця
#
# # print(value_str[::-1])
# # print(value_str[::2])
# # print(value_str[0::2]) #чотні
# # print(value_str[1::2]) #нечотні
# # print(value_str[::-2])
#
# document = "file.exe"
# # document = "file.py"
# # "1000293.jpg" "nikolas_1.jpg"
#
# dot = document.find('.') #знаходить індекс підстроки
# print(dot)
# # extension = document[(dot+1):]
# # # print(extension)
# # # name = document[0:4]
# # name = document[:dot]
# # print(name)
#
# # name = document [0:4]
# # [:(dot-1)]
#
# doc_length = len(document)
#
# extension = document[(doc_length - dot + 1):]
# name = document[:(doc_length - dot)]
# print(name)

# str_1 = "hello"
# str_2 = "Hello"
# print(str_2.lower())
# print(str_2.upper())
# if str_1.lower() == str_2.lower():
#     print("ok")


# Email@email.com
# email@email.com

# first_name = input("name: ")
#
# print(first_name.capitalize())