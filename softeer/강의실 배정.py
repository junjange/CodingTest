import sys
import heapq

n = int(sys.stdin.readline())
i=[]
for _ in range(n):
    a, b = map(int,sys.stdin.readline().split())
    heapq.heappush(i, (b, a))

c=0
count =0
while i:
    a, b =heapq.heappop(i)

    if b >= c:
        count +=1
        c=a

print(count)


