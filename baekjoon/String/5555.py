import sys


word = list(map(str, sys.stdin.readline().rstrip("\n")))
n = int(sys.stdin.readline())
cnt = 0 # 찾고자하는 문자열을 포함한 반지의 개수

# 반복문을 통해 반지를 확인
for _ in range(n):
    target = list(map(str, sys.stdin.readline().rstrip("\n")))
    target += target # 반지는 시작과 끝이 연결된 상태

    # 반복문을 통해 찾고자하는 문자열이 반지에 포함되어 있는지 확인
    for i in range(20):
        if word == target[i:len(word) + i]:
            cnt += 1
            break

print(cnt)
