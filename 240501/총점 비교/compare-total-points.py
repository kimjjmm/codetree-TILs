class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

N = int(input())
students = []
for _ in range(N):
    name, kor, eng, math = input().split()
    student = Student(name, int(kor), int(eng), int(math))
    students.append(student)
    

# 점수의 총합 기준 오름차순
students.sort(key=lambda x: x.kor + x.eng + x.math) 

for student in students: # 정렬 이후의 결과 출력
    print(student.name, student.kor, student.eng, student.math)