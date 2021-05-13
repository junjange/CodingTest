n = int(input())
array =[500,100,50,10,5,1]
i = 1000-n
count =0

for j in array:
    count += i // j
    i%=j
    if i==0:
        break
print(count)