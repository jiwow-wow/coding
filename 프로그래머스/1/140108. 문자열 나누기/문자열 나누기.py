def solution(s):
    answer = 0
        
    while(s !=''):
        first_c = s[0]
        cnt = 0 
        cnt_n =0
        divided = False
        
        for i,c in enumerate(s):

            if c == first_c:
                cnt += 1
            else:
                cnt_n +=1

            if cnt_n == cnt:
                s = s[cnt*2:]
                divided = True
                break
                
        if not divided:
            s = ''
                
        answer+=1
    
    return answer