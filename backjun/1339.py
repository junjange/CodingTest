n = int(input())
a=[]

for _ in range(n):
    a.append(list(map(str,input().split())))

print(a)



b = str(a[-1][-1][-1])
bb = b*10
print(bb)
print(b)
print(a[-1][-1][-1])

