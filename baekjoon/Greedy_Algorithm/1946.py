import sys

test_case = int(sys.stdin.readline())

# 테스트 케이스 만큼 반복한다.
for _ in range(test_case):
    # 지원자의 수를 입력받는다.
    n = int(sys.stdin.readline())
    # 서류심사 성적과 면접시험 성적을 입력받아 서류심사 성적기준으로 정렬한다.
    test = sorted([list(map(int, sys.stdin.readline().strip().split())) for x in range(n)],
                  key=lambda x: x[0])
    # 서류심사 성적기준, 오름차순으로 정렬했기 때문에 test[0]번째 지원자는 합격이다.
    count = 1
    # 합격한 지원자 면접시험 성적 기준으로 비교한다.
    target = test[0][1]

    for i in range(1, n):
        # 합격한 지원자보다 면접시험 성적이 높으면 합격
        if test[i][1] < target:
            # 합격한 지원자에 면접시험 성적으로 바꿔준다.
            target = test[i][1]
            # 합격한 지원자 카운트
            count += 1

    print(count)

