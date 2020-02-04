def solution(s):
    answer = True
    p_count = 0
    y_count = 0
    s = s.upper()

    for i in s:
        if i == "P" : p_count += 1
        elif i == "Y" : y_count += 1

    if p_count != y_count : answer = False
    return answer

s = "pPoooY"
print(solution(s))