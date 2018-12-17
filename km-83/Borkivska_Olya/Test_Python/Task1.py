""""
Дано довільний список. Вивести рекурсивно елементи списку з індексами, що обчисллюються формулою index = 3*i, де і=0,1,2,3,....
"""


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def rez(list, i=0):
    try:
        print(list[i * 3])
        i += 1
        rez(list, i)
    except IndexError:
        return


rez(list)