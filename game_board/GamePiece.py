from __future__ import annotations


class GamePiece:
    def __init__(self, label: str = '-') -> GamePiece:
        self._label = label

    @property
    def state_value(self) -> int:
        if self._label.lower() == 'x':
            return 1
        elif self._label.lower() == 'o':
            return 2
        else:
            return 0

    def __str__(self) -> str:
        return self._label.upper()

    def __repr__(self) -> str:
        return self.__str__()
