import sys

n, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().strip()))
stack = []

# 숫자 제거 횟수 체크
del_num = k

# 반복문을 통해 n자리까지 확인
for i in range(n):
    # 제거할 수가 있고 리스트가 있으면 반복한다.
    # i번째 수보다 작은 리스트의 끝 수를 모두 제거하기 위해서
    while del_num > 0 and stack:

        # 리스트의 끝 수와 i번째 수를 비교
        if stack[len(stack) - 1] < num[i]:

            # 리스트의 끝 수가 작으면 팝하고 숫자 제거 횟수를 -1 해준다.
            stack.pop()
            del_num -= 1

        # 리스트의 끝 수가 더 크면 멈춰준다.
        else:
            break

    # 리스트에 i번째 수를 추가한다.
    stack.append(num[i])


# 리스트에 담겨있는 수를 자릿수에서 제거할 횟수를 뺀 만큼 순서대로 출력한다.
result = ""
for i in range(n - k):
    result += str(stack[i])
print(result)
