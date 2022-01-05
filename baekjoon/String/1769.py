import sys


word = list(map(int, sys.stdin.readline().strip()))
cnt = 0 # 문제 변환 과정

# 반복문을 통해 한 자리 수가 될 때까지 문제 변환 과정을 수행
while len(word) > 1:
    cnt += 1 # 문제 변환 과정 카운트

    # 뮨제 변환 과정
    temp = []
    word = sum(word) # 각 리스트의 수를 더한다.
    # 반복문을 통해 더한 수를 자릿수에 나눠 리스트에 담는다.
    for i in str(word):
        temp.append(int(i))

    # 리스트를 word에 다시 넣는다.
    word = temp

# 문제 변환 과정 출력
print(cnt)

# 한 자리 수가 3의 배수인지 확인
if word[0] % 3 == 0:
    print("YES")
else:
    print("NO")
