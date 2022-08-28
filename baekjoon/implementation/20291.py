import sys


n = int(sys.stdin.readline())
dic = {}
for _ in range(n):
    pile = str(sys.stdin.readline()).split(".")
    path = pile[1].rstrip("\n")
    if path in dic:
        dic[path] += 1
    else:
        dic[path] = 1

answer = sorted(dic.items())

for key, value in answer:
    print(key, value)
