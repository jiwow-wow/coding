def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p

    return participant[-1]
        
""" 카운터로 풀이
from collections import Counter


def solution(participant, completion):
    # 각 리스트의 원소 개수를 센 뒤 빼줍니다.
    answer = Counter(participant) - Counter(completion)

    # 남은 딕셔너리에서 키(이름)를 가져옵니다.
    return list(answer.keys())[0]

"""

""" 해시함수로 풀이
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

"""