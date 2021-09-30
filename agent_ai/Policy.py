from typing import Dict, List
from utils.custom_types import Position, Qpair


class Policy:
    q_function: Dict[Qpair, int] = {}

    @classmethod
    def getBestMove(
        gameState: int,
        validMoves: List[Position]
    ) -> Position:

        best_move = None
        max_score = -float('inf')

        for pos in validMoves:
            q_pair = Qpair(gameState, pos)
            Policy.initializeState(q_pair)
            score = Policy.q_function[q_pair]

            if max_score < score:
                best_move = pos
                max_score = score

        return best_move

    @classmethod
    def initializeState(q_pair: Qpair) -> None:
        if q_pair not in Policy.q_function:
            Policy.q_function[q_pair] = 1

