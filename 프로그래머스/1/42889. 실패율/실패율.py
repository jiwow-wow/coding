def solution(N, stages):
    answer = []
    
    clear_player = []
    for i in range(1, N+2):
            clear_player.append(stages.count(i))
    
    for s in range(1, N+1):
        if sum(clear_player[s-1:]) != 0:
            answer.append( clear_player[s-1] / sum(clear_player[s-1:]))
        else:
            answer.append(0)
    
    fail = list(enumerate(answer, start =1) )
    fail.sort(key =lambda x: x[1], reverse = True)
    
    
    return [s for s,f in fail ]
