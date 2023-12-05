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

def genRandMatrix(nRows, nCols):
    mat = []

    for i in range(0, nRows):
        row = [random.randrange(-10, 10) for _ in range(0, nCols)]

        mat.append(row)

    return mat

def prog1():
    try:
        m = int(input("Введите количество столбцов матрицы:.."))
        n = int(input("Введите количество строк матрицы:.."))
    except:
        oshibka()
    kant = m
    if (m and n) <= 0:
        oshibka()
    else:
        matrix = []
        for i in range(n):
            stroka = []
            for k in range(m):
                rand = random.randint(-10, 10)
                stroka.append(rand)
            matrix.append(stroka)
        for i in matrix:
            print(i)
        for i in range(m):
            for k in matrix:
                if k[i] == 0:
                    kant-=1
                    break
    print(f'количество ненулевых столбцов в матрице = {kant}')




def prog2():
    cnt = 0
    summa = 0
    try:
        m = int(input("Введите количество столбцов матрицы:.."))
        n = int(input("Введите количество строк матрицы:.."))
    except:
        oshibka()
    kant = m
    spisSum = []
    if (m and n) <= 0:
        oshibka()
    else:
        matrix = []
        for i in range(n):
            stroka = []
            for k in range(m):
                rand = random.randint(-10, 10)
                stroka.append(rand)
            matrix.append(stroka)
        for i in matrix:
            print(i)
        for i in matrix:
            for j in i:
                summa += j
            spisSum.append(summa)
        print("~"*15)
        print(spisSum, "суммы")
        for i in range(len(spisSum) - 1):
            for j in range(len(spisSum) - i - 1):
                if spisSum[j] > spisSum[j + 1]:
                    spisSum[j], spisSum[j + 1] = spisSum[j + 1], spisSum[j]
                    matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
        print(spisSum, "последовательность сумм")
        print("получившаяся матрица:")
        for i in matrix:
            print(i)





def prog3():
    pythonist = 'pythonist'
    slov = dict()
    for i in pythonist:
        cnt = 0
        for j in pythonist:
            if i==j:
                cnt+=1
        slov[i] = cnt
    print(slov)


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