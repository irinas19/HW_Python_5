""" Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом"" """

import random
totalSweets=2021

def CheckEnteredNumber(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def GetScore(candiesAmount,turn):
    while True:
        if CheckEnteredNumber(candiesAmount):
            candiesAmount=int(candiesAmount)
            if 0<candiesAmount<=28:
                return candiesAmount
            else:
                print("Check your input, it must be integer [1...28].")
                candiesAmount=input(f"Player {turn} turn. Enter number of candies. It should be in range [1...28]: ")
        else:
            print("Check your input, it must be integer [1...28].")
            candiesAmount=input(f"Player {turn} turn. Enter number of candies. It should be in range [1...28]: ")

def Lottery():
    print("Now you will have lotery to identify who will be the first!")
    player1Num=input("The first player please enter your number from 0 to 100: ")
    player2Num=input("The second player please enter your number from 0 to 100: ")
    if CheckEnteredNumber(player1Num) and CheckEnteredNumber(player2Num):
        player1Num=int(player1Num)
        player2Num=int(player2Num)
        if (0<=player1Num<=100) and (0<=player2Num<=100):
            botNum=random.randint(0,100)
            print(f"The reference number is {botNum}.")
            dif1=abs(player1Num-botNum)
            dif2=abs(player2Num-botNum)
            if dif1>dif2:
                return False
            else:
                return True
        else:
             print("Check your input, it must be integer [0...100].")
             Lottery()
    else:
        print("Check your input, it must be integer [0...100].")
        Lottery()

def Game(candiesNum):
    if Lottery():
        print("Player 1 the first.")
        turnFlag=1
    else:
        print("Player 2 the first.")
        turnFlag=2
    while candiesNum>0:
        print(f"{candiesNum} candies left.")
        if turnFlag==1:
            candiesAmount=GetScore(input(f"Player {turnFlag} turn. Enter number of candies. It should be in range [1...28]: "),turnFlag)
            turnFlag=2
        else:
            candiesAmount=GetScore(input(f"Player {turnFlag} turn. Enter number of candies. It should be in range [1...28]: "),turnFlag)
            turnFlag=1
        candiesNum=candiesNum-candiesAmount
    return turnFlag  

winName=Game(totalSweets)
if winName==2:
        print("Player 1 is winner!") 
else:
        print("Player 2 is winner!")  