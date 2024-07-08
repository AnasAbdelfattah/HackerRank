n,m=(input()).split()

arr=map(int,input().split())

A =set(map(int,input().split()))

B =set(map(int,input().split()))

count_happenies=0

for num in arr : 
    if num in A :
        count_happenies+=1 
    elif num in B : 
        count_happenies-=1 
 print(count_happenies)
