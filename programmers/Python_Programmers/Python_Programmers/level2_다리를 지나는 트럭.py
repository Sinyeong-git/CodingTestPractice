def solution(bridge_length, weight, truck_weights):
    answer = 0
    brigeTruckWeight = []
    brigeTruckTime = []
    idx = 0

    #마지막 차가 들어올 때 까지 정해진 알고리즘 대로 작동
    while idx<len(truck_weights) :
        #1초 증가
        answer += 1
        #다리위에 트럭을 실을 수 있을 때 
        if sum(brigeTruckWeight) + truck_weights[idx] <= weight :
            brigeTruckWeight.append(truck_weights[idx])
            brigeTruckTime.append(0)
            idx+=1

        #다리위에 트럭에게 1초씩 지나간 시간 추가
        for j in range(len(brigeTruckTime)) :
            brigeTruckTime[j] += 1
        
        #맨 앞 트럭차가 도착하면 없애주기
        if brigeTruckTime[0] == bridge_length :
            brigeTruckTime.pop(0)
            brigeTruckWeight.pop(0)
         
    #마지막 차가 나가는 시간 추가     
    return answer + bridge_length


input1 = 2
input2 = 10
input3 = [7,4,5,6]

print(solution(input1,input2,input3))