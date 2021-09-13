import sys

while True:

    n = list(map(str, sys.stdin.readline().rstrip("\n")))
    upper = 0
    lower = 0
    num = 0
    blank = 0

    # 리스트 안에 아무것도 없으면 멈춘다.
    if not n:
        break

    # 문자를 반복하여 어떤 문자인지 확인
    for i in n:
        # 대문자인지
        if i.isupper():
            upper += 1

        # 소문자인지
        elif i.islower():
            lower += 1

        # 숫자인지
        elif i.isdigit():
            num += 1

        # 공백인지
        elif i == " ":
            blank += 1

    print(lower, upper, num, blank)




