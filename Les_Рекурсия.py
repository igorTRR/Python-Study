def fibonfchi(n):
    if n in [1,2]: # базис -если n - находтся в списках -1,2 -то мы возвращаем 1...в прот случае - рекусию-fib//
        return 1
    return fibonfchi(n-1) + fibonfchi(n-2)

list = []
for i in range(1,10):
    list.append(fibonfchi(i))
print(list)    