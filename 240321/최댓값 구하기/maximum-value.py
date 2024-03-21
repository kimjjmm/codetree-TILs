inp = input().split()

a = int(inp[0])
b = int(inp[1])
c = int(inp[2])

if a>=b:
    if a>=c:
        print(a)
    else:
        print(c)
elif b>=c:
    if b>=a:
        print(b)
    else:
        print(a)
elif c>=a:
    if c>=b:
        print(c)
    else:
        print(b)