#########    Постоянные переменные    #########
chisla = '0123456789'
latBykvi = "ABCDEFGHIKLMNOPQRSTVWXYZqwertyuioplkjhgfdsazxcvbnm"

import random, math


def oshibka():
    print('*' * 5 + "Введено неправитльное значение!" + '*' * 5)


def сntProbel(st):
    cnt = 0
    for i in st:
        if i == ' ':
            cnt += 1
    return cnt


def prog1():
    try:
        #spis = []
        #cnt = 0
        #maxi = mini = 0
        #st = str(input("введите строку, содержащую хотя бы один пробел:.."))
        #for i in range(len(st)):
        #    if st[i] == ' ':
        #        spis.append(i)
        #print(st[(spis[0]):(spis[-1])])
        m = int(input("Введите количество столбцов матрицы"))
        n = int(input("Введите количество строк матрицы"))
    except:
        oshibka()
    k = 0
    if (m and n) > 0:
        matrix = []
        for i in range(n):
            stroka = []
            for k in range(m):
                rand = random.randint(-10, 10)
                stroka.append(rand)
            matrix.append(stroka)
        for i in matrix:
            print(i)



#def prog2():
    #cnt = 0
    #st = str(input("введите строку:.."))
    #for i in st:
    #    if i in chisla:
    #        cnt += 1
    #print(cnt)






#def prog3():
#    try:
#        stp = ''
#        n = []
#        ln = int(input("Введите длину списка:.."))
#        l = [(random.randint(-100, 100) / (random.randint())) for i in range(ln)]
#        min = l[0]
#        print(l)
#        for i in l:
#            if min >= i:
#                min = i
#        print(min)
#        for i in l:
#            if abs(i) <= 1:
#                l.insert(0, i)
#
#    except:
#        oshibka()


CallProg = input("Введите номер задачи, который Вы хотите выполнить:..")

while True:
    if CallProg == "1":
        prog1()
        break
    elif CallProg == "2":
        prog2()
        break
    elif CallProg == "3":
        prog3()
        break
    else:
        print("Задачи под данным номером нет!")
        CallProg = input(f"\nВведите номер задачи, который Вы хотите выполнить:..")