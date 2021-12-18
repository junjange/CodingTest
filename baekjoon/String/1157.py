import sys
from collections import Counter

word = list(map(str, sys.stdin.readline().strip().upper())) # 입력을 대문자로 받는다.
word = Counter(word) # Counter 함수를 통해 알파벳의 개수를 확인

# word에 알파벳의 데이터가 2개 이상 있는지 확인한다.
if len(word.most_common(2)) < 2:
    print(max(word))

else:
    # 알파벳의 개수가 제일 많은 2개의 데이터를 확인
    a, b = word.most_common(2)
    
    # 2개의 알파벳의 개수가 같으면 "?" 출력
    if a[1] == b[1]:
        print("?")
    
    # 다르다면 개수가 더 많은 알파벳을 출력
    elif a[1] > b[1]:
        print(a[0])

    else:
        print(b[0])
