inp = input().split()
a = int(inp[0])
b = int(inp[1])
c = int(inp[2])


print(1 if a<b and a<c else 0, 1 if a==b and b==c and c==a else 0)