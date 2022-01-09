import sys

n = int(sys.stdin.readline())

pattern = list(map(str, sys.stdin.readline().split("*"))) # * 기준으로 왼쪽 문자열과 오른쪽 문자열로 나눈다.
left = pattern[0].strip()  # 왼쪽 문자열
right = pattern[1].rstrip("\n") # 오른쪽 문자열

# 반복문을 통해 파일의 이름을 확인
for _ in range(n):
    file = list(map(str, sys.stdin.readline().rstrip("\n")))

    # 파일 이름의 길이가 왼쪽, 오른쪽 문자열의 기링보다 작으면 패턴이 일치 할 수 없다.
    if len(file) >= len(left) + len(right):
        
        # 왼쪽 문자열과 파일의 왼쪽 문자열만큼 자른 문자열이 같고, 오른쪽 문자열과 파일의 오른쪽 문자열만큼 자른 문자열이 같을 경우 패턴일 일치하는 것
        if left == "".join(file[:len(left)]) and right == "".join(file[len(file) - len(right):]):
            print("DA")

        else:
            print("NE")
    else:
        print("NE")
