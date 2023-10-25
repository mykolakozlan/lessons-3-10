# practice
# list comprehension
# sets
# sets methods(union(), difference(), intersection())

################# list comprehension

# value_str = [1, 2, 3, 4]

# some_list = []
# for i in value_str:
#     if not (i**2) % 2:
#         some_list.append(i**2)

# some_list = [i for i in value_str]
# some_list = [i**2 for i in value_str]
# some_list = [i**2 for i in value_str if not (i**2) % 2]

# print(some_list)

################ sets

# value_list = [1, 2, 2, 3, 24, 34, 9]
# value_list = ["1", "2", "2", "3", "4", "4", "9"]

# print(value_list)
# value_set = set(value_list)
# print(value_set)

# sets methods(union(), difference(), intersection())

# Command + Option + L (mac)/ Ctrl + Alt + L (Win)

# value_set_1 = {1, 2, 3, 4, 5, 30}
# value_set_2 = {10, 2, 30}

# print(value_set_1)

# value_set_1 = value_set_1.union(value_set_2) # "+"
# new_set_1 = value_set_1.difference(value_set_2)
# print(new_set_1)
#
# new_set = value_set_2.difference(value_set_1)
# print(new_set)
# #
# new_set_2 = new_set_1.union(new_set) # "-" ПОРЯДОК ЗАПИСУ ВАЖЛИВИЙ
# print(new_set_2)

# # value_set_1 = value_set_1.intersection(value_set_2) # перехрещення/порівняння (те що є в обидвох сетах)
#
#
# print(value_set_1)


# a = {1, 3, 4, 5, 6, 7}
# b = {6, 56, 42, 1, 3}
# a_1 = a.union(b)
# a2 = a.difference(b)
# b5 = a_1.union(a2)
#
# print(a_1)
# print(a2)
# print(b5)
