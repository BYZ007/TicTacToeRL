import abc
from game_board.GamePiece import GamePiece
from game_board.GameBoard import GameBoard
from utils.custom_types import Position


class Player(abc.ABC):
    def __init__(self, name: str, gamePiece: GamePiece) -> None:
        self._gamePiece = gamePiece
        self._name = name

    @property
    def gamePiece(self) -> GamePiece:
        return self._gamePiece

    @property
    def name(self) -> str:
        return self._name

    def makeMove(self, gameBoard: GameBoard, pos: Position) -> None:
        if GameBoard.isMoveValid(gameBoard, pos):
            gameBoard.setBoard(pos, self._gamePiece)
