def solution(progresses, speeds):
    answer = []

    while True :          
        #디버깅용 print
        #print(progresses,speeds)

        #작업목록이 없을경우 탈출
        if len(progresses) == 0 : break

        #완료 작업 카운터
        f_counter = 0

        for i in range(len(progresses)) :       
            #prgoresses에 작업량 추가
            progresses[i] += speeds[i]

        #첫번째 작업이 끝났을때
        if progresses[0] > 100:
            for i in range(len(progresses)) :                    
                #중간에 100%미만 작업이 껴있을경우 break
                if progresses[i] < 100 : break;
                #100프로 이상이 된 작업 체크
                if progresses[i] > 100 :  f_counter += 1

        #완료된 작업 만큼 answer추가,progresses 제거
        if f_counter > 0 : 
            answer.append(f_counter)
            for i in range(f_counter) :
                progresses.pop(0)
                speeds.pop(0)
        
    return answer



input1 = [93,30,55]
input2 = [1,30,5]

print(solution(input1,input2))