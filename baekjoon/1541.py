i = input().split('-')


result = []
for a in i:
    b =a.split('+')
    num = 0
    for j in b:
        num +=int(j)
    result.append(num)
d = result[0]

for c in range(1,len(result)):
     d -= result[c]

print(d)
