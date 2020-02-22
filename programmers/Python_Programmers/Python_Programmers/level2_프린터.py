def solution(priorities, location):
    answer = 0
    index_pri = []
    NeedRestart = False
    #인덱스값과 우선순위값을 가진 2차원 리스트 생성 [[인덱스,우선순위]]
    for i in range(len(priorities)):
        index_pri.append([])
        index_pri[i].append(i)     
        index_pri[i].append(priorities[i])
    
    #index_pri에서 첫번째 값보다 큰 우선순위가 있을 경우 첫번째 값을 마지막에 넣고 while문 재시작
    while True :
        #print(index_pri)
        
        
        #index[0][1] 보다 더 큰 우선순위가 있는 경우 탐색
        for j in range(1,len(index_pri)):
            
            #마지막 인자일 경우 바로 인쇄
            if len(index_pri) <= 1 : break
            
            #우선순위가 더 큰 값 확인시
            if index_pri[0][1] < index_pri[j][1] :  
                #재시작 토큰 TRUE
                NeedRestart = True
                #더이상 탐색할 필요 없으므로 빠르게 탈출
                break;  
        
        #재시작 토큰 TRUE일때
        if NeedRestart == True : 
            #토큰 초기화
            NeedRestart = False
            #첫번째 값을 마지막으로 옮기기
            index_pri.append([])
            index_pri[len(index_pri)-1].append(index_pri[0][0])
            index_pri[len(index_pri)-1].append(index_pri[0][1])
            index_pri.pop(0)
            continue

        #재시작 토큰 FALSE일떄
        else :
            #print("인쇄")
            #프린트 인쇄 -> answer 값 1 증가
            answer += 1
            #이번에 인쇄하는 인덱스가 원하는 값일 경우 return
            if index_pri[0][0] == location : return answer
            #인쇄를 한 후 index_pri 0번째 값 삭제
            index_pri.pop(0)


input1 = [2, 1, 3, 2]
input2 = 2

print(solution(input1,input2))