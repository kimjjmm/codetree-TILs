n = int(input())
sum_val = 0
avg = 0
arr = list(map(float, input().split()))

for elem in arr:
    sum_val += elem
avg = sum_val/n
print(f"{avg:.1f}")
if avg >= 4.0:
    print('Perfect')
elif avg >= 3.0:
    print("Good")
else:
    print("Poor")