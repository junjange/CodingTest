import sys


# 거듭제곱을 재귀적으로 수행
def fpow(a, b):
    # 1번 곱해도 되면 a % C를 리턴
    if b == 1: 
        return a % C
    
    # 곱해야하는 수가 1보다 많다면
    else:
        # 곱해야하는 수를 반으로 나누어 재귀적으로 탐색
        x = fpow(a, b//2)
        
        # 곱해야하는 수가 짝수이면 
        if b % 2 == 0:
            return x * x % C
        
        # 곱해야하는 수가 홀수이면
        else:
            return x * x * a % C


A, B, C = map(int, sys.stdin.readline().split())
print(fpow(A, B))
