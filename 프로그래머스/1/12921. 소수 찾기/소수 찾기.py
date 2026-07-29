def solution(n):
    answer = 0
    
    for i in range(2,n+1):
        prime = True
        for k in range(2, int(i**0.5)+1):
            if i % k == 0:
                prime = False
                break
        if prime:
            answer +=1
    
    return answer
