# Пользователь вводит текст(строка).
# Словом считается последовательность непробельных символов
# идущих подряд, слова разделены одним или большим числом
# пробелов или символами конца строки.Определите, сколько различных
# слов содержится в этом тексте.

text = '''She sells, sea shells on the sea shore. The shells\
 that she sells are sea shells! I'm sure So if she sells sea \
shells on the sea shore? I'm sure that\n the shells are sea \
shore shells'''.upper().replace ('.','' ).split()
# result = [i.strip('.,?!\n').lower() for i in text.split()]
# result = set(result)
# print(result)
# print(len(result))
print(text)
# print(len(text))
print (len(set(text)))

