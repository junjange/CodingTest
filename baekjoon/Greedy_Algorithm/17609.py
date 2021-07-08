import sys


# 회문 판단 함수
def palindrome(s, start, end):
    # 문자열 시작부터 끝까지, 끝부터 시작까지 비교하고 크로스 되면 멈춘다.
    while start < end:
        # 문자열 시작 문자와 끝 문자가 같으면 한칸씩 가운데를 향하게 이동해 다시 비교한다.
        if s[start] == s[end]:
            start += 1
            end -= 1
        # 시작 문자와 끝 문자가 다르면 회문은 아닌 것이 되고 유사회문인지 확인해야 한다.
        else:
            # 시작 문자를 하나 제거한 케이스와 끝 문자를 하나 제거한 케이스
            # 위 두 가지 케이스를 나누어 유사회문인지 확인한다.
            case1 = pseudo_palindrome(s, start + 1, end)
            case2 = pseudo_palindrome(s, start, end - 1)

            # 두 케이스중 하나라도 True가 나오면 유사회문이다.
            if case1 == True or case2 == True:
                return 1
            # 그게 아니라면 그냥 문자열이다.
            else:
                return 2

    # 문자열 시작 문자와 끝 문자가 크로스 되고도 문자가 서로 같다면 회문이다.
    return 0


# 유사회문 판단 함수
def pseudo_palindrome(a, start, end):
    # 문자열 시작부터 끝까지, 끝부터 시작까지 비교하고 크로스 되면 멈춘다.
    while start < end:
        # 문자열 시작 문자와 끝 문자가 같으면 한칸씩 가운데를 향하게 이동해 다시 비교한다.
        if a[start] == a[end]:
            start += 1
            end -= 1
        # 시작 문자와 끝 문자가 다르면 그냥 문자열이다.
        else:
            return False

    # 문자열 시작 문자와 끝 문자가 크로스 되고도 문자가 서로 같다면 유사회문이다.
    return True


t = int(sys.stdin.readline())
for i in range(t):
    c = list(input())

    # 문자열에 시작과 끝을 확인한다.
    res = palindrome(c, 0, len(c) - 1)

    # 리턴 값 출력
    print(res)
