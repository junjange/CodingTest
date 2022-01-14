import sys

t = int(sys.stdin.readline())

# 반복문을 통해 테스트 데이터를 확인
for _ in range(t):
    n = int(sys.stdin.readline())
    initial_state = list(map(str, sys.stdin.readline().rstrip("\n")))
    target_state = list(map(str, sys.stdin.readline().rstrip("\n")))
    cnt = []

    # 반복문을 통해 오셀로말의 초기 상태와 목표 상태를 확인
    for i in range(n):
        # 초기 상태와 목표 상태가 다르면 초기 상태를 리스트에 추가
        if initial_state[i] != target_state[i]:
            cnt.append(initial_state[i])

    # 리스트에 아무것도 없다면 초기 상태와 목표 상태가 같은 것
    if not cnt:
        print(0)

    # 리스트에 "B"상태가 많다면 "B"의 개수만큼 작업
    elif cnt.count("B") >= cnt.count("W"):
        print(cnt.count("B"))

    # 리스트에 "W"상태가 많다면 "W"의 개수만큼 작업
    else:
        print(cnt.count("W"))
