def solution(board, h, w):
    answer = 0
    color_list = []
    l = len(board)
    
    if h > 0:
        color_list.append(board[h-1][w])
    if w > 0:
        color_list.append(board[h][w-1])
    if w+1 < l: 
        color_list.append(board[h][w+1])
    if h+1 < l:
        color_list.append(board[h+1][w])
        
    return color_list.count(board[h][w])