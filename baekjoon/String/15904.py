import sys


word = str(sys.stdin.readline())
UCPC = ["U", "C", "P", "C"]

# 반복문을 통해 입력받은 문자열에 UCPC가 있는지 확인
for i in UCPC:

    # 문자열에 UCPC가 있으면
    if i in word:
        # 문자열을 UCPC를 찾은 이후에 리스트로 초기화
        word = word[word.index(i) + 1:]

    # 문자열에 UCPC가 없으면
    # I hate UCPC를 출력하고 종료
    else:
        print("I hate UCPC")
        exit()

# 문자열에 UCPC가 있으면 I love UCPC 출력
print("I love UCPC")
