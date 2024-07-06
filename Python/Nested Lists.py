if __name__ == '__main__':
    student_list = []
    student_score_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_list.append([name, score])
        student_score_list.append(score)
    
    min_score = min(student_score_list)
    second_lowest_score_list = [score for score in student_score_list if score != min_score]
    
    second_lowest_score = min(second_lowest_score_list)
    
    final_list = [student[0] for student in student_list if student[1] == second_lowest_score]
    
    final_list.sort()
    
    for name in final_list:
        print(name)
