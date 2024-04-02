n = int(input())

while n <= 100:
    if n >= 90:
        print("A", end=' ')
        n+=1
    elif n >= 80:
        print("B", end =' ')
        n+=1
    elif n>=70:
        print("C", end =' ')
        n+=1
    elif n>=60:
        print("D", end =' ')
        n+=1
    else:
        print("F",end =' ')
        n+=1