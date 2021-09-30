class GamePiece:
    def __init__(self, label: str = '-') -> None:
        self._label = label.lower()

    @property
    def state_value(self) -> int:
        if self._label == 'x':
            return 1
        elif self._label == 'o':
            return 2
        else:
            return 0

    def __str__(self) -> str:
        return self._label

    def __repr__(self) -> str:
        return self.__str__()
