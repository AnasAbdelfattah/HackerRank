if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
value_list=student_marks[query_name]
sum=0
for num in value_list:
    sum=float(sum + num)
avg=sum/len(value_list)
print(f"{avg:.2f}")


