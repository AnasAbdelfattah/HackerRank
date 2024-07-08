from itertools import combinations

N = int(input())
L = input().lower().split()
K = int(input())

count = 0

for i in combinations(L, K):
    if 'a' in i:
        count += 1
 
result= count/len(list(combinations(L, K)))

print(f"{result:.3f}")
