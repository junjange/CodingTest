n = int(input())
l = list(map(int, input().split()))
o = list(map(int, input().split()))


a= 0
result =o[0]*l[0]

for i in range(1,(n-1)):
    if o[a] <= o[i]:
        result += o[a] *l[i]
    else:
        a=i
        result += o[i]*l[i]






print(result)
