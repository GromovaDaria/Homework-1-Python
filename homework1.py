# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# week_day = int(input('Input the serial number of the day of the week '))
#if 1 < week_day <=5:
#    print('It is not a weekend')
#elif 5 < week_day <= 7:
#    print('It is a weekend')
#else:
#    print('Invalid number. Please enter a number from 1 to 7')

# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

#def InputNumbers(a): 
#    xyz = []
#    for i in range(a):
#        xyz.append(input(f'Input the number {i+1}: '))
#    return xyz


#def CheckPredicate(list):  
#    first = not (list[0] or list[1] or list[2])
#    second = not list[0] and not list[1] and not list[2]
#    result = first == second
#    return result
#newlist = InputNumbers(3)
#if CheckPredicate(newlist) == True:
#    print('The statement is true')
#else:
#    print('The statement is false')

#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

#def CheckCoord(a, b):
#    if a and b > 0:
#        result = 1
#    if a < 0 and b > 0:
#        result = 2
#    if a and b < 0:
#        result = 3
#    if a > 0 and b < 0:
#        result = 4
#    return result
#
#x = int(input('Enter value X: '))
#while x == 0:
#    x = int(input("Error. Enter a value that won't be 0: "))
#
#y = int(input('Enter value Y: '))
#while y == 0:
#    y = int(input("Error. Enter a value that won't be 0: "))
#print(f'coordinate point is in quarter {CheckCoord(x,y)}')

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

#x = int(input('Enter quarter number (from 1 to 4): '))
#if x > 4 or x < 1:
#    print("Error! This quarter doesn't exist. Enter number from 1 to 4")
#elif x == 1:
#    print('The range in this quarter x > 0, y > 0')
#elif x == 2:
#    print('The range in this quarter x < 0, y > 0')
#elif x == 3:
#    print('The range in this quarter x < 0, y < 0')
#elif x == 4:
#    print('The range in this quarter x > 0, y < 0')

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#Пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

import math

def distance(ax,ay,bx,by):
    AC = bx - ax
    BC = by - ay
    AB = math.sqrt(AC**2 + BC**2)
    return AB

ax = int(input('Enter the X coordinate of point А: '))
ay = int(input('Enter the Y coordinate of point А: '))
bx = int(input('Enter the X coordinate of point B: '))
by = int(input('Enter the Y coordinate of point B: '))
result = round(distance(Ax,Ay,Bx,By),3)
print(f'The distance between point А({Ax}, {Ay}) and point B({Bx}, {By}) is {result}')