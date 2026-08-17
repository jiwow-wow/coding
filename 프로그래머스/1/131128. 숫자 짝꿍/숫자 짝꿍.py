"""
from collections import Counter

# 단 1번만 순회하여 각 숫자의 개수를 셈 - O(N + M)
cnt_x = Counter(X)
cnt_y = Counter(Y)

# Counter의 교집합(&) 연산: 두 객체에 모두 존재하는 요소의 최소 개수를 알아서 남김
common = cnt_x & cnt_y
"""

def solution(X, Y):
    answer = []
    num_list = [ str(i) for i in range(9,-1,-1)]
    
    for n in num_list:
        if n in X and n in Y:
            cnt = min (X.count(n), Y.count(n))
            answer.append(n * cnt)
    result = ''.join(answer)
    
    if result == '':
        return '-1'
    elif result[0] == '0':
        return '0'
    
    return result
    
