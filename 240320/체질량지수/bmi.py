inp = input().split()

height = int(inp[0])
weight = int(inp[1])
BMI = (weight*100*100)//(height**2)

print(BMI)

if BMI >=25:
    print("Obesity")