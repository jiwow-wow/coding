def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p

    return participant[-1]
        
"""
from collections import Counter


def solution(participant, completion):
    # 각 리스트의 원소 개수를 센 뒤 빼줍니다.
    answer = Counter(participant) - Counter(completion)

    # 남은 딕셔너리에서 키(이름)를 가져옵니다.
    return list(answer.keys())[0]

"""