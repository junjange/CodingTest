import sys

p, n = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

result = a[0]

for i in range(1,n):
    result = (result * p)%1000000007

    if len(a) > i:
        result += a[i]


print(result)


