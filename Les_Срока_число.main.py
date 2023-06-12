def sum_str(*args):
    res = ''
    for i in args:
        res+= i
    return res 
print(sum_str('g','e','l'))  
print(sum_str('g','e','l','i','k')) 
print(sum_str('123')) 
print(sum_str('1','2','3')) 