year = int(input())

if (year%4==0):
    print('true')

elif (year%100 ==0):
    if(year%400 != 0):
        print('false')