import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    day = 0
    canSupplies = []
    while stock < k :
        
        #하루 증가, stock 1 감소, k 1 감소
        day += 1
        stock -= 1
        k -= 1

        #해외 공급 가능일자가 왔을경우 그 값을 Max-min heapq로 canSupplies에 추가
        if len(dates) > 0 and day > dates[0] :         
            heapq.heappush(canSupplies,(-supplies[0],supplies[0]))
            dates.pop(0); supplies.pop(0);

        # 공급 필요시 공급
        if stock < 0 :
            stock += heapq.heappop(canSupplies)[1]
            answer += 1
        
    return answer

input1 = 4
input2 = [4,10,15]
input3 = [20,5,10]	
input4 = 30

print(solution(input1,input2,input3,input4))