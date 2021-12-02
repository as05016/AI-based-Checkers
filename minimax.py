import math
from copy import deepcopy
# from flask.globals import current_app
import pprint

pp = pprint.PrettyPrinter(indent=4)

mapping_from_location = {}
mapping_from_coordinates = {}

boardState = {'a1': None, 'a2': {'player': 'player2', 'location': 'a2', 'isKing': False}, 'a3': None, 'a4': None, 'a5': None, 'a6': {'player': 'player1', 'location': 'a6', 'isKing': False}, 'a7': None, 'a8': {'player': 'player1', 'location': 'a8', 'isKing': False}, 'b1': {'player': 'player2', 'location': 'b1', 'isKing': False}, 'b2': None, 'b3': {'player': 'player2', 'location': 'b3', 'isKing': False}, 'b4': None, 'b5': None, 'b6': None, 'b7': {'player': 'player1', 'location': 'b7', 'isKing': False}, 'b8': None, 'c1': None, 'c2': {'player': 'player2', 'location': 'c2', 'isKing': False}, 'c3': None, 'c4': None, 'c5': None, 'c6': {'player': 'player1', 'location': 'c6', 'isKing': False}, 'c7': None, 'c8': {'player': 'player1', 'location': 'c8', 'isKing': False}, 'd1': {'player': 'player2', 'location': 'd1', 'isKing': False}, 'd2': None, 'd3': {'player': 'player2', 'location': 'd3', 'isKing': False}, 'd4': None, 'd5': None, 'd6': None, 'd7': {'player': 'player1', 'location': 'd7', 'isKing': False}, 'd8': None, 'e1': None, 'e2': {'player': 'player2', 'location': 'e2', 'isKing': False}, 'e3': None, 'e4': None, 'e5': None, 'e6': {'player': 'player1', 'location': 'e6', 'isKing': False}, 'e7': None, 'e8': {'player': 'player1', 'location': 'e8', 'isKing': False}, 'f1': {'player': 'player2', 'location': 'f1', 'isKing': False}, 'f2': None, 'f3': {'player': 'player2', 'location': 'f3', 'isKing': False}, 'f4': None, 'f5': None, 'f6': None, 'f7': {'player': 'player1', 'location': 'f7', 'isKing': False}, 'f8': None, 'g1': None, 'g2': {'player': 'player2', 'location': 'g2', 'isKing': False}, 'g3': None, 'g4': None, 'g5': None, 'g6': {'player': 'player1', 'location': 'g6', 'isKing': False}, 'g7': None, 'g8': {'player': 'player1', 'location': 'g8', 'isKing': False}, 'h1': {'player': 'player2', 'location': 'h1', 'isKing': False}, 'h2': None, 'h3': {'player': 'player2', 'location': 'h3', 'isKing': False}, 'h4': None, 'h5': None, 'h6': None, 'h7': {'player': 'player1', 'location': 'h7', 'isKing': False}, 'h8': None}

for i in boardState.keys():

    ord_num = ord(i[0])
    chr_num = ord_num - 96
    

    # [row, column]
    lst = [int(i[1]), chr_num]
    mapping_from_location[i] = lst
    mapping_from_coordinates[str(lst)] = i



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

def minimax(board, depth, max_player, player):
    allMoves= get_all_moves(board, player)

    # print(allMoves)
    if depth == 0 or is_winner(board,player) != None:
        return evaluate(board), board
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in allMoves:
            new_board = get_new_board(board,move)
            evaluation = minimax(new_board, depth-1, False, "player1")[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in allMoves:
            new_board = get_new_board(board,move)
            evaluation = minimax(new_board, depth-1, True, "player2")[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        return minEval, best_move

def minimax_with_alpha_beta(board, depth, max_player, player, alpha, beta):
    allMoves= get_all_moves(board, player)

    # print(allMoves)
    if depth == 0 or is_winner(board,player) != None:
        return evaluate(board), board
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in allMoves:
            new_board=get_new_board(board,move)
            #NEED TO COMPUTE ALL MOVES FOR NEW BOARD & PASS THAT TO MINIMAX TOO
            evaluation = minimax_with_alpha_beta(new_board, depth-1, False, 'player1', alpha, beta)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                print("pruning max")
                break
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in allMoves:
            new_board=get_new_board(board,move)
            #NEED TO COMPUTE ALL MOVES FOR NEW BOARD & PASS THAT TO MINIMAX TOO
            evaluation = minimax_with_alpha_beta(new_board, depth-1, True, 'player2', alpha, beta)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
            beta = min(beta, evaluation)
            if alpha <= beta:
                print("pruning min")
                break
        return minEval, best_move


def get_pieces_left(board,our_player):
    player_pieces=0
    pieces=[]
    for piece in board:
        if board[piece]!=None:
            if board[piece]['player']==our_player:
                player_pieces+=1
                pieces.append(piece)
    return [player_pieces, pieces]

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
    if get_pieces_left(board,player)[0] <= 0 or len(get_all_moves(board, player)) == 0:
        return False
    elif player == "player1":
        if (get_total_pieces(board)-get_pieces_left(board,player)[0]) <= 0:
            return True

        if len(get_all_moves(board, "player2")) == 0:
            return True

    elif player == "player2":
        if (get_total_pieces(board)-get_pieces_left(board,player)[0]) <= 0:
            return True

        if len(get_all_moves(board, "player1")) == 0:
            return True
    return None 

# def evaluate(board,our_player):
#     player_pieces=get_pieces_left(board,our_player)[0]
#     player_kings=get_num_kings(board,our_player)
#     opponent_pieces=get_total_pieces(board)-player_pieces
#     opponent_kings=get_total_kings(board)-player_kings
#     return player_pieces - opponent_pieces + (player_kings * 0.5 - opponent_kings * 0.5)

def evaluate(board):
    player_pieces=get_pieces_left(board,"player2")[0]
    player_kings=get_num_kings(board,"player2")
    opponent_pieces=get_total_pieces(board)-player_pieces
    opponent_kings=get_total_kings(board)-player_kings
    return player_pieces - opponent_pieces + (player_kings * 0.5 - opponent_kings * 0.5)

# def get_valid_moves(board,piece):
#     moves=[]

#     dict={'piece': piece, 'moveTo':''}
def get_new_board(board,move):
    n_board=deepcopy(board)
    if (abs(int(move[0][1])-int(move[1][1]))==2):
        diff_h = int(move[0][1])-int(move[1][1]) # -ve in right direction 2 or -2
        diff_v = mapping_from_location[move[0]][1] - mapping_from_location[move[1]][1] # -ve when moving up
        kill_row = int(move[0][1])-diff_h*0.5
        kill_col = mapping_from_location[move[0]][1] - (diff_v*0.5)
        kill_piece = mapping_from_coordinates[str([int(kill_row), int(kill_col)])]

        n_board[kill_piece] = None


    n_board[move[1]]=n_board[move[0]]
    n_board[move[0]]= None
    return n_board

# needs to be implemented
def get_all_moves(board, c_player):
    moves = []

    for i in board.keys():
        if(board[i] == None or board[i]["player"] != c_player):
            continue


        row = int(mapping_from_location[i][0])
        col = int(mapping_from_location[i][1])

        top_left = None
        top_right = None
        bottom_left= None
        bottom_right = None

        isKing = board[i]["isKing"]
        
        if(c_player == "player2" or isKing == True):
            if(col - 1 >= 1 and row + 1 <= 8):
                top_left = mapping_from_coordinates[str([row + 1, col - 1])]

                if(top_left != None and board[top_left] == None):
                    moves.append((i, top_left))
                elif(top_left != None and board[top_left] != None and board[top_left]["player"] != c_player):
                    if(col - 2 >= 1 and row + 2 <= 8):
                        kill_pos = mapping_from_coordinates[str([row + 2, col - 2])]
                        if(kill_pos != None and board[kill_pos] == None):
                            moves.append((i, kill_pos))

            if(col + 1 <= 8 and row + 1 <= 8):
                top_right = mapping_from_coordinates[str([row + 1, col + 1])]

                if(top_right != None and board[top_right] == None):
                    moves.append((i, top_right))
                elif(top_right != None and board[top_right] != None and board[top_right]["player"] != c_player):
                    if(col + 2 <= 8 and row + 2 <= 8):
                        kill_pos = mapping_from_coordinates[str([row + 2, col + 2])]
                        if(kill_pos != None and board[kill_pos] == None):
                            moves.append((i, kill_pos))

        if(c_player == "player1" or isKing == True):
            if(col - 1 >= 1 and row - 1 >= 1):
                bottom_left = mapping_from_coordinates[str([row - 1, col - 1])]

                if(bottom_left != None and board[bottom_left] == None):
                    moves.append((i, bottom_left))
                elif(bottom_left != None and board[bottom_left] != None and board[bottom_left]["player"] != c_player):
                    if(col - 2 >= 1 and row - 2 >= 1):
                        kill_pos = mapping_from_coordinates[str([row - 2, col - 2])]
                        if(kill_pos != None and board[kill_pos] == None):
                            moves.append((i, kill_pos))
            
            if(col + 1 <= 8 and row - 1 >= 1):
                bottom_right = mapping_from_coordinates[str([row - 1, col + 1])]
                if(bottom_right != None and board[bottom_right] == None):

                    moves.append((i, bottom_right))
                elif(bottom_right != None and board[bottom_right] != None and board[bottom_right]["player"] != c_player):
                    if(col + 2 <= 8 and row - 2 >= 1):
                        kill_pos = mapping_from_coordinates[str([row - 2, col + 2])]
                        if(board[kill_pos] == None):
                            moves.append((i, kill_pos))

    return moves

    
        

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

# print(minimax(boardState,2,True,'player2'))
# print(minimax_with_alpha_beta(boardState,2,True,'player2',float('-inf'), float('inf')))

# pp.pprint(get_all_moves(boardState2, "player1"))

#print(minimax(boardState,4, True,'player2'))
#print(minimax_with_alpha_beta(boardState,4,True,'player2', float('-inf'), float('inf')))