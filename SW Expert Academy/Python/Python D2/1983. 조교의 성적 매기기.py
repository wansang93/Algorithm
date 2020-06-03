# 풀이1: 상위 몇 % 인지를 확인하여 출력하기
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split(' '))
    students = []
    for n in range(N):
        midterm, final, assignment = map(int, input().split())
        sum_all = midterm * 0.35 + final * 0.45 + assignment * 0.20
        students.append(sum_all)

    k_scores = students[K-1]
    students.sort(reverse=True)

    rank = (students.index(k_scores)+1) / N  # 등수 / 사람 수 -> 상위 몇 % 인지
    grade = ''

    if rank <= 0.1:
        grade = 'A+'
    elif rank <= 0.2:
        grade = 'A0'
    elif rank <= 0.3:
        grade = 'A-'
    elif rank <= 0.4:
        grade = 'B+'
    elif rank <= 0.5:
        grade = 'B0'
    elif rank <= 0.6:
        grade = 'B-'
    elif rank <= 0.7:
        grade = 'C+'
    elif rank <= 0.8:
        grade = 'C0'
    elif rank <= 0.9:
        grade = 'C-'
    else:
        grade = 'D'

    print('#{} {}'.format(t, grade))

# 풀이2: 학점을 배열에 담아서 리턴하기
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split(' '))
    students = []
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for n in range(N):
        midterm, final, assignment = map(int, input().split())
        sum_student = midterm * 0.35 + final * 0.45 + assignment * 0.20
        students.append(sum_student)

    k_score = students[K-1]
    students.sort(reverse=True)

    rank_of_ten = students.index(k_score) // (N//10)  # 핵심 코드
    k_grade = grade[rank_of_ten]

    print('#{} {}'.format(t, k_grade))
