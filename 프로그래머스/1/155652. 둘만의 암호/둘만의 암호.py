def solution(s, skip, index):
    answer = ''
    skip_ord_list = list(map(ord, skip))

    for ch in s:
        ch_to_int = ord(ch)
        cnt = 0
        
        while cnt < index:
            ch_to_int += 1
            if ch_to_int > ord('z'):
                ch_to_int = ord('a')
            if ch_to_int in skip_ord_list:
                continue
            cnt += 1

        answer += chr(ch_to_int)

    return answer

"""
#a~z를 set 에 담는 게 느릴줄 알았지만 이후 for 문이 1개라서 훨씬 빠르다는 것을 알았음
#밑에 풀이 해설: a~z를 set 에 담고 skip할 문자를 미리 제거, 이후 딕셔너리에 담고  

from string import ascii_lowercase

def solution(s, skip, index):
    result = ''

    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    l = len(a_to_z)

    dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}

    for i in s:
        result += a_to_z[(dic_alpha[i] + index) % l]

    return result
"""