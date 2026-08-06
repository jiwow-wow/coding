"""
다른 좋은 풀이:
1. 10을 k로 치환하여 문자열 2개를 1개로 줄임
2. 

def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)
"""

def solution(dartResult):
    num_list = []
    
    i = 0
    while ( i < len(dartResult)):
        score = 0
        
        if dartResult[i: i+2] == '10':
            score = 10
            i +=2
        else:
            score = int(dartResult[i]) 
            i +=1
        num_list.append(score)
        
        op = 0 
        if dartResult[i] =='S':
            op =1 
            i +=1
        elif dartResult[i] =='D':
            op =2
            i +=1
        elif dartResult[i] =='T':
            op =3
            i +=1
        num_list.append(num_list.pop()**op)
        
        if i <len(dartResult):
            if dartResult[i] =='#':
                num_list.append(num_list.pop()*(-1))
                i += 1
            elif dartResult[i] =='*':
                if len(num_list) >= 2:
                       num_list[-2] *= 2
                num_list[-1] *= 2
                i += 1
    
    return sum(num_list)
        

"""
import re

pattern = re.compile(r"([0-9]|10)([SDT])([*#]?)")
matches = pattern.findall(dartResult)
"""