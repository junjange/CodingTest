import heapq

def solution(jobs):
    answer: int = 0
    n = 0
    start = -1
    now = 0
    heap = []
    while n < len(jobs):

        for i in jobs:
            if start < i[0] <= now:
                heapq.heappush(heap, [i[1], i[0]])

        if len(heap) > 0:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1]  # 작업 요청시간부터 종료시간까지 계산
            n += 1

        else:
            now += 1


    return answer // len(jobs)
