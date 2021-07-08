import sys
import heapq

n = int(sys.stdin.readline())
heap = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# 강의 시작시간으로 정렬한다.
heap.sort(key=lambda x: x[0])
# 강의실
room = []
# 처음 강의실에 종료시간
heapq.heappush(room, heap[0][1])

for i in range(1, n):
    # 강의실 종료시간과 다음 강의 시작시간 비교
    if room[0] > heap[i][0]:
        # 강의실 종료시간이 다음 강의 시작시간보다 크면
        # 다른 강의실에 강의를 배정해야 함으로 room 리스트에 다음 강의 종료시간을 힙푸시한다.
        heapq.heappush(room, heap[i][1])
    else:
        # 강의실 종료시간이 다음 강의 시작시간보다 작거나 같으면
        # 강의실에 종료시간을 다음 강의에 종료시간으로 바꿔준다.
        heapq.heappop(room)
        heapq.heappush(room, heap[i][1])

# 강의실 개수 출력
print(len(room))