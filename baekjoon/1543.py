doc = input()
word = input()
# 시작 인덱스
index = 0
cnt = 0
# 처음 확인하는 인덱스가 마지막에 확인해야하는 인덱스보다 작을 때까지 반복한다.
while index <= len(doc) - len(word):
    # 문서에 인덱스 시작부터 단어의 길이까지, 단어가 있는지 확인
    if doc[index:index + len(word)] == word:
        # 단어를 찾았으므로 시작 인덱스의 기준을 단어 길이만큼 더해준다.
        index += len(word)
        # 카운트한다.
        cnt += 1

    else:
        # 단어가 없으면 시작 인덱스에 1을 더해 그 다음 인덱스부터 확인한다.
        index += 1

print(cnt)
