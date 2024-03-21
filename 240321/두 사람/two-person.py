info1 = input().split()
info2 = input().split()

age1 = int(info1[0])
sex1 = info1[1]

age2 = int(info2[0])
sex2 = info2[1]

if (age1 >= 19 and sex1 == 'M') or (age2 >=19 and sex2 == 'M'):
    print(1)
else:
    print(0)