import heapq

def solution(scoville, K):
    answer = 0

    #heapq를 이용해 scoville 리스트 heapq 화 
    #heapq => 가장 작은 수가 앞으로 오는 이진구조 // 리스트처럼 사용 가능 
    #heappush, heappop 될때마다 자동 정렬되는 특징이 있음
    #일반 리스트보다 정렬과 성능이 중요시될때 자주 사용되는듯
    heapq.heapify(scoville)
      
    #첫번째 인자가 K보다 클 경우 종료
    while scoville[0] < K :
        #K이상으로 못만들 경우 예외처리 -1
        if len(scoville) < 2 : return -1
        answer+=1
        #첫번째 작은값 + 두번째 작은값 * 2 를 scoville에 push
        heapq.heappush(scoville, (heapq.heappop(scoville) + heapq.heappop(scoville)*2))                     
    
    return answer

input1 = [1, 2, 3, 9, 10, 12]
input2 = 7
print(solution(input1,input2))