if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for i in student_marks.keys():
        total = 0
        if i == query_name:
            for j in range(len(student_marks[i])):
                total += student_marks[i][j]
            average = total / len(student_marks[i])
            print(f'{average:.2f}')
