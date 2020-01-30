def solution(answers):

    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]

    answer = []

    correct_score = [0,0,0]
         
    for i in range(len(answers)):
        if answers[i] == pattern1[i % 5]: 
            correct_score[0] += 1 
        if answers[i] == pattern2[i % 8]: 
            correct_score[1] += 1 
        if answers[i] == pattern3[i % 10]: 
            correct_score[2] += 1 
    
    winner_score = max(correct_score)


    for i in range(3):
        if correct_score[i] == winner_score:
            answer.append(i + 1)

    return answer



input = [1,2,3,4,5]

print(solution(input))

