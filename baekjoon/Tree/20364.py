import sys

n, q = map(int, sys.stdin.readline().split())

visited = [0] * (n + 1) # 땅의 점유 여부

# 반복문을 통해 오리들이 원하는 땅을 가지도록 한다.
for i in range(q):
    tan = int(sys.stdin.readline())
    target = tan
    flag = 0 # 다른 오리의 점유된 땅의 번호

    # 반복문을 통해 원하는 땅에서 루트 땅까지 점유된 땅을 밟는지 확인
    while target != 1:

        # 점유된 땅을 밟을 경우
        if visited[target] >= 1:
            flag = target # 다른 오리의 점유된 땅의 번호를 초기화

        # 2로 나눠 루트 땅까지 이동
        target //= 2

    # 루트 땅까지 이동하면서 점유된 땅을 밟았다면
    if flag:
        print(flag) # 밟은 땅의 번호를 출력

    # 그게 아니라면 땅을 점유하고 0을 출력
    else:
        visited[tan] = 1
        print(0)
