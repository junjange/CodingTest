import sys

cnt = [] # FBI 요원의 번호

# 반복문을 통해 5명의 첩보원명을 확인
for i in range(5):
    word = list(map(str, sys.stdin.readline().strip()))
    # 반복문과 조건문을 통해 FBI 요원을 찾는다.
    for j in range(len(word) - 2):
        # FBI 요원을 찾으면 해당 번호를 cnt 에 추가하고 반복을 멈춘다.
        if word[j] == "F" and word[j + 1] == "B" and word[j + 2] == "I":
            cnt.append(i + 1) 
            break

# cnt 가 있으면 FBI 요원이 있는 것으로 FBI 요원의 번호를 출력
if cnt:
    print(*cnt)
else:
    print("HE GOT AWAY!")
