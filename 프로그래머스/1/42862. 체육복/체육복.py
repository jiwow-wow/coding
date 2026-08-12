

def solution(n, lost, reserve):
    answer = n -len(lost)
    lost.sort() 
    reserve.sort()
    
    for l in lost[:]:
        if l in reserve:
            reserve.remove(l)
            lost.remove(l)
            answer += 1
    
    for l in lost:

        if l-1 in reserve:
            reserve.remove(l-1)
            answer +=1
        elif l+1 in reserve: 
            reserve.remove(l+1)
            answer +=1
            
    return answer