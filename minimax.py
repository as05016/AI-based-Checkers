import math
from copy import deepcopy
from flask.globals import current_app

boardState = {'a1': None, 'a2': {'player': 'player2', 'location': 'a2', 'isKing': False}, 'a3': None, 'a4': None, 'a5': None, 'a6': {'player': 'player1', 'location': 'a6', 'isKing': False}, 'a7': None, 'a8': {'player': 'player1', 'location': 'a8', 'isKing': False}, 'b1': {'player': 'player2', 'location': 'b1', 'isKing': False}, 'b2': None, 'b3': {'player': 'player2', 'location': 'b3', 'isKing': False}, 'b4': None, 'b5': None, 'b6': None, 'b7': {'player': 'player1', 'location': 'b7', 'isKing': False}, 'b8': None, 'c1': None, 'c2': {'player': 'player2', 'location': 'c2', 'isKing': False}, 'c3': None, 'c4': None, 'c5': None, 'c6': {'player': 'player1', 'location': 'c6', 'isKing': False}, 'c7': None, 'c8': {'player': 'player1', 'location': 'c8', 'isKing': False}, 'd1': {'player': 'player2', 'location': 'd1', 'isKing': False}, 'd2': None, 'd3': {'player': 'player2', 'location': 'd3', 'isKing': False}, 'd4': None, 'd5': None, 'd6': None, 'd7': {'player': 'player1', 'location': 'd7', 'isKing': False}, 'd8': None, 'e1': None, 'e2': {'player': 'player2', 'location': 'e2', 'isKing': False}, 'e3': None, 'e4': None, 'e5': None, 'e6': {'player': 'player1', 'location': 'e6', 'isKing': False}, 'e7': None, 'e8': {'player': 'player1', 'location': 'e8', 'isKing': False}, 'f1': {'player': 'player2', 'location': 'f1', 'isKing': False}, 'f2': None, 'f3': {'player': 'player2', 'location': 'f3', 'isKing': False}, 'f4': None, 'f5': None, 'f6': None, 'f7': {'player': 'player1', 'location': 'f7', 'isKing': False}, 'f8': None, 'g1': None, 'g2': {'player': 'player2', 'location': 'g2', 'isKing': False}, 'g3': None, 'g4': None, 'g5': None, 'g6': {'player': 'player1', 'location': 'g6', 'isKing': False}, 'g7': None, 'g8': {'player': 'player1', 'location': 'g8', 'isKing': False}, 'h1': {'player': 'player2', 'location': 'h1', 'isKing': False}, 'h2': None, 'h3': {'player': 'player2', 'location': 'h3', 'isKing': False}, 'h4': None, 'h5': None, 'h6': None, 'h7': {'player': 'player1', 'location': 'h7', 'isKing': False}, 'h8': None}
allPosMoves ={   'a1': None,
    'a2': [[], None],
    'a3': None,
    'a4': None,
    'a5': None,
    'a6': [['b5'], None],
    'a7': None,
    'a8': [[], None],
    'b1': [[], None],
    'b2': None,
    'b3': [['a4', 'c4'], None],
    'b4': None,
    'b5': None,
    'b6': None,
    'b7': [[], None],
    'b8': None,
    'c1': None,
    'c2': [[], None],
    'c3': None,
    'c4': None,
    'c5': None,
    'c6': [['b5', 'd5'], None],
    'c7': None,
    'c8': [[], None],
    'd1': [[], None],
    'd2': None,
    'd3': [['c4', 'e4'], None],
    'd4': None,
    'd5': None,
    'd6': None,
    'd7': [['e6'], None],
    'd8': None,
    'e1': None,
    'e2': [[], None],
    'e3': None,
    'e4': None,
    'e5': None,
    'e6': None,
    'e7': None,
    'e8': [[], None],
    'f1': [[], None],
    'f2': None,
    'f3': [['e4', 'g4'], None],
    'f4': None,
    'f5': [['e4', 'g4'], None],
    'f6': None,
    'f7': [['e6'], None],
    'f8': None,
    'g1': None,
    'g2': [[], None],
    'g3': None,
    'g4': None,
    'g5': None,
    'g6': [['h5'], None],
    'g7': None,
    'g8': [[], None],
    'h1': [[], None],
    'h2': None,
    'h3': [['g4'], None],
    'h4': None,
    'h5': None,
    'h6': None,
    'h7': [[], None],
    'h8': None}
def minimax(board, depth, max_player, player, allPossibleMoves):
    allMoves=[]
    for piece in allPossibleMoves:
        if allPossibleMoves[piece]!=None:
            for i in range(len(allPossibleMoves[piece][0])):
                allMoves.append((piece,allPossibleMoves[piece][0][i]))
    # print(allMoves)
    if depth == 0 or is_winner(board,player) != None:
        return evaluate(board,player), board
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in allMoves:
            new_board=get_new_board(board,move)
            new_allPossibleMoves=get_all_moves(new_board,player)
            #NEED TO COMPUTE ALL MOVES FOR NEW BOARD & PASS THAT TO MINIMAX TOO
            evaluation = minimax(new_board, depth-1, False, player,new_allPossibleMoves)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in allMoves:
            new_board=get_new_board(board,move)
            new_allPossibleMoves=get_all_moves(new_board,player)
            #NEED TO COMPUTE ALL MOVES FOR NEW BOARD & PASS THAT TO MINIMAX TOO
            evaluation = minimax(new_board, depth-1, True, player,allPossibleMoves,new_allPossibleMoves)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        return minEval, best_move

def get_pieces_left(board,our_player):
    player_pieces=0
    pieces=[]
    for piece in board:
        if board[piece]!=None:
            if board[piece]['player']==our_player:
                player_pieces+=1
                pieces.append(piece)
    return player_pieces,pieces
def get_num_kings(board,our_player):
    player_kings=0
    for piece in board:
        if board[piece]!=None:
            if board[piece]['player']==our_player and (board[piece]['isKing']):
                player_kings+=1
    return player_kings
def get_total_pieces(board):
    total= 0
    for piece in board:
        if board[piece]!=None:
            total+= 1
    return total
def get_total_kings(board):
    total= 0
    for piece in board:
        if board[piece]!=None and (board[piece]['isKing']):
            total+= 1
    return total

def is_winner(board,player):
    if get_pieces_left(board,player)[0] <= 0:
        return False
    elif get_total_pieces(board)-get_pieces_left(board,player)[0] <= 0:
        return True
    return None 

def evaluate(board,our_player):
    player_pieces=get_pieces_left(board,our_player)[0]
    player_kings=get_num_kings(board,our_player)
    opponent_pieces=get_total_pieces(board)-player_pieces
    opponent_kings=get_total_kings(board)-player_kings
    return player_pieces - opponent_pieces + (player_kings * 0.5 - opponent_kings * 0.5)

# def get_valid_moves(board,piece):
#     moves=[]

#     dict={'piece': piece, 'moveTo':''}
def get_new_board(board,move):
    n_board=deepcopy(board)
    # current= move[0]
    # destination= move[1]
    # print(current,destination)
    n_board[move[1][0]]=n_board[move[0]]
    n_board[move[0]]= None
    return n_board

# needs to be implemented
def get_all_moves(board,player):
    pass

# def get_all_moves(board, player):
#     moves = []
#     for piece in get_pieces_left(board, player)[1]:
#         valid_moves = board.get_valid_moves(piece)
#         for move, skip in valid_moves.items():
#             temp_board = deepcopy(board)
#             temp_piece = temp_board.get_piece(piece.row, piece.col)
#             # new_board = simulate_move(temp_piece, move, temp_board, game, skip)
#             moves.append(new_board)
#     return moves
# def minimax(currentDepth, targetDepth,nodeIdx,maxTurn, state):
#     if (currentDepth== targetDepth):
#         return scores[nodeIdx]
#     if maxTurn:
#         return max(minimax(currentDepth+1, targetDepth ,nodeIdx*2,False,scores),minimax(currentDepth+1, targetDepth ,nodeIdx*2+1,False,scores))
#     else:
#         return min(minimax(currentDepth+1, targetDepth,nodeIdx*2,True,scores),minimax(currentDepth+1, targetDepth,nodeIdx*2+1,True,scores))
# scores = [3, 5, 2, 9, 12, 5, 23, 23]
 
# treeDepth = math.log(len(scores), 2)
 
# print("The optimal value is : ", end = "")
# print(minimax(0,treeDepth, 0, True, scores))

print(minimax(boardState,2,True,'player2',allPosMoves))