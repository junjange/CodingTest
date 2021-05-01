import sys
n, k = map(int,sys.stdin.readline().split())

m=[]
v=[]
c=[]
for _ in range(n):

    m, v = list(map(int,sys.stdin.readline().split()))

for _ in range(k):
    c.append(int(sys.stdin.readline()))

print(n,k,m,v,c)