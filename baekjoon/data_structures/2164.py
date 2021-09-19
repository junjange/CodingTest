import sys
from collections import deque

n = int(sys.stdin.readline())
heap = deque()

# n장의 카드를 1 부터 n 까지 번호르 매겨준다.
for i in range(1, n + 1):
    heap.append(i)

# 리스트의 크기가 1일때까지 반복한다.
while len(heap) != 1:
    heap.popleft() # 팝한다.
    heap.append(heap.popleft()) # 첫 번째 수를 맨 뒤로 옮긴다.

print(heap[0])
