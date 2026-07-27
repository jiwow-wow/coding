def solution(babbling):
    answer = 0
    b_list =[ "aya", "ye", "woo", "ma"]
        
    for bab in babbling:
        for my_b in b_list:
            if my_b*2 not in bab:
                bab=bab.replace(my_b,' ')
        if len(bab.strip())==0:
            answer +=1
    return answer
