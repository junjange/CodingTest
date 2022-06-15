import sys
s1 = list(map(str, sys.stdin.readline().strip()))
s2 = list(map(str, sys.stdin.readline().strip()))

dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
answer = 0

# 반복문을 통해 두 개의 문자열을 확인
for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        # 두 개의 문자열중에 문자가 같다면 dp에 +1로 저장
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(dp[i][j], answer)

print(answer)
