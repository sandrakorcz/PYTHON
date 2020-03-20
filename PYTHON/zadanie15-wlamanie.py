n = int(input())
L = list(map(int, input().split()))
print(max(L) - min(L) + 1 - n)
