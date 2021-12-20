import sys

word = str(sys.stdin.readline().strip())
target = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 크로아티아 알파벳

# 반복문을 통해 크로아티아 알파벳을 "x"로 변환
for i in target:
    word = word.replace(i, "x")

# 남은 알파벳의 개수를 출력
print(len(word))

