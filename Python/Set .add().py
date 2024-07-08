N=int(input())

countries_list=[]
for _ in range(N):
    countries_list.append(input())
    

My_set=set(countries_list)
print(len(My_set))

