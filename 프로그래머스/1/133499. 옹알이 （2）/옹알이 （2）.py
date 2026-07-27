# def solution(babbling):
#     answer = 0
#     b_list =[ "aya", "ye", "woo", "ma"]
    
#     print( "yeye".replace("ye", ''))
    
#     for bab in babbling:
#         for my_b in b_list:
#             # print(bab, answer)
#             if bab == "":
#                 answer +=1
#                 break
            
            
#             if my_b in bab:
#                 bab = bab.replace(my_b, '')
#                 print(my_b, bab =="")
#             elif my_b not in bab:
#                 break



        
    
#     return answer

def solution(babbling):
    answer = 0
    possible = ["aya", "ye", "woo", "ma"]
    
    for bab in babbling:
        # 1. 연속된 같은 발음이 포함되어 있다면 바로 제외
        is_double = False
        for p in possible:
            if p * 2 in bab:
                is_double = True
                break
        if is_double:
            continue
            
        # 2. 발음 가능한 단어를 공백으로 치환
        for p in possible:
            bab = bab.replace(p, " ")
            
        # 3. 공백을 모두 제거했을 때 빈 문자열이 되면 발음 가능한 단어
        if bab.strip() == "":
            answer += 1
            
    return answer