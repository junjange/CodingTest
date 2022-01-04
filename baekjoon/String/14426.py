import sys


n, m = map(int, sys.stdin.readline().split())

s = [str(sys.stdin.readline().rstrip("\n")) for _ in range(n)]
targets = [str(sys.stdin.readline().rstrip("\n")) for _ in range(m)]

# 집합 s와 m개의 문자열을 비교하기 위해 오름차순 정렬
s.sort()
targets.sort()
words = [] # 접두사가 될 수 있는 문자열 리스트

# 반복문을 통해 집합 s의 제일 큰 문자열의 앞 문자와 target 문자열의 앞 문자를 비교
for i in range(m):
    # target 문자열의 앞 문자가 더 크면 그 다음 target 문자열은 집합 s의 접두사가 될 수 없다.
    if s[-1][0] < targets[i][0]:
        break
    # 집합 s의 제일 큰 문자열의 앞 문자가 더 크면 접두사가 될 수 있으므로 words에 추가
    words.append(targets[i])

cnt = 0 # 접두사 개수

# 반복문을 통해 words의 문자열이 집합 s의 접두사인지 확인
for i in words:
    for j in s:
        # words의 문자열의 앞 문자가 집합 s의 문자열의 앞문자보다 작으면
        # 그 다음 집합 s의 문자열의 접두사가 될 수 없으므로 반복문을 멈춘다.
        if i[0] < j[0]:
            break

        # 집합 s의 문자열을 words의 문자열의 길이만큼 잘랐을 때 words의 문자열과 같다면
        # words의 문자열이 집합 s의 문자열의 접두사가 된다.
        if j[:len(i)] == i:
            cnt += 1
            break

print(cnt)
