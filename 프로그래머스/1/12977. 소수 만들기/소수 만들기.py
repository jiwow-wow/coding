""" 
성능 개선:
1. 기존풀이: 통과 (0.96ms, 11.5MB)
2. 소수 판별시 break문으로 이후 생략:	통과 (0.68ms, 11.7MB) 
현재는 리스트 안에 값이 많지 않아서 미비하지만 수가 많아질 수록 기하급수적으로 짧아질 것으로 예상

고안한 다른 풀이: 
1. nums 배열에서 최대값 3번 추출 후 nums의 조합에서 가장 큰 합을 구한다
2. 해당 합 이하의 소수를 미리 구하여 리스트에 저장
3. 3 값의 합이 리스트에 있는지 확인

조합 해결: 
1. for문 해결
2. 라이브러리 이용: from itertools import combinations
"""
def solution(nums):
    answer = 0
    sum_list = []

    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)):
            for k in range(j+1, len(nums)):
                n = nums[i]+nums[j]+ nums[k]
                sum_list.append(n)    
    
    for n in sum_list:
        is_prime = True
        for i in range(2, int(n **0.5)+1):
            if n % i ==0:
                is_prime = False
                break 
        if is_prime == True:
            answer +=1 
    return answer
