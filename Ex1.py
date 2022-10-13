# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'Я вышел абв выгуливать рыбу' # сюда задавать слова 
text_find = 'абв'
index = 0

list1 = text.split(' ')
print(list1)

list2 = [item for item in list1 if text_find not in item]
print(list2)