def solution(heights):
    answer = []
    isAppend = False

    #1차 for문 시작
    for i in range(len(heights)-1,-1,-1):
        #2차 for문 시작
        for j in range(i-1,-1,-1):
            print("J : ",j)
            #I 값의 탑을 기준으로 왼쪽으로 탐색, 더 큰 탑이 존재한다면 그 탑의 인덱스를 리스트 처음에 삽입
            if heights[i] < heights[j] : answer.insert(0,j+1); isAppend = True; break;            
        #탑이 존재하지 않을경우 0값을 넣어주기 위한 루틴
        if isAppend == False : answer.insert(0,0);  
        isAppend = False
    return answer
    
#1회차
# 4,3,2,1 0
# 3 2 1 0
# 2회차
# 3 2 1 0
# 2 1 0

input1 = [6,9,5,7,4]
#input1 = [3,9,9,3,5,7,2]

print(solution(input1))