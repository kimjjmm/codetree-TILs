N = int(input())

A = [ input() for _ in range(N)]
A.sort()

# for word in A:
#     print(word)

print(*A, sep="\n")