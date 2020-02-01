def solution(arr):
    answer = []


    for i in arr:
        #[-1] 과는 다르게 [-1:]은 리스트 값으로 출력해줌, NULL값이여도 오류가 없음
        #리스트 형식으로 나오기에 비교대상 i 도 [i]로 작성
        if answer[-1:] == [i] : continue
        answer.append(i)    
    return answer

arr = [1,1,3,3,0,1,1]

print(solution(arr))