from utils.custom_types import Position
from players import Player
from game_board.GamePiece import GamePiece
from game_board.GameBoard import GameBoard


class HumanPlayer(Player):
    def __init__(self, name: str, gamePiece: GamePiece) -> None:
        super().__init__(name, gamePiece)

    def playerMakeMove(self, gameBoard: GameBoard) -> None:
        validMove = False

        while not validMove:
            print("Please enter your move e.g: i,j ")
            i, j = input().split(',')
            pos = Position(int(i), int(j))

            if gameBoard.isMoveValid(gameBoard, pos):
                validMove = True
            else:
                print("Move not valid, please try again.")

        print(f"Moving {self._gamePiece} to {pos}")
        super().makeMove(gameBoard, pos)
