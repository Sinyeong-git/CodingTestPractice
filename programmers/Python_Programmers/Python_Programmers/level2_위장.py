from collections import Counter


def solution(clothes):
    """ 
    모든 옷의 가지수에 +1 해서 모두 곱한다음 -1 해서 리턴
    ex) a : 3 , b : 2 , c : 1 일때
    a는 안입는다, a_1 , a_2 , a_3 4가지의 선택지가 생김
    따라서 4 * 3 * 2 가 총 선택지
    하지만 모두 안입는 경우는 제한사항에 걸리기에 -1
    """  

    clothes_array = []
    answer = 1

    for i in clothes :
        clothes_array.append(i[1])

    clothes_counter = Counter(clothes_array)

    for i in clothes_counter :
        answer *= (clothes_counter[i]+1)

    return answer-1


input = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(input))