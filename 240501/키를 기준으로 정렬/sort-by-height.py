class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

N = int(input())
people=[]
for _ in range(N):
    name, height, weight = input().split()
    people.append(Person(name,int(height), int(weight)))

people.sort(key=lambda p: p.height) # 국어 점수 기준 오름차순 정렬

for student in people: # 정렬 이후의 결과 출력
    print(student.name, student.height, student.weight)