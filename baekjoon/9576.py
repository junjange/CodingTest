import sys

case = int(sys.stdin.readline())
# 케이스만큼 반복
for _ in range(case):
    n, m = map(int, sys.stdin.readline().split())
    # a, b 구간을 리스트로 받고 b번 기준으로 정렬
    ab = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    ab = sorted(ab, key=lambda x: x[1])

    # 학생 수
    cnt = 0
    # 계수 정렬, n + 1권에 책
    chek = [1] * (n + 1)

    # 모든 구간을 반복하여 확인
    for a, b in ab:
        # 구간 길이 확인
        for i in range(a, b + 1):
            print(chek)
            # 책이 있으면 책을 준다.
            if chek[i] == 1:
                # 책을 줬으므로 0으로 초기화
                chek[i] = 0
                # 학생 수 카운트
                cnt += 1
                # 구간에 있는 학생에게 책을 줬으므로 멈춘다.
                break

    # 각 케이스 별로 학생 수를 출력
    print(cnt)
