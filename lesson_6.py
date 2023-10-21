# розминка з подвійним for loop

# my_string = '0123456789'


# my_string = 0
# while my_string < 100:
#     print(my_string+1)
#     my_string += 1

# for symbol1 in my_string:
#     for symbol2 in my_string:
#         num = int(symbol1 + symbol2)
#         print(num)

# tens_digit = 0
# while tens_digit < 10:
#     ones_digit = 0 # -> 1
#     while ones_digit < 10:
#
#
#         num_str = string[tens_digit] + string[ones_digit] # 0 + 0 -> 0 + 1
#         num_int = int(num_str) #00 -> 0, 01 -> 1
#         print(num_int)
#         ones_digit += 1
#     tens_digit += 1

# for tens_digit in my_string:
#     for ones_digit in my_string:
#         number_str = tens_digit + ones_digit
#         number_int = int(number_str)
#         print(number_int)

# for i in range(10):

#     for j in range(10):

#         num_str = my_string[i] + my_string[j]
#         num_int = int(num_str)
#         print(num_int)

#############
#
# my_string = '0123456789'
#
# for symbol1 in my_string:
#     for symbol2 in my_string:
#         num = int(symbol1 + symbol2)
#         print(num)
#
# #############
#
# my_string = '0123456789'
#
# for x in my_string:
#     for y in my_string:
#         print(int(x+y))
#
# #############
# my_string_1 = "0123456789"
# my_string_2 = "0123456789"
#
# for symb_int_1 in my_string_1:
#     for symb_int_2 in my_string_2:
#          print(symb_int_1 + symb_int_2)

# my_string = '0123456789'

# for i in range(100):
#
#     number_str = ''
#     if i > 9:
#         number_str += my_string[i // 10]
#     number_str += my_string[i % 10]
#     number = int(number_str)
#     print(number)

# for two_digit_number in range(100):
#     print(two_digit_number)

    # tens = two_digit_number // 10
    # ones = two_digit_number % 10
    # print(tens, ones)


# порівняння list та tuple
# змінні не змінні типи даних різниця
# методи строк(split(), rsplit(), join())
# методи list(append(), pop(), sort(), copy())
# функція sorted()


# list() - списки, масиви
# tuple() - кортеж

# value_list = ["Hello", 1, 1.5, True,]  #змінний
# value_tuple = ("Hello",) #незмінний
# # function(), math()
# print(type(value_list))
# print(type(value_tuple))

# ############################################

# base_list = [1, 2, 3]
#
# my_new_list = base_list * 4
#
# print(my_new_list)
#
# base_list[0] = 10
# print(f"base_list {base_list}")
#
# print(f"my_new_list {my_new_list}")
#
# # ######################################

value_1 = "Hello"
value_2 = value_1[:]


base_list = [1, 2, 3, [1, 4, 5]]
# base_list_2 = base_list.copy()

new_list = [base_list.copy()] * 4

# [link, link, link, link]
print(new_list)

base_list[0] = 10
# new_list[0]
print(f"base_list {base_list}")
print(f"new_list {new_list}")

# # # ######################################

# value_list = [
#     "Hello",
#     1,
#     1.5,
#     True,
#     False,
# ]  #змінний
# value_tuple = (
#     "Hello",
# ) #незмінний
# print(len(value_tuple))
# # function(), math()
# print(type(value_list))
# print(type(value_tuple))

#
# base_list = [1, 2, 3]
# # print(base_list)
# base_list.append("Hello")
# # print(base_list.append("Hello"))
# # print(base_list)
#
# deleted_val = base_list.pop()
# # print(base_list)
# print(deleted_val)
#
# websites = [
#     "www.site1.com",
#     "www.site2.com",
#     "www.site3.com",
#     "www.site4.com",
#     "www.site5.com",
#     "www.site6.com",
# ]
#
# print(websites)
#
# while websites:
#
#     deleted_val = websites.pop()
#     print(deleted_val)


# len(websites)
#
#
# while not len(websites):
# while not True:
# while False:

# while len(websites) != 0:
# while len(websites):
# while websites:

# print(websites)


# value = "Hello"
# print(value)
# value = value.lower()
# print(value)


# методи строк(split(), rsplit(), join())

# # value = "Hello world"
# value = "desktop/d.oc/file/img.jpg"
#
# val_list = value.split('/')
# # val_list[1] = 'png'
# print(val_list)
# final_str = "\\".join(val_list)
# print(final_str)

###########sort

# base_list = [1, -4, 9, 10, 2, 3]
# base_list = ["amd", "aamd", "aaamd", "bmd", "ppp", "0", "]", "@"]

# print(base_list)
# base_list.sort()
# sorted(base_list)

# print(sorted(base_list, reverse=False, key=abs))
# print(base_list)
# sorted()

######## ASCII - мыжнародний стандарт розмітки
# print(ord("A"), ord("["), ord("a"), ord("m"), ord("@"))
#
# print(chr(65))
#




