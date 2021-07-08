import sys

n, k = map(int, sys.stdin.readline().split())
plug = list(map(int, sys.stdin.readline().split()))

# 멀티탭에 꽂혀있는 플러그
multitap = []
# 횟수
cnt = 0

for i in range(k):
    # 꽂아야하는 플러그가 멀티탭에 이미 꽂혀있으면 다음 loop를 돈다.
    if plug[i] in multitap:
        continue

    # 멀티탭에 1구라도 비어 있으면 멀티탭을 꽂고 다음 loop를 돈다.
    if len(multitap) < n:
        multitap.append(plug[i])
        continue

    # 다음에 꽂아야하는 플러그
    plug_next = []

    # 멀티탭에 모든 구를 사용하고 있을 때
    for j in range(n):

        # 멀티탭에 꽂혀 있는 플러그가 다음에 꽂아야하는 플러그중에 있는지 확인
        if multitap[j] in plug[i:]:
            # 다음에 꽂아야하는 플러그의 순서를 인덱스를 통해 확인하고 인덱스의 위치 값을 가져온다.
            # 인덱스 값을 다음에 꽂아야하는 플러그 리스트에 추가한다.
            plug_next.append(plug[i:].index(multitap[j]))

        else:
            # 멀티탭에 꽂혀 있는 플러그가 다음에 꽂아야하는 플러그중에 없으면 플러그 사용순서의 최대 범위 +1을 인덱스 값에 넣는다.
            # 인덱스 값인 101을 다음에 꽂아야하는 플러그 리스트에 추가하여 플러그를 최우선으로 뽑는다.
            plug_next.append(101)

            # 확실히 뽑아야하는 플러그가 생겼으므로 멈춰준다.
            break

    # 플러그를 인덱스 값이 큰 순서부터 뽑는다.
    del multitap[plug_next.index(max(plug_next))]
    # 다음 플러그를 꽂는다.
    multitap.append(plug[i])
    # 카운트
    cnt += 1

print(cnt)