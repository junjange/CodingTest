import sys

c = sys.stdin.readline()
stack = []
# 주어진 문자열이 P이거나 PPAP이면 PPAP 출력
if c == "P" or c == "PPAP":
    print("PPAP")
else:
    # 문자열을 반복하여 문자를 확인
    for i in c:
        # 문자를 스택에 추가
        stack.append(i)

        # 스택 리스트 뒤에서 4번째까지 문자가 ["P", "P", "A", "P"]일 경우
        # 첫 번째 P만 남기고 팝한다.
        if stack[-4:] == ["P", "P", "A", "P"]:
            stack.pop()
            stack.pop()
            stack.pop()
    # 스택 리스트에 ["P", "\n"]가 있으면 모든 PPAP를 P로 바꿔준 것으로 PPAP 출력
    if stack == ["P", "\n"]:
        print("PPAP")

    # 그게 아니라면 PPAP가 아니므로 NP 출력
    else:
        print("NP")
