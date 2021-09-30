from players import Player
from game_board.GamePiece import GamePiece
from agent_ai import Policy


class Agent(Player):
    def __init__(
        self,
        name: str,
        gamePiece: GamePiece,
        policy: Policy
    ) -> None:

        super().__init__(name, gamePiece)
        self._policy = policy

    @property
    def policy(self) -> Policy:
        return self._policy
