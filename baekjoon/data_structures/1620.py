import sys

n, m = map(int, sys.stdin.readline().split())
book_dic = {}
book_list = []

# 포켓몬의 개수를 반복하여 포켓몬의 이름을 입력받는다.
for i in range(n):
    poketmon = sys.stdin.readline().rstrip() # 포켓몬 이름
    # 포켓몬의 이름을 딕셔너리 형과 리스트 형으로 저장한다.
    book_dic[poketmon] = i + 1
    book_list.append(poketmon)

# 문제의 개수만큼 반복한다.
for _ in range(m):    
    q = sys.stdin.readline().rstrip() # 포켓몬의 알파벳이나 번호

    # 입력받은 문제가 알파벳인지 숫자인지 구분한다.
    # 숫자라면 리스트에 (해당 숫자 - 1) 을 입력하여 출력한다.
    if q.isdigit():
        print(book_list[int(q) - 1])
    
    # 알파벳이라면 딕셔너리에 해당 알파벳을 입력하여 벨류값을 출력한다.
    else:
        print(book_dic[q])
