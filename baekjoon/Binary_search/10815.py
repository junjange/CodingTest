import sys

n = int(sys.stdin.readline())
n_list = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

# 반복문을 통해 숫자 카드를 확인
for i in m_list:
    _min = 0 # 최소 칸
    _max = n - 1 # 최대 칸
    flag = False # 상근이가 숫자 카드를 가지고 있는지에 대한 유무

    # 이분 탐색, 최소칸이 최대칸보다 커질 때까지 반복
    # 상근이의 카드중에 현재 카드가 있는지 확인
    while _min <= _max:

        mid = (_max + _min) // 2 # 상근이의 카드중에서 뽑을 카드의 칸

        # 상근이가 뽑은 카드가 현재 숫자 카드라면 1을 출력하고 반복을 멈춘다.
        if n_list[mid] == i:
            print(1, end=" ")
            flag = True
            break

        # 상근이가 뽑은 카드가 현재 숫자 카드보다 크다면 상근이의 카드 중에서 숫자가 더 작은 카드를 뽑기 위해
        # 숫자 카드의 최대 칸을 현재 뽑은 카드 칸의 -1로 초기화 한다.
        elif n_list[mid] > i:
            _max = mid - 1

        # 상근이가 뽑은 카드가 현재 숫자 카드보다 작다면 상근이의 카드 중에서 숫자가 더 큰큰 카드를 뽑기 위해
        # 숫자 카드의 최소 칸을 현재 뽑은 카드 칸의 +1로 초기화 한다.
        elif n_list[mid] < i:
            _min = mid + 1

    # 이분 탐색을 통해 상근이의 카드중에 현재 카드를 찾지 못했다면 0을 출력
    if not flag:
        print(0, end=" ")
