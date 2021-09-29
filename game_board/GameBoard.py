from __future__ import annotations
from utils.custom_types import Position
from GamePiece import GamePiece
from typing import List


class GameBoard:
    def __init__(self, size: int) -> GameBoard:
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

    @board.setter
    def board(self, pos: Position, game_piece: GamePiece) -> None:
        self._board[pos.i][pos.j] = game_piece
        self._is_dirty = True

    @property
    def state(self) -> int:
        if self._is_dirty:
            self._state = self.board2state(self)
            self._is_dirty = False

        return self._state

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
