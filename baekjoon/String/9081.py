import sys


def next_permutation(s):
    k = -1

    # 반복문을 통해 문자열의 크기를 비교한다.
    # 모든 문자가 오름차순으로 정렬되어 있다면 현재 문자가 마지막 단어인 것이다.
    for i in range(len(s) - 1):
        if s[i] < s[i + 1]:
            k = i

    # 마지막 단어라면 Flase
    if k == -1:
        return False

    # 반복문을 통해 마지막 인덱스부터 0번째 인덱스까지 s[k]보다 큰 값(s[i])을 찾아준다.
    # s[k] < s[i]를 만족하는 i를 발견했으면 m에 i를 넣어주고 바로 break를 해준다.
    for i in range(len(s) - 1, -1, -1):
        if s[k] < s[i]:
            m = i
            break

    # s[k]와 s[m]의 위치를 바꿔준 뒤, L에 s[0 : k+1]까지 넣어준다.
    # 그 뒤에 s[k+1: ]을 reverse해준 list를 extend해준뒤 L을 return해준다.
    s[k], s[m] = s[m], s[k]
    L = s[:k + 1]
    L.extend(list(reversed(s[k + 1:])))
    return L


t = int(sys.stdin.readline())
for _ in range(t):
    n = input().rstrip()
    answer = next_permutation(list(n))
    if answer:
        print(''.join(answer))
    else:
        print(n)
