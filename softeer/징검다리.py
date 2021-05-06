import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
result=[1]*n

for i in range(1, n):
    result_max = 0
  

    for j in range(i):
     
        if a[i] > a[j]:
            if result_max<result[j]:
                result_max=result[j]
    result[i] =result_max+ 1

print(max(result))
