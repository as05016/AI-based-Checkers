from flask import Flask, send_from_directory, request
from flask_cors import CORS #comment this on deployment
import pprint

pp = pprint.PrettyPrinter(indent=4)

app = Flask(__name__)
CORS(app) #comment this on deployment

boardState = {'a1': None, 'a2': {'player': 'player2', 'location': 'a2', 'isKing': False}, 'a3': None, 'a4': None, 'a5': None, 'a6': {'player': 'player1', 'location': 'a6', 'isKing': False}, 'a7': None, 'a8': {'player': 'player1', 'location': 'a8', 'isKing': False}, 'b1': {'player': 'player2', 'location': 'b1', 'isKing': False}, 'b2': None, 'b3': {'player': 'player2', 'location': 'b3', 'isKing': False}, 'b4': None, 'b5': None, 'b6': None, 'b7': {'player': 'player1', 'location': 'b7', 'isKing': False}, 'b8': None, 'c1': None, 'c2': {'player': 'player2', 'location': 'c2', 'isKing': False}, 'c3': None, 'c4': None, 'c5': None, 'c6': {'player': 'player1', 'location': 'c6', 'isKing': False}, 'c7': None, 'c8': {'player': 'player1', 'location': 'c8', 'isKing': False}, 'd1': {'player': 'player2', 'location': 'd1', 'isKing': False}, 'd2': None, 'd3': {'player': 'player2', 'location': 'd3', 'isKing': False}, 'd4': None, 'd5': None, 'd6': None, 'd7': {'player': 'player1', 'location': 'd7', 'isKing': False}, 'd8': None, 'e1': None, 'e2': {'player': 'player2', 'location': 'e2', 'isKing': False}, 'e3': None, 'e4': None, 'e5': None, 'e6': {'player': 'player1', 'location': 'e6', 'isKing': False}, 'e7': None, 'e8': {'player': 'player1', 'location': 'e8', 'isKing': False}, 'f1': {'player': 'player2', 'location': 'f1', 'isKing': False}, 'f2': None, 'f3': {'player': 'player2', 'location': 'f3', 'isKing': False}, 'f4': None, 'f5': None, 'f6': None, 'f7': {'player': 'player1', 'location': 'f7', 'isKing': False}, 'f8': None, 'g1': None, 'g2': {'player': 'player2', 'location': 'g2', 'isKing': False}, 'g3': None, 'g4': None, 'g5': None, 'g6': {'player': 'player1', 'location': 'g6', 'isKing': False}, 'g7': None, 'g8': {'player': 'player1', 'location': 'g8', 'isKing': False}, 'h1': {'player': 'player2', 'location': 'h1', 'isKing': False}, 'h2': None, 'h3': {'player': 'player2', 'location': 'h3', 'isKing': False}, 'h4': None, 'h5': None, 'h6': None, 'h7': {'player': 'player1', 'location': 'h7', 'isKing': False}, 'h8': None}


@app.route("/computerMove")
def index():

    #Logic to find computerMove

    return {
        'moveTo': "e4",
        'piece': "d3"
    }

    

@app.route("/updateBoard", methods=["POST"])
def get_board_state():

    board = request.json

    pp.pprint(board)


    return {
        'response': 'OK'
    }