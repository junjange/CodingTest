import sys

t = int(sys.stdin.readline())

# 테스트 케이스만큼 반복
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    k = list(map(int, sys.stdin.readline().split()))
    heap = []

    # 문서의 중요도와 인쇄 순서를 heap에 추가
    for i in range(n):
        heap.append([k[i], i])

    cnt = 0 # 인쇄 횟수
    while True:

        # 제일 첫 번째 문서의 중요도가 제일 높을 경우
        if heap[0][0] == max(heap)[0]:
            cnt += 1 # 카운트

            # 찾고 있는 순서이면 멈춘다.
            if heap[0][1] == m:
                break

            # 찾고있는 순서가 아니라면 인쇄한다.
            heap.pop(0)

        # 제일 첫 번째 문서의 중요도가 제일 높지 않은 경우
        else:
            # 첫 번째 문서를 맨 뒤로 추가한다.
            heap.append(heap.pop(0))

    print(cnt)
