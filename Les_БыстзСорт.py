import abc


def qwikSort(array):
    if len(array)<=1:
        return array
    else:
        num = array[0]
    list1 = [i for i in array[1:] if i <= num ]  #Проходим по 1 списку от i до  елемента кроме[1-первого[0]]]
                                                #-тк 1ел[0]это num ..используем срезы [1:] берем  ел которые
                                                # меньше [num]
   
    list2 = [i for i in array [1:] if i > num]  
    return  qwikSort(list1) + [num] + qwikSort(list2)  
                                     
print(qwikSort)
print(qwikSort([11,12,3, 5, 6,17, 9,16]))