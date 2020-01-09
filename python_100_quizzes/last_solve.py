import random  as r

# 총 7개, 30명인 학생, 5과목
class_num = 7
student_num = 30
subject_num = 5

# 1. 반 점수 모두가 담긴 전교 점수 다중 리스트를 만들어주세요.

total_score = []
for i in range(class_num):
    class_score = []
    for j in range(student_num):
        score = []
        for i in range(subject_num):
            score.append(r.randint(1, 100))
        class_score.append(score)
    total_score.append(class_score)
print('1번 문제')
print(total_score)

# 전체 평균, 반 평균, 학생 평균
total_avg = 0
class_avg = []

# 2. 반 평균을 구하세요.
for classes in total_score:
    student_avg = 0
    for students in classes:
        student_avg += sum(students) / subject_num
    class_avg.append(student_avg / student_num)
print('2번 문제')
print(class_avg)

# 3. 반 1등 점수를 구하세요.
frist_class = []
for classes in total_score:
    frist_rank = 0
    for students in classes:
        sum_students = sum(students)
        if frist_rank < sum_students:
            frist_rank = sum_students
    frist_class.append(frist_rank)
print('3번 문제')
print(frist_class)

# 4. 전교 평균을 구하세요.
print('4번 문제')
print(sum(class_avg) / class_num)