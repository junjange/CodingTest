import sys

r = int(sys.stdin.readline())
# 중복 조합을 통해 문제를 수행한다. nHr = n+r-1 C r
n = 10 + r - 1

a = n # n+r-1
b = r # r

# aCb 구현
for i in range(1, r):
    a *= n - i # n x (n - i) .. x (n - r + 1)
    b *= r - i # r!

print((a // b) % 10007) # a! // b!
