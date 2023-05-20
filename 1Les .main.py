# a = 5.6755
# b = 6.2563
# #print(a*b)
# print(round(a*b,2))


# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif  username == 'Ника': 
#     print('Ника!долго тебя ждали!') 
# elif username == 'Катя':  
#      print('О- Катя')
# else:
#     print(username,'Привет')


# n = 1
# while n < 5:
#     print('верно')
#     n = n+1
# else:    
#     print('ФИНИШ')    

# n = 1
# while n < 5:
#     n += 1
#     if n == 3:
#         #break -плохой тон в пограммировании (исп flag)
#         continue
#     print(n)

# Нахождение мин делителя числа
# n = int(input('Введите число n: '))
# flag = True
# i = 1
# while flag:
#     if n % i == 0:#
#         flag = False
#         print(i)
#     elif i > n //2:
#         print(n) 
#         flag = False
#     i+=1

# Цикл For(числа), строки
#for i in 1, 4,-5, 0,-1:
   # print(i)
#r = range(5) 
#r = range(2,5)
# r = range(100,0,-50)
# for i in r:
#     print(i)  

# a = "qwerty"
# print(a)
# print(a[0]) # вывод по (индексу)
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])

#for i in a: 
    #print(i)
    
   # CЛОЖНЫЙ КОД
# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)   

    # СТРОКА
# text = 'ПроБуЮ игРать тЕксТом' 
# print(text) # вывод текста
# print(len(text))  # Длинна (размер) текста
# print('игРать' in text) # смотрить есть ли слово такое в тексте
# print(text.lower()) # все переводим в нижн.регистр
# print(text.upper()) # все в верхн регистр
# print(text.replace('игРать','баловаться')) # меняем слово  в тексте (букву)

    # СРЕЗЫ ( изменяем тексе по индексу)
text = 'ПроБуЮ игРать тЕксТом' 
print(text[:])    #  вывод текста c 0  до конца
print(text[:4])   #  если(:) стоят в начале - то берем от 0 буквы до 4 буквы (до 1..2..3 итд)
print(text[5:])   # c 5 буквы до конца
print(text[5:12]) # c 5 буквы до 12
print(text[5:-2])  #c 5 буквы до конца -2 (-3-5-15) последние буквы          
print(text[::4])  # oт 1 буквы до конца с шагом 4(те с1 каждую 4 букву)       
# или print(text[0:len(text):4]) c1 до конца с шагм 4
print(text[len(text)-2:])  # берем только 2 последние буквы т.к(:) стоят в конце
# еще можно сладовать так :...
text = text[:4] + text[5:12] + text[len(text)-2:]
print(text)


    
    