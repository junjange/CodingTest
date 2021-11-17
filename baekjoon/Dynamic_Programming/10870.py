import sys


def dp(m):
    # 피보나치 수가 0일 때 0을 리턴
    if m == 0:
        return 0
    
    # 피보나치 수가 1일 때 1을 리턴
    elif m == 1:
        return 1
    
    # 피보나치가 2 이상일 경우에는 바로 앞 두 피보나치를 재귀 호출로 구해 합한다.
    else:
        return dp(m - 1) + dp(m - 2)


n = int(sys.stdin.readline())
print(dp(n))
