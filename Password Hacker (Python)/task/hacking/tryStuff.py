import string
import os

import re

def my_generator():
    i = 0
    while True:
        yield i
        i = i + 1


def sumDigits(integer: int):
    result = 0
    while integer != 0:
        result += integer % 10
        integer = int(integer / 10)
    return result


print(sumDigits(309))


def letters(word):
    for letter in word:
        yield letter


def myProduct(list1: list, list2: list) -> list:
    return list([i * j for i, j in zip(list1, list2)])


def myProduct2(list_1, list_2):
    return list(map(lambda i, j: i * j, list_1, list_2))


list1 = [1, 2, 3]
list2 = [4, 5, 6]


def choose_vowels(letters):
    vowels = ['a', 'e', 'i', 'u', 'o']
    return list(filter(lambda x: x in vowels, letters))


liste = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e']

main_courses = ['beef stew', 'fried fish']
price_main_courses = [28, 23]

desserts = ['ice-cream', 'cake']
price_desserts = [2, 4]

drinks = ['cola', 'wine']
price_drinks = [3, 10]

# main_courses = zip(main_courses, price_main_courses)
# desserts = zip(desserts, price_desserts)
# drinks = zip(drinks, price_drinks)

import itertools


meals = [" ".join(i) for i in itertools.product(main_courses, desserts, drinks)]

prices = itertools.product(price_main_courses, price_desserts, price_drinks)

totals = [i + j + k for i, j, k in prices]

totalMeal = zip(meals, totals)

# for i in totalMeal:
#     if i[1] <= 30:
#         print(i[0], str(i[1]))
#
# for i in itertools.product(string.ascii_lowercase, repeat=3):
#     print(i)

alphabet = string.ascii_lowercase
numbers = "".join([str(i) for i in range(10)])
letters = alphabet + numbers

passwords = ("".join(i) for i in itertools.product(letters, repeat=1))

expression = "abc456"

print(re.findall("(\d+|\D+)", expression))

# expression.split()
#
# for i in [''.join(x) for x in itertools.product(*zip(expression.upper(), expression.lower()))]:
#     # print(i)
#     pass
#
# for i in zip(expression.upper(), expression.lower()):
#     print(i)

# print(os.getcwd())
# file = open("passwords.txt")
#
# line = file.readline()
#
# for line in file:
#     print(line)
