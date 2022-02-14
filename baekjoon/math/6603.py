import sys


def lotto(idx, num):
    # 6개의 로또 번호 경우의 수를 찾았다면 결과를 출력하고 리턴
    if idx == 6:
        print(*res)
        return

    # 반복문을 통해 로또 집합을 확인
    for i in range(num, k):
        # 탐색하지 않은 로또 번호라면 탐색
        if not visited[i]:
            res[idx] = s[i] # 경우의 수에 현재 로또 번호를 추가
            visited[i] = True # 탐색
            lotto(idx + 1, i + 1) # 재귀적으로 탐색
            visited[i] = False # backTracking


# 반복문을 통해 테스트 케이스를 입력 받음
while True:
    n = list(map(int, sys.stdin.readline().split()))

    # 테스트 케이스가 0이면 반복을 멈춤
    if n[0] == 0:
        break

    k = n[0] # 로또 집합의 개수
    s = n[1:] # 로또 집합
    visited = [False] * k # 로또 번호는 한번만 사용 가능하기 때문에 사용여부 확인
    res = [0] * 6 # 경우의 수
    lotto(0, 0)
    print()

