import sys

n = int(sys.stdin.readline())
# set 자료형을 통해 중복을 제거하고 정렬을 위해 list 자료형으로 감싸준다.
word = list(set(str(sys.stdin.readline().strip()) for _ in range(n))) 
word.sort() # 오름차순 정렬
word.sort(key=lambda x: len(x)) # 단어의 길이를 기준으로 오름차순 정렬

# 반복문을 통해 단어를 출력
for i in word:
    print(i)
