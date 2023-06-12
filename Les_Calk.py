
def f(x):
     return x*x
print(f(5))
print(type(f))  # смотрим к чему относится(type)  .. этo (fункция)...


a = f
print((a))
print(a(5))
print(f(5))     # все одинаково
print()

def calk1(a):
    return a+a

def calk2(a):
    return a*a

def math(op, x):     # ор - какая-то фунция, х -параметр
    print(op(x))
    
math(calk1, 5) 
math(calk2, 5) 
    


