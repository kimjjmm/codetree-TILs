arr = list(map(int, input().split()))
cnt = 0
sum = 0

for elem in arr:
    if elem == 0:
        break
    sum += elem
    cnt += 1


print(sum, sum/cnt)