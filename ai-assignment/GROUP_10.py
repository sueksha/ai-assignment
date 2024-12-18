import time
from copy import deepcopy

def group1(self, board):
    possible_moves = self.getPossibleMoves(board)
    if not possible_moves or self.game.endGame:
        return 

    player, opponent = self.allPiecesLocation(board)
    
    class TimeoutException(Exception):
        pass

    def minimax(self, board, depth, max_player, alpha=float("-inf"), beta=float("inf"), end_time=None):
        if depth == 0 or self.game.endGame or not self.getPossibleMoves(board):
            return self.evaluate(board), None, None

        if time.time() > end_time:
            raise TimeoutException()

        if max_player:
            maxEval = float("-inf")
            best_start, best_end = None, None
            for pos in player:
                for move in board.get_valid_legal_moves(pos[0], pos[1], False):
                    copy_board = deepcopy(board)
                    self.moveOnBoard(copy_board, pos, move)
                    evaluation, _, _ = minimax(self, copy_board, depth-1, False, alpha, beta, end_time)
                    if evaluation > maxEval:
                        maxEval = evaluation
                        best_start, best_end = pos, move
                    alpha = max(alpha, evaluation)
                    if beta <= alpha:
                        break
            return maxEval, best_start, best_end
        else:
            minEval = float("inf")
            best_start, best_end = None, None
            for pos in opponent:
                for move in board.get_valid_legal_moves(pos[0], pos[1], False):
                    copy_board = deepcopy(board)
                    self.moveOnBoard(copy_board, pos, move)
                    evaluation, _, _ = minimax(self, copy_board, depth-1, True, alpha, beta, end_time)
                    if evaluation < minEval:
                        minEval = evaluation
                        best_start, best_end = pos, move
                    beta = min(beta, evaluation)
                    if beta <= alpha:
                        break
            return minEval, best_start, best_end

    def iterative_deepening(max_time=18, max_depth=10):
        start_time = time.time()
        end_time = start_time + max_time
        depth = 1
        best_move, best_choice = None, None

        while depth <= max_depth:
            try:
                _, move, choice = minimax(self, board, depth, True, float("-inf"), float("inf"), end_time)
                if move is not None and choice is not None:
                    best_move, best_choice = move, choice
                depth += 1
                if time.time() >= end_time:
                    break
            except TimeoutException:
                break
        return best_move, best_choice

    move, choice = iterative_deepening()
    return move, choice