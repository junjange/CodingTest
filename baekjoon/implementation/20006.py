import sys

p, m = map(int, sys.stdin.readline().split())
rooms = []

# 각각의 플레이어를 입력 받아 방에 넣어주기
for _ in range(p):
    l, n = input().split()
    # 최초 입력된 플레이어
    if not rooms:
        rooms.append([[int(l), n]])
        continue

    # 방에 들어갔는지 확인 하는 flag변수
    enter = False
    # 각 방을 돌면서
    for room in rooms:
        # 조건에 합당하면 넣어주기
        if len(room) < m and room[0][0] - 10 <= int(l) <= room[0][0] + 10:
            room.append([int(l), n])
            enter = True
            break
    # 못들어갔으면 새로운 방을 파서 넣어주기
    if not enter:
        rooms.append([[int(l), n]])

# 이름 기준 정렬
for room in rooms:
    room.sort(key=lambda x: x[1])

# 정원 수에 따라 출력
for room in rooms:
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
    for player in room:
        print(*player)
