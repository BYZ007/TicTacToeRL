from typing import Dict, Tuple, List
from utils.custom_types import Position


class Policy:
    q_function: Dict[Tuple[int, Position], float] = {}

    def getBestMove(self, gameState: int, validMoves: List[Position]) -> Position:
        best_move = None
        max_score = -float('inf')

        for pos in validMoves:
            score = Policy.q_function[(gameState, pos)]
            if max_score < score:
                best_move = pos
                max_score = score

        return best_move


