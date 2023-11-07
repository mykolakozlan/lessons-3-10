# 1. Створити папку ./alphabet/ Якщо тека існує, то ОК.
# 2. У папці ./alphabet/ створити файли виду a.txt, b.txt, ..., z.txt
# у яких буде записано рядок алфавіту, але із заміною літери з назви файлу на прописну.
# Приклад: для b.txt рядок буде aBcde...

# 3. Зробити функцію, яка видаляє випадкову половину всіх файлів у цій папці.

# makedir, makedirs(exist_ok), remove
import os
# import string
from string import ascii_lowercase
import random


def create_dir(name):
    os.makedirs(name, exist_ok=True)


def create_file(sym, some_dir, ascii_lower):
    text = ascii_lower.replace(sym, sym.swapcase())
    full_path = os.path.join(some_dir, sym + ".txt")

    # with open(f"{some_dir}/{sym}.txt", 'w') as f:
    with open(full_path, 'w') as f:
        f.write(text)


# ascii_lower = ascii_lowercase

def create_files(some_dir, ascii_lower):
    for symb in ascii_lower:
        create_file(symb, some_dir, ascii_lower)


def remove_half_of_file(dir_name):
    files_list = os.listdir(dir_name)
    random.shuffle(files_list)

    # file_to_delete = files_list[:len(files_list) // 2]
    file_to_delete = files_list[::2]
    for to_del in file_to_delete:
        os.remove(os.path.join(dir_name, to_del))


dir_name = "alphabet"

# create_dir(dir_name)
# create_files(dir_name, ascii_lowercase)
# remove_half_of_file(dir_name)
