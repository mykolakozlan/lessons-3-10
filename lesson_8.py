# розпаковка tuple та list
# змінна "_"
# поняття dict
# основні методи dict(update(), get(), pop(), keys(), values(), items())


# value_1 = 1
# value_2 = 2
#
# value_1, value_2 = value_2, value_1


# value_list = (1, 2, 3, 4, 6, 7, 8)

# value_1, value_2, value_3 = value_list[:3]

# value_1, value_2, value_3, _ = value_list

# request_list = ["", "", ""]

# if len(request_list) > 3:
#     value_1, value_2, value_3, *tmp = request_list
# else:
#     value_1, value_2, value_3 = request_list

# value_1, value_2, value_3, *tmp = value_list

# print(_)
# print(value_1, value_2, value_3, tmp)
# print(value_list)
# print(*value_list)

# for _ in range(10):
#     print("hello")

########### dict

# value_list = [1, 2, 3, 4, 5]
# value_list[2]

# value_dict = dict()

# hash table for dict
#
# value_dict = {
#     "key": "value",
#     "key1": "value",
#     "key2": "value",
#     1: 3,
#
#     # (1,2, [1,2]): 3,
#     (1, 2): 3,
#     1.2: 3,
#     True: 3,
#     None: 3,
# }
#
# address = {
#     "country": "Ukraine",
#     "city": "Kyiv",
# }
#
# person = {
#     "first_name": "Nick",
#     "last_name": "Kozlan",
#     "password": "111111",
#     "email": "email@gmail.com",
#     "address": address
# }
# person_2 = {
#     "first_name": "Nick",
#     "last_name": "Kozlan",
#     "password": "111111",
#     "email": "email@gmail.com",
#     "address": address
# }
#
# our_group = [person, person_2]

# value_str = "1234"
# for value in enumerate(value_str):
#     print(value)


# print(person["first_name"])
# print(person["address"]["city"])
# print(person)

# for key in person_2:
#     print(key, person_2[key])
#
# for key in person_2.items():
#     print(key[0], key[1])
#
# for key, value in person_2.items():
#     print(key, value)

# .items()
# print(person_2.values())

# person_3 = dict()
# person_3["first_name"] = "Bogdan"
# person_3["last_name"] = "Count"
# person_3["email"] = "Count@"
# # print(person_3)
# print(person_3.keys())

# if "email" not in person_3:
#     print("Email is a nessesary field")

# email_3 = person_3["email"]


# email_3 = person_3.get('email', False)


#
# from random import randint
#
# result = randint(1,6)
#
# dice_dict = {
#     1: "This is 1",
#     2: "This is 2",
#     3: "This is 3",
#     4: "This is 4",
#     5: "This is 5",
#     6: "This is 6",
# }
#
# print(dice_dict[result])


# ASCII   ord()

# print(ord("a"))
# print(chr(97))

# alphabet_dict = {}
#
# for key in range(ord("a"), ord("z")+1):
#     alphabet_dict[key] = chr(key)
#
# for key in alphabet_dict:
#     pass
#
# new_alphabet_dict = {}
# print(new_alphabet_dict)
#
# for key in alphabet_dict:
#     new_alphabet_dict[alphabet_dict[key]] = key
#
# for key, value in alphabet_dict.items():
#     new_alphabet_dict[value] = key
#
# print(new_alphabet_dict)

########### dict comprehension

# value_list = [i for i in range(10)]
# print(value_list)

# value_dict = {i: f"This is {i}" for i in range(1, 7)}
# value_dict = {i: i**2 for i in range(1, 7) if not i % 2}
# print(value_dict)

# update()

# val_dict_1 = {
#     1: "1111",
#     2: "22222",
# }

# val_dict_2 = {
#     2: "3333",
#     4: "44444",
# }
#
# val_dict_1.update(val_dict_2)

# print(a)
# print(val_dict_1)


# pop()

# val_dict_1 = {
#     "1": "1111",
#     2: "22222",
# }
# print(val_dict_1)
# a = val_dict_1.pop("1")
# print(a)
# print(val_dict_1)

# value_str = "Hello"
# value_str = [
#     "jjjjj",
#     2,
#     [1,1,1]
# ]
# # value = "H"
#
#
# for i in value_str:
#     # value_int = 0 #-> 1 -> 2
#     # value = "H" -> "e"
#     print(i)
