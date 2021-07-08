import sys

n = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))
# 추의 무게 오름차순 정렬
w.sort()
# target의 초기값(양의 정수의 최솟값은 1이기 때문)
target = 1
# 추의 무게를 더한 target과 다음 추의 무게를 비교
for i in w:
    print(target, i)
    # 추의 무게가 더 크면 그때의 target을 측정할 수 없다.
    if target < i:
        break
    # target의 추의 무게를 더해준다.
    target += i

print(target)
