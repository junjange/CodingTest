import sys

n, k =map(int,sys.stdin.readline().split())

s = list(map(int,sys.stdin.readline().split()))


for i in range(k):
    a, b = list(map(int,sys.stdin.readline().split()))
    c = b-a +1
    result= sum(s[a-1:b])/c
    print("%0.2f" % result)

