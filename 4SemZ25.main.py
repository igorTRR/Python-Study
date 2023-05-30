# 25. Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам
# с помощью постфикса формата _n.

replay = 'a a a b a c b b d'.split()
letters = {}
result = ''
for i in range(len(replay)):                # через срезы
    if replay[0:i:].count(replay[i]) == 0:
        result += replay[i]
    else:
         result += f'{replay[i]}_{replay[0:i].count(replay[i])}'
    print(replay[0:i], result)
print(result)
 

# for i in range(len(replay)):
#     if replay[i] not in letters.keys():
#         letters[replay[i]] = 1
#         result += f'{replay[i]} '
#     else:
#         result += f'{replay[i]}_{letters[replay[i]]} '
#         letters[replay[i]] += 1
# print(result)

