
# data types

# Numbers

# int - integer ціле число
# float - 1.666666666661
# complex - (2+3j)
# decimal - 2.6666666666606

# string cтрока
# str


# Bolean bool(True/False)

# tuple - кортежи ()

# list - cписок []
# set - множина {}
# dict - словник {key: value}

# None

# id() функція яка показує адресу файлу
# type() функція яка тип файлу

box = "hello"
# print(id(box))
new_box = box

box = "hellо!"
# print(id(box))

# print(new_box, type(new_box), id(new_box))

# constants

PI = 3.14
MONTHS_IN_YEAR = 12

################################################################################

num_1 = 9
num_2 = 2

result_add = num_1 + num_2
result_sub = num_1 - num_2
result_mul = num_1 * num_2
result_div = num_1 / num_2
result_div_2 = num_1 // num_2 # цілочислене ділення
result_div_3 = num_1 % num_2 # залишок ділення
result_power = num_1 ** num_2 # зведення в ступінь
result_root = num_1 ** 0.5 # корінь

# print(result_root, type(result_root))


################################################################################

# string

# some_text = 'Hello \nI\'m\tNick'
# some_text = r"c\doc\new_fole.doc" #raw string сира строка
# some_text = 'Football club "Liverpool" '
# some_text = """Hello"""
# some_text = '''Hello'''


name = "Nick"
age = 24.7
# \n нова строка
# \t табуляція
# \ ігнорувати символ

# print(type(age))
# str_age = str(age)
# # some_text = f"Hello I\'m {name}" #format string
# some_text = name + ' ' + str_age #format string

# print(type(age))

# int(age)
# float(age)

print(str(age))