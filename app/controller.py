from flask import render_template, request
from app import app
from app.models.player import *
from app.models.game import *

@app.route('/')
def index():
    return "Play rock, paper, scissors"

@app.route('/<choice1>/<choice2>')
def play_game(choice1, choice2):
    # return choice1 + choice2
    player1 = Player("Alex", choice1)
    player2 = Player("John", choice2)
    game = Game(player1, player2)
    game.compare_choices()
    if player1.winner:
        return "Player1 is the winner"
    elif player2.winner:
        return "Player2 is the winner"
    return "It is a tie"



    

    
