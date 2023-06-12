# import random
# n = 8
# list =[]
# for i in range(n):
#     list.append(random.randint(0,6))
# print(*list)

def mergeSort(list):
    if len(list) >1:
       mid = len(list) //2
       list1 = list[:mid]
       list2 = list[mid:]
       mergeSort(list1)
       mergeSort(list2)
       i = j = k = 0
       while i < len(list1) and j < len(list2):
           if list1[i] < list2[j]:
               list[k] = list1[i]
               i+= 1
           else:
               list[k] = list2[j]    
               j+=1
           k +=1  
       while i < len(list1):
           list[k] = list1[i]
           i+= 1
           k+= 1  
           
       while j < len(list2):
           list[k] = list2[j]
           j+= 1
           k+= 1  
           
list3 = [3,5,1,7,34,23,11,15] 
mergeSort(list3) 
print(list3)               