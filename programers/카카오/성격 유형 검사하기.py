def solution(survey, choices):
    answer = ''
    dic = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    n = len(survey)

    for i in range(n):
        x, y = survey[i].strip()
        if choices[i] < 4:
            dic[x] += 4 - choices[i]
        elif choices[i] > 4:
            dic[y] += choices[i] - 4

    if dic["R"] < dic["T"]:
        answer += "T"
    else:
        answer += "R"

    if dic["C"] < dic["F"]:
        answer += "F"
    else:
        answer += "C"

    if dic["J"] < dic["M"]:
        answer += "M"
    else:
        answer += "J"

    if dic["A"] < dic["N"]:
        answer += "N"
    else:
        answer += "A"

    return answer
