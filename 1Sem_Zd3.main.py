import math
FirstCl = int(input('Введите количечтво учащихся 1кл: '))  #20
SecondCL = int(input('Введите количечтво учащихся 2кл: ')) #21
TherdCl = int(input('Введите количечтво учащихся 3 кл: '))  #22
i = ((FirstCl + 1//2) + (SecondCL + 1)//2 + (TherdCl +1) // 2)
print(math.ceil(i))



