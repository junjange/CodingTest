import sys

n = int(sys.stdin.readline())
budget = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

_max = max(budget) # 예산 상한액의 최댓값
_min = 1 # 예산 상한액의 최솟값

# 이분 탐색
while _max >= _min:
    mid = (_max + _min) // 2 # 예산 상한액
    res = 0 # 배정한 예산액

    # 반복문을 통해 예산을 배정
    for i in budget:
        # 예산 상한액보다 요청된 예산이 크면 예산 상한액을 배정
        if mid < i:
            res += mid

        # 예산 상한액보다 요청된 예산이 작거나 같다면 요청된 예산액 배정
        else:
            res += i

    # 배정한 예상액이 총 예산보다 크다면 예산 상한액을 줄여주기 위해
    # 예산액 최대 범위를 현재 예산 상한액의 -1 해준 값으로 초기화한다.
    if res > m:
        _max = mid - 1

    # 배정한 예상액이 총 예산보다 작거나 같다면 예산 상한액을 높여주기 위해
    # 예산액 최소 범위를 현재 예산 상한액의 +1 해준 값으로 초기화한다.
    else:
        _min = mid + 1

# 배정할 수 있는 예산 상한액의 최대값 출력
print(_max)
