n = int(input())

p =list(map(int, input().split()))
p.sort()

result =0
x=0

for i in p:
    result = i+result
    x += result

print(x)
