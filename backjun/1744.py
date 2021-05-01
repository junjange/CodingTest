import sys
n = int(sys.stdin.readline())
po = []
ne = []
ze = []
sum =0
for _ in range(n):
    num = int(sys.stdin.readline())
    if num > 1:
        po.append(num)
    elif num <=0:
        ne.append(num)
    else:
        ze.append(num)

po.sort(reverse=True)
ne.sort()

print(po,ne,ze)
for i in range(len(ze)):
    sum +=ze[i]
if len(po) % 2 == 0:
    for i,j in zip(range(0,len(po),2),range(1,len(po),2)):
        sum += po[i]*po[j]
else:
    for i,j in zip(range(0,len(po),2),range(1,len(po),2)):
        sum += po[i]*po[j]
    sum += po[-1]

if len(ne) % 2 == 0:
    for i, j in zip(range(0, len(ne), 2), range(1, len(ne), 2)):
        sum += ne[i] * ne[j]
else:
    for i, j in zip(range(0, len(ne), 2), range(1, len(ne), 2)):
        sum += ne[i] * ne[j]
    sum += ne[-1]

print(sum)
