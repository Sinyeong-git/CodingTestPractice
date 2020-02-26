
#str 3번 반복해서 돌려줌 ex) 30 -> 303030
def whatisfirst(n):
    return n*3

def solution(numbers):
   
    numbers = list(map(str,numbers))
    answer = ''

    '''
    9,3,30 일때 9 , 3 , 30 순으로 정렬
    303 보단 330 이 더 크기에 위 정렬순서로 가야댐

    str*3한 값을 key로 해서 정렬
    3 과 30 를 예로 들면 333, 303030 으로 비교하게됨
    str 비교는 앞에서 부터 작은게 먼저 뒤로 가기때문에 333>303030 판정이 됨
    '''

    numbers.sort(reverse = True ,key=whatisfirst)

    #0000 같은 경우 0 으로 출력하기 위해서
    if numbers[0] == "0" : return str(0);

    for i in numbers :
        answer = answer + i
    
    return answer

#input1 = [3, 30, 34, 5, 9]
input1 = [0,0,0,0]

print(solution(input1))