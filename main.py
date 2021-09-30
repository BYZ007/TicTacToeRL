from game_board.GamePiece import GamePiece
from utils.custom_types import Position
from game_board import GameBoard

if __name__ == '__main__':
    gameBoard = GameBoard.GameBoard(3)
    gameBoard.printBoard(gameBoard)

    p1 = GamePiece('x')
    pos = Position(1, 1)
    gameBoard.setBoard(pos, p1)
    gameBoard.printBoard(gameBoard)
