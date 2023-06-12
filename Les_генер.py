list_1 = [i for i in range(1,20) ] # ГЕНЕРАТОР
print(list_1)

list_1 = list(map(lambda i: i + 10, list_1))
print(list_1)

data = '15 156 46 7 9 65'
print(data)

# data =data.split()
# print(data)

data = list(map(int,data.split()))# map -встроенная f можно пройти 1раз
print(data)
