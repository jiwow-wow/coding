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
    elif result[0] == '0' :
        return '0'
    
    return result
    
    
    
    
    
    
#     set_x = set(X)
#     set_y = set(Y)
#     set_xy = set_y - set_x
    
#     list_answer = list(Y)
    
#     for num in set_xy:
#         list_answer.remove(num)

#     if len(list_answer) == 0:
#         return '-1'
    
#     list_answer.sort(reverse =True)
    
#     return str(int(''.join(list_answer)))
