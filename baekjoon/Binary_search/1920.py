import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))
n_list.sort() # 이분 탐색을 위해 오름차순으로 정렬

# 반복문을 통해 m개의 수들을 확인
for i in m_list:

    _min = 0 # 최댓값의 칸 수
    _max = n - 1 # 최솟값의 칸 수

    # 이분탐색을 통해 m개의 수가 A에 있는지 확인
    # 최솟값이 최댓값보다 커질때까지 반복한다.
    while _min <= _max:

        mid = (_max + _min) // 2 # 탐색하는 곳에 중간 칸 수

        # 찾는 수가 있을 경우
        if i == n_list[mid]:
            print(1)
            break

        # 찾는 수가 더 클 경우
        # 최솟값의 칸 수를 현재 비교한 칸 수에 + 1로 초기화하고 다시 탐색한다.
        elif i > n_list[mid]:
            _min = mid + 1

        # 찾는 수가 더 작을 경우
        # 최댓값의 칸 수를 현재 비교한 칸 수에 - 1로 초기화하고 다시 탐색한다.
        elif i < n_list[mid]:
            _max = mid - 1

    # 최솟값의 칸 수가 최댓값의 칸 수보다 크다면
    # 찾는 수가 리스트에 없는 것으로 0을 출력
    if _min > _max:
        print(0)


