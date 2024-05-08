n = int(input())
arr = list(map(int,input().split()))
sum_val = 0
arr_even = []

for elem in arr:
    if elem % 2 == 0:
        arr_even.append(elem)


for value in reversed(arr_even):
    print(value, end=" ")