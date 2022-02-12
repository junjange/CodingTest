import sys


# 부등호 확인 함수
def poss(i, j, l):
    if l == ">":
        return i > j
    else:
        return i < j


# backTracking
def backTracking(idx, word):
    global mx, mn

    # idx가 부등호 문자의 개수보다 크다면 모든 숫자를 알맞게 넣은 것
    if idx > k:
        # 맨처음 만족하는 값이 최소, 마지막에 저장되는 것이 최대
        if len(mn) == 0:
            mn = word
        else:
            mx = word
        return

    # 반복문을 통해 0부터 9까지의 숫자를 확인
    for i in range(10):
        # 탐색하지 않은 숫자라면
        if not visited[i]:
            # 현재 탐색중인 idx가 0이거나 부등호가 참이라면
            if idx == 0 or poss(word[-1], str(i), m[idx - 1]):
                visited[i] = True # 현재 숫자 탐색 확인
                backTracking(idx + 1, word + str(i)) # idx + 1해주고 현재 숫자를 합친 문자열을 재귀적으로 다시 탐색
                visited[i] = False # backTracking


k = int(sys.stdin.readline())
m = list(map(str, sys.stdin.readline().split()))
visited = [False] * 10 # 숫자는 한번만 사용 가능하기 때문에 사용여부를 확인
mx, mn = "", "" # 최댓값과 최솟값
backTracking(0, "")

print(mx)
print(mn)
