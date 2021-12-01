import sys

t = int(sys.stdin.readline())

# 테스트 케이스만큼 반복
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    a = m
    b = n
    
    # mCn 구현
    for i in range(1, n):
        a *= m - i # m!
        b *= n - i # n!
        
    print(a // b) # m! // n!
