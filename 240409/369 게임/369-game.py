n = int(input())

for i in range(1,n+1):
    if i %3 ==0:
        print(0,end = " ")
    elif str(i) == '3' or str(i) =='6' or str(i) =='9':
        print(0, end= " ")
    else:
        print(i,end=" ")