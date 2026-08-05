def solution(keymap, targets):
    answer = []
    k_dic = {}
    
    for key in keymap:
        for i, k in enumerate(key):
            if k not in k_dic:
                k_dic[k] = i+1
            else:
                k_dic[k] = min(k_dic[k], i+1) 
    
    for target in targets:
        cnt = 0
        for t in target:
            
            if t in k_dic:
                cnt += k_dic[t]
            else: 
                cnt = -1
                break
        answer.append(cnt)
        
    return answer