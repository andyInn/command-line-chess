from Board import Board
from Pawn import Pawn
from Rook import Rook
from King import King
from Queen import Queen
from Bishop import Bishop
from Knight import Knight
from Coordinate import Coordinate as C
from Move import Move
from Piece import Piece
from AI import AI
from InputParser import InputParser
import time
import sys

WHITE = True
BLACK = False


#print("What side would you like to play as?")
#chosenSide = input()
#if 'w' in chosenSide.lower() :
    #side = WHITE
#else :
    #side = BLACK

#chosenSide = WHITE


for _ in range(1) : 
    moves = 0
    board = Board()
    print(board)
    #for move in board.getAllMovesLegal(board.currentSide) :
        #print(move)
    parser = InputParser(board, WHITE)
    blackai = AI(board, BLACK, 2)
    whiteai = AI(board, WHITE, 2)
    for _ in range(50) :
        move = None
        if board.currentSide == WHITE :
            move = whiteai.getRandomMove()
        else :
            move = blackai.getRandomMove() 

        move.notation = parser.notationForMove(move)

        print("MOVE: " + str(move.notation))
        board.makeMove(move)
        moves += 1
        print(board)
        #print(board.getPointAdvantageOfSide(board.currentSide))
        if board.isCheckmate() :
            #print("MOVES : " + str(moves))
            #print("CHECKMATE!")
            break
