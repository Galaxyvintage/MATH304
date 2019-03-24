class PrisonerDilemma:
    def __init__(self, payoff_matrix, strategy_a, strategy_b):
        self.payoff_matrix = payoff_matrix
        self.player_a = strategy_a
        self.player_b = strategy_b
        self.payoff_a = 0
        self.payoff_b = 0

    def play(self, turns=200):
        self.player_a.clear_history()
        self.player_b.clear_history()
        for _ in range(turns):
            move_by_a = self.player_a.next_move(self.player_b)
            move_by_b = self.player_b.next_move(self.player_a)
            self.player_a.update_history(move_by_a)
            self.player_b.update_history(move_by_b)
            # print(move_by_a, move_by_b)
            payoff = self.payoff_matrix[move_by_a][move_by_b]
            self.payoff_a += payoff[0]
            self.payoff_b += payoff[1]
        return self.payoff_a, self.payoff_b

