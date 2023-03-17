# TODO Звездный прямоугольник 1
# Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами
# 14
# ×
# 10
# 14×10 в соответствии с образцом:

# **********
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# **********
# Примечание. Для вывода прямоугольника используйте цикл for.

def draw_box():
    width = 10
    height = 14
    print("*" * width)
    for _ in range(height - 2):
        print("*" + " " * (width - 2) + "*")
    print("*" * width)


draw_box()



def draw_box():
    print('*' * 10 + "\n" + ('*' + ' ' * 8 + '*' + "\n")*12 + '*' * 10)


draw_box()


def draw_box(number, symbol_1, symbol_2, digit):
    for _ in range(number):
        print(f"{symbol_2}{symbol_1 * digit}{symbol_2}")


draw_box(1, "*", "", 10)
draw_box(12, " ", "*", 8)
draw_box(1, "*", "", 10)


# TODO Звездный треугольник 1
# Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными
# 10
# 10 в соответствии с образцом:
#
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********
# Примечание. Для вывода треугольника используйте цикл for.

def draw_triangle():
    for symbol in range(1, 11):
        print("*" * symbol)


draw_triangle()



# TODO Звездный треугольник
# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:

# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника;
# а затем выводит его.
# Примечание. Гарантируется, что основание треугольника – нечетное число.


def draw_triangle(fill, base):
    for number in range(1, (base // 2) + 1):
        print(fill * number)
    for number in range((base // 2) + 1, 0, -1):
        print(fill * number)

fill = input()
base = int(input())
draw_triangle(fill, base)



# объявление функции
def draw_triangle(fill, base):
    for i in range(1, base + 1):
        print(fill * min(i, base - i + 1))

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)


# TODO ФИО
# Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
# name – имя человека;
# surname – фамилия человека;
# patronymic – отчество человека;
# а затем выводит на печать ФИО человека.

# Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.
def print_fio(name, surname, patronymic):
    fio = "".join((surname[0], name[0], patronymic[0])).upper()
    print(fio)


name, surname, patronymic = input(), input(), input()
print_fio(name, surname, patronymic)


# TODO Сумма цифр
# Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.
def print_digit_sum(num):
    nums = sum(map(int, str(num)))
    print(nums)


number = int(input())
print_digit_sum(number)



def print_digit_sum(num):
    nums = (int(digit) for digit in str(num))
    print(sum(nums))


number = int(input())
print_digit_sum(number)



# TODO Решение задач Задача 1. Напишите функцию, которая возвращает длину гипотенузы прямоугольного треугольника по известным значениям его катетов.

# Решение. Для нахождения длины гипотенузы, нам нужно применить теорему Пифагора: квадрат гипотенузы прямоугольного треугольника, равен сумме квадратов его катетов. Другими словами, если a,b – длины катетов, а c – длина гипотенузы, то имеет место равенство:
# c**2 = a**2 + b**2 ** 0.5
# Для извлечения квадратного корня мы использовали оператор возведения в степень. Напомним, что результатом обоих выражений: math.sqrt(c) и c ** 0.5 является одно число

def compute_hypotenuse(a, b):
    result = (a**2 + b**2) ** 0.5
    return result


print(compute_hypotenuse(3, 4))



# TODO Задача 2. Напишите функцию get_distance(x1, y1, x2, y2), вычисляющую расстояние между точками (x1; y1) и (x2; y2)
# Решение. Расстояние между двумя точками (x1; y1) и (x2; y2) определяется по формуле
# p = корень квадратный (x1 - x2)**2 + (y1 - y2)**2
# Несложно заметить, что искомое расстояние – это длина гипотенузы прямоугольного треугольника с катетами равными

# Функция, вычисляющая расстояние между точками, может иметь вид:

def get_distance(x1, y1, x2, y2):
    return compute_hypotenuse(x1 - x2, y1 - y2)

# Для подсчета искомого расстояния мы используем уже созданную нами функцию compute_hypotenuse передавая ей в качестве аргументов числа x1 - x2 и y1 - y2.

# Основная программа имеет вид:

x1, y1 = float(input()), float(input())  # считываем координаты первой точки
x2, y2 = float(input()), float(input())  # считываем координаты второй точки

print(get_distance(x1, y1, x2, y2))      # вычисляем и выводим расстояние между точками



# TODO Задача 3. Напишите функцию sum_digits(n), принимающую в качестве аргумента натуральное число и возвращающую сумму его цифр.
# Решение. Функция sum_digits(n) может иметь вид:

def sum_digits(n):
    result = 0
    while n > 0:
        result += n % 10
        n //= 10
    return result
# Основная программа имеет вид:

n = int(input())
print(sum_digits(n))      # вычисляем и выводим сумму цифр считанного числа


# TODO Задача 4. Напишите функцию compute_average(numbers), принимающую в качестве аргумента список чисел и возвращающую среднее значение элементов списка.

# Решение. Для подсчета среднего значения элементов списка нужно вычислить сумму всех элементов и их количество, то есть использовать функции sum() и len(). Функция compute_average(numbers) может иметь вид:

def compute_average(numbers):
    return sum(numbers) / len(numbers)
# Основная программа имеет вид:

numbers = [1, 3, 5, 1, 6, 8, 10, 2]
print(compute_average(numbers))      # вычисляем и выводим среднее значение элементов списка
# Результатом работы такой программы будет число 4.5, которое и является средним значением.


# TODO Конвертер километров
# Напишите функцию convert_
# to_miles(km), которая принимает в качестве аргумента расстояние в километрах и возвращает расстояние в милях. Формула для преобразования: мили = километры * 0.6214.
def convert_to_miles(km):
    return km * 0.6214


num = int(input())
print(convert_to_miles(num))



# TODO Количество дней
# Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце.
# Примечание 1. Гарантируется, что передаваемый аргумент находится в диапазоне от 1 до 12.
# Примечание 2. Считайте, что год является невисокосным.

def get_days(month):
    result = (28 if month == 2 else 30 if month in [4, 6, 9, 11] else 31)
    return result


num = int(input())
print(get_days(num))


def get_days(month):
    result = ["28" if month == 2 else "30" if month in (4, 6, 9, 11) else "31"]
    return "".join(result)


num = int(input())
print(get_days(num))


# TODO Делители 1
# Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую список всех делителей данного числа.
def get_factors(num):
    divisors = []
    for digit in range(1, num + 1):
        if num % digit == 0:
            divisors.append(digit)

    return divisors


number = int(input())
print(get_factors(number))



def get_factors(num):
    return [digit for digit in range(1, num + 1) if num % digit == 0]


number = int(input())
print(get_factors(number))


# TODO Делители 2
# Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую количество делителей данного числа.
# Примечание 1. Используйте уже реализованную функцию get_factors(num) из предыдущей задачи.
def get_factors(num):
    return [digit for digit in range(1, num + 1) if num % digit == 0]


def number_of_factors(num):
    return len(get_factors(num))


number = int(input())
print(number_of_factors(number))


# TODO Найти всех
# Напомним, что строковый метод find('a') возвращает местоположение первого вхождения символа a в строке. Проблема заключается в том, что данный метод не находит местоположение всех символов а.

# Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: строку target и символ symbol и возвращает список, содержащий все местоположения этого символа в строке.
# Примечание 1. Если указанный символ не встречается в строке, то следует вернуть пустой список.

def find_all(target, sym):
    return [index for index, elem in enumerate(target) if elem == sym]


text = input()
symbol = input()
print(find_all(text, symbol))


# TODO Merge lists 1
# Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два отсортированных по возрастанию списка, состоящих из целых чисел, и объединяет их в один отсортированный список.

# Примечание 1. Списки list1 и list2 могут иметь разную длину.
# Примечание 2. Можно использовать списочный метод sort(), а можно обойтись и без него 😎.

def merge(nums_1, nums_2):
    nums_1.extend(nums_2)
    nums_1.sort()
    return nums_1


numbers_1 = [int(num) for num in input().split()]
numbers_2 = [int(num) for num in input().split()]
print(merge(numbers_1, numbers_2))



# TODO Слияние двух отсортированных списков
# Слияние двух отсортированных списков в один — важная задача в информатике. Она естественно возникает при сортировке списков c использованием сортировки слиянием.
# Пусть даны два отсортированных по возрастанию списка чисел list1 и list2:

def quick_merge(list1, list2):
    result = []
    elem1 = list1[0]
    elem2 = list2[0]
    while elem1 < len(list1) and elem2 < len(list2):
        if list1[elem1] <= list2[elem2]:
            result.append(list1[elem1])
            elem1 += 1
        else:
            result.append(list2[elem2])
            elem2 += 1

    if elem1 < len(list1):   # прицепление остатка
        result += list1[elem1:]
    if elem2 < len(list2):
        result += list2[elem2:]

    return result


list_1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
list_2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
list3 = quick_merge(list_1, list_2)
print(list3)


def quick_merge(list1, list2):
    result = sorted(list1 + list2)
    return result


list_1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
list_2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
list3 = quick_merge(list_1, list_2)
print(list3)


# TODO Merge lists 2
# На вход программе подается число n, а затем n строк, содержащих целые числа в порядке возрастания. Из данных строк формируются списки чисел. Напишите программу, которая объединяет указанные списки в один отсортированный список с помощью функции quick_merge(), а затем выводит его.

# Формат входных данных
# На вход программе подается натуральное число n, а затем n строк, содержащих целые числа в порядке возрастания, разделенные символом пробела.
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

def quick_merge(nums_1, nums_2):
    result = sorted(nums_1 + nums_2)
    return result


total_nums = []
number = int(input())
for _ in range(number):
    text = input().split()
    numbers = [int(elem) for elem in text]
    total_nums = quick_merge(total_nums, numbers)


print(*total_nums)


# TODO Is Valid Triangle?
# Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов три натуральных числа, и возвращает значение True если существует невырожденный треугольник со сторонами side1, side2, side3 и False в противном случае.

# Примечание 1. С данной задачей мы уже сталкивались при изучении условного оператора.
# Неравенство треугольника (невырожденный) — длина наибольшей стороны меньше суммы длин двух других сторон (True)

def is_valid_triangle(side1, side2, side3):
    numbers = [side1, side2, side3]
    if max(numbers) < sum(numbers) - max(numbers):
        return True
    else:
        return False

a, b, c = int(input()), int(input()), int(input())
print(is_valid_triangle(a, b, c))


def is_valid_triangle(*args):
    if max(args) < sum(args) - max(args):
        return True
    else:
        return False


a, b, c = int(input()), int(input()), int(input())
print(is_valid_triangle(a, b, c))


# TODO Is a Number Prime? 🌶️
# Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True если число является простым и False в противном случае.
def is_prime(num):
    divider = 0
    for digit in range(2, num + 1):
        if num % digit == 0:
            divider += 1
    if divider == 1:
        return True
    else:
        return False


number = int(input())
print(is_prime(number))


def is_prime(num):
    if num == 1:
        return False
    for digit in range(2, num):
        if num % digit == 0:
            return False
    return True


number = int(input())
print(is_prime(number))


# TODO Next Prime 🌶️🌶️
# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое число большее числа num.

# Примечание 1. Используйте функцию is_prime() из предыдущей задачи.

def get_next_prime(num):
    prime_nums = []
    if num == 1:
        return 2
    for digit in range(num + 1, num + num):
        if is_prime(digit):
            prime_nums.append(digit)
    return prime_nums[0]


def is_prime(num):
    if num == 1:
        return False
    for digit in range(2, num):
        if num % digit == 0:
            return False
    return True


number = int(input())
print(get_next_prime(number))


# TODO Good password 🌶️
# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является надежным и False в противном случае.
# Пароль является надежным если: его длина не менее 8 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.

def is_password_good(password):  # aabbCC11OP
    upper_case = [chr(elem) for elem in range(ord(chr(65)), ord(chr(91)))]
    lower_case = [chr(elem) for elem in range(ord(chr(97)), ord(chr(123)))]
    nums = [chr(elem) for elem in range(ord(chr(48)), ord(chr(58)))]
    if len(password) >= 8:
        for symbol in password:
             if symbol in nums and symbol in (upper_case) and symbol in lower_case:
                return True
    return False


tetx = input()
print(is_password_good(tetx))



def is_password_good(password):  # aabbCC11OP
    nums = [chr(elem) for elem in range(ord(chr(48)), ord(chr(58)))]
    counter = 0
    if len(password) < 8:
        return False
    if password != password.upper():
        counter += 1
    if password != password.lower():
        counter += 1
    for symbol in password:
        if symbol in nums:
            counter += 1
            break
    if counter == 3:
        return True
    return False


text = input()
print(is_password_good(text))


def is_password_good(password):
   if len(password) < 8:
       return False
   flag_1 = False
   flag_2 = False
   flag_3 = False
   for symbol in password:
       if symbol.isupper():
           flag_1 = True
       if symbol.islower():
           flag_2 = True
       if symbol.isdigit():
           flag_3 = True
   return flag_1 and flag_2 and flag_3


text = input()
print(is_password_good(text))


# TODO Ровно в одном
# Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2 и возвращает значение True если слова имеют одинаковую длину и отличаются ровно в 1 символе и False в противном случае.

def is_one_away(word_1, word_2): # bike (aab aba)
    counter = 0
    len_word = len(word_1)
    if len(word_1) == len(word_2):
        for letter_1 in word_1:
            for letter_2 in word_2:
                if letter_1 == letter_2:
                    counter += 1
                    word_1 = word_1[1:]
                    word_2 = word_2[1:]
                    break
                else:
                    word_1 = word_1[1:]
                    word_2 = word_2[1:]
                    break
    else:
        False
    if counter == len_word - 1:
        return True
    else:
        return False


text_1 = input()
text_2 = input()
print(is_one_away(text_1, text_2))


def is_one_away(word_1, word_2):
    counter = 0
    for elem in range(len(word_1)):
        if word_1[elem] != word_2[elem]:
            counter += 1
    if len(word_1) == len(word_2) and counter == 1:
        return True
    return False


text_1 = input()
text_2 = input()
print(is_one_away(text_1, text_2))


# TODO Палиндром 🌶️
# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True если указанный текст является палиндромом и False в противном случае.
# Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях
# Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы, а также символы , . ! ? -.
def is_palindrome(text):
    symbols = ".,!?- "
    text = [symbol.lower() for symbol in text if symbol not in symbols]
    return text == text[::-1]


txt = input()
print(is_palindrome(txt))



def is_palindrome(text):
    symbols = [".", ",", "!", "?", "-", " "]
    for symbol in symbols:
        text = text.replace(symbol, "")
    return text == text[::-1]


txt = input().lower()
print(is_palindrome(txt))




def is_palindrome(txt):
    new_txt = []
    for symbol in txt:
        if symbol not in ".,!?-":
            new_txt.append(symbol)
    new_txt = "".join(new_txt)
    return new_txt == new_txt[::-1]


text = input().lower().replace(" ", "")
text = list(text)
print(is_palindrome(text))


def is_palindrome(text):
    new_text = []
    for symbol in text:
        if symbol not in ".,!?- ":
            new_text.append(symbol.lower())
    print(new_text)
    return new_text == new_text[::-1]



txt = input()
print(is_palindrome(txt))


# TODO BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.

def is_valid_password(password):
    if len(password) > 3:
        return False
    flag_1, flag_2, flag_3 = False, False, False
    if password[0] == password[0][::-1]:
        flag_1 = True
    if is_prime(password[1]):
        flag_2 = True
    if int(password[2]) % 2 == 0:
        flag_3 = True
    return flag_1 and flag_2 and flag_3


def is_prime(number):
    number = int(number)
    if number <= 2:
        return False
    for digit in range(2, number):
        return number % digit != 0


text = input().split(":")
print(is_valid_password(text))


# TODO Правильная скобочная последовательность 🌶️
# Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text, состоящую из символов ( и ) и возвращает значение True если поступившая на вход строка является правильной скобочной последовательностью и False в противном случае.

# Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только из символов ( и ), где каждой открывающей скобке найдется парная закрывающая скобка.
def is_correct_bracket(text):
    symbol = "()"
    while symbol in text:
        text = text.replace(symbol, "")
    return text == ""


txt = input()
print(is_correct_bracket(txt))


def is_correct_brasket(text):
    counter = 0
    for symbol in text:
        if counter < 0:
            return False
        elif symbol == "(":
            counter += 1
            continue
        elif symbol == (")"):
            counter -= 1
    return counter == 0


txt = input()
print(is_correct_brasket(txt))


# TODO Змеиный регистр
# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».
# Примечание 1. Почитать подробнее о стилях именования можно тут.

def convert_to_python_case(text):  # MyMethodThatDoSomething
    for symbol in text:
        if symbol.isupper():
            text = text.replace(symbol, "_" + symbol.lower())
    return text[1:]

txt = input()
print(convert_to_python_case(txt))


def convert_to_python_case(text):
    new_text = ""
    for symbol in text:
        if symbol.isupper():
            new_text += "_"
        new_text += symbol.lower()
    return new_text[1:]

txt = input()
print(convert_to_python_case(txt))

#TODO Середина отрезка
#Напишите функцию get_middle_point(x1, y1, x2, y2), которая принимает в качестве аргументов координаты концов отрезка 
#(x1;y1) и (x2;y2) и возвращает координаты точки являющейся серединой данного отрезка.
#Примечание 1. Координаты середины отрезка с концами в точках вычисляются по формуле:
#(x1+x2/2; y1+y2/2)

def get_middle_point(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y



x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())
x, y, = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)



#TODO Площадь и длина
#Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус 
#окружности и возвращает два значения: длину окружности и площадь круга, ограниченного данной окружностью.
#
#Примечание 1. Длина окружности и площадь круга радиуса r вычисляются по формулам:
#С=2πr, S=πr**2
#Примечание 2. Для числа π используйте глобальную константу из модуля math.

import math


def get_circle(radius):
    c = 2 * math.pi * radius
    s = math.pi * radius ** 2
    return c, s



r = float(input())
length, square = get_circle(r)
print(length, square)


#TODO Корни уравнения 🌶️🌶️
#Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых
#числа a, b, c – коэффициенты квадратного уравнения ax2+bx+c=0 и возвращает его корни в порядке возрастания.
#Примечание 1. С подобной задачей мы уже сталкивались.
#Примечание 2. Гарантируется, что квадратное уравнение имеет корни.
#discriminant=D = b**2 − 4ac. 

def solve(a, b, c):
    discriminant = (b**2) - (4 * a * c)
    square_1 = (-b + discriminant**0.5) / (2 * a)
    square_2 = (-b - discriminant**0.5) / (2 * a)
    return min(square_1, square_2), max(square_1, square_2)



a, b, c = int(input()), int(input()), int(input())
x1, x2 = solve(a, b, c)
print(x1, x2)


#-------------------begin------------------------------
def draw_triangle():
    height = 8
    for symbol in range(height):
        print(" " * (height - 1 - symbol) + "*" * (1 + symbol * 2))


draw_triangle()



def get_shipping_cost(quantity):
    if quantity == 1:
        return quantity * 1000
    return (quantity - 1) * 120 + 1000


number = int(input())
print(get_shipping_cost(number))



def compute_binom(n, k):
    result = factorial(n) / (factorial(k) * factorial(n - k))
    return int(result)


def factorial(num):
    fac = 1
    for digit in range(1, num + 1):
        fac *= digit
    return fac


n = int(input())
k = int(input())
print(compute_binom(n, k))





# 
# def number_to_words(num):
    # if num // 10 == 0:
        # return search(num)
    # print((num // 10) * 10)
    # print(num % 10)
    # return search((num // 10) * 10), search(num % 10)
# 
# 
# 
# def search(n):
    # numbers = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть',
            #    7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять', 11: 'одиннадцать',
            #    12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать',
            #    15: 'пятнадцать', 16: 'шестнадцать',17: 'семнадцать', 18: 'восемнадцать',
            #    19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать', 40: 'сорок',
            #    50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
            #    80: 'восемьдесят', 90: 'девяносто'}
    # return numbers[n]
# 
# 
# number = int(input())
# print(number_to_words(number))


def number_to_words(num):
    one = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    two = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    three = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if num // 10 == 0:
        return one[num - 1]
    if num // 10 == 1:
        return two[num % 10]
    if num % 10 == 0:
        return three[num // 10 - 2]
    else:
        return three[num // 10 - 2] + " " + one[num % 10 - 1]



number = int(input())
print(number_to_words(number))





def get_month(language, number):
    lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if language == "ru":
        return lng_ru[number - 1]
    return lng_en[number - 1]

lan = input()
num = int(input())
print(get_month(lan, num))



def is_magic(date):
    return int(date[0]) * int(date[1]) == int(date[2]) % 100


date = input().split(".")
print(is_magic(date))





def is_pangram(text):
    text = set(text)
    counter = 0
    abc = "abcdefghijklmnopqrstuvwxyz"
    for letter in text:
        if letter in abc:
            counter += 1
    return counter == 26


txt = input().lower()
print(is_pangram(txt))


#-------------------end------------------------------





