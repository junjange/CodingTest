import sys

case = int(input())

for _ in range(case):
    a = int(input())
    test = sorted([list(map(int,sys.stdin.readline().strip().split()))for x in range(a)],
                  key= lambda x:x[0])

    count = 1
    min = test[0][1]
    print(test)
    print(min)

    for i in range(1,a):
        if test[i][1]<min:
            min =test[i][1]
            count+=1

    print(count)
