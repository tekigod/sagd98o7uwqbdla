# Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint
candies = int(input('Сколько конфет: '))
take = int(input("Максимальное количество конфет можно взять: "))

def take_to_have_for_first(candies, take):
    take_candies = candies % (take + 1)
    if take_candies == 0:
        take_candies = take
    return(f'чтобы выиграть первому ходящему необходимо взять {take_candies}')

first_move = randint(1,2) 
print(f"Первым ходит игрок {first_move}")
second_move = 3 - first_move
print(f'Второй ходит игрок {second_move}')
count = 0
while candies > 0:
    count += 1
    player1 = int(input("Ход первого игрока. Возьмите конфеты: "))
    candies = candies - player1
    print(f'осталось конфет: {candies}')
    print(take_to_have_for_first(candies, take))
    if candies > 0:
        player2 = int(input("Ход второго игрока. Возьмите конфеты: "))
        candies = candies - player2
        print(f'осталось конфет: {candies}')
        print(take_to_have_for_first(candies, take))
if candies == 0:
    print('Игра окончена')
if take % 2 != 0:
    print(f'Победил игрок {first_move}')
else:
    print(f'Победил игрок {second_move}')