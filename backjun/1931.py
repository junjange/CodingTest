n = int(input())
i=[]
for _ in range(n):
    i.append(list(map(int,input().split())))


i= sorted(i,key=lambda i: i[0])
i= sorted(i,key=lambda i: i[1])


c=0
count =0
for a,b in i:
    if a >= c:
        count +=1
        c=b

print(count)


