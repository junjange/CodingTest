def solution(progresses, speeds):
    answer = []

    while progresses:
        progresses = [x + y for x, y in zip(progresses, speeds)]
        cnt = 0

        while progresses[0] >= 100:
            del progresses[0]
            del speeds[0]
            cnt += 1
            if not progresses:
                break
        if cnt:
            answer.append(cnt)

    return answer
