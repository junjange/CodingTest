import sys


word = { "0" : "zero", "1" : "oen" , "2" : "two" , "3" : "three" , "4" : "four" , "5" : "five",  "6" : "six", "7" : "seven" , "8" : "eight" , "9" : "nine" }
m, n = map(int, sys.stdin.readline().split())

nums = []
# 반복문을 통해 m부터 n까지 수를 영어 단어로 바꾼다.
for i in range(m, n + 1):
    temp = []
    for j in str(i):
        temp.append([word[j], j])
    nums.append(temp)

# 바꾼 영어 단어를 사전순으로 정렬하기 위해 오름차순으로 정렬
nums.sort()

# 반복문을 통해 영어 단어의 수를 출력
for k in range(len(nums)):
    res = ""
    
    # 한 줄의 10개씩 출력
    if k % 10 == 0 and k != 0:
        print()
        
    for a, b in nums[k]:
        res += b
    print(res, end=" ")



