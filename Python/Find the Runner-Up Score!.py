n = int(input())
arr = list(map(int, input().split()))
array=[]
for i in range(len(arr)):
    if arr[i] not in array:
        array.append(arr[i])
        
t=0      
for i in range(len(array)):
    for j in range(i+1 , len(array)):
        if array[i]>array[j]:
            t=array[i]
            array[i]=array[j]
            array[j]=t
            
            
print(array[-2])
