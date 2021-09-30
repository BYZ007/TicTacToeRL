from __future__ import annotations
from utils.custom_types import Position
from game_board.GamePiece import GamePiece
from typing import List


class GameBoard:
    def __init__(self, size: int) -> None:
        self._size: int = size
        self._board: List[List[GamePiece]] = [
            [GamePiece() for _ in range(size)] for _ in range(size)
        ]
        self._is_dirty: bool = False
        self._state: int = 0

    @property
    def size(self) -> int:
        return self._size

    @property
    def board(self) -> List[List[GamePiece]]:
        return self._board

    @property
    def state(self) -> int:
        if self._is_dirty:
            self._state = self.board2state(self)
            self._is_dirty = False

        return self._state

    def setBoard(self, pos: Position, game_piece: GamePiece) -> None:
        self._board[pos.i][pos.j] = game_piece
        self._is_dirty = True

    @staticmethod
    def boardToState(gameBoard: GameBoard) -> int:
        return sum(
            [
                [
                    3 ** (i * 3 + j) * gameBoard.board[i][j]
                    for j in range(gameBoard.size)
                ]
                for i in range(gameBoard.size)
            ]
        )

    @staticmethod
    def reversedState(gameBoard: GameBoard) -> int:
        state = 0
        for i in range(gameBoard.size):
            for j in range(gameBoard.size):
                if gameBoard.board[i][j].state_value == 1:
                    state += 2 * 3 ** (i * 3 + j)

                elif gameBoard.board[i][j].state_value == 2:
                    state += 3 ** (i * 3 + j)

        return state

    @staticmethod
    def printBoard(gameBoard: GameBoard) -> None:
        for i in range(gameBoard.size):
            print(" ".join([str(piece) for piece in gameBoard.board[i]]))
        print("\n")

    @staticmethod
    def isMoveValid(gameBoard: GameBoard, pos: Position) -> bool:
        if (
            pos.i < 0
            or pos.j < 0
            or pos.i >= gameBoard.size
            or pos.j >= gameBoard.size
        ):
            return False

        if gameBoard.board[pos.i][pos.j].state_value != 0:
            return False

        return True
