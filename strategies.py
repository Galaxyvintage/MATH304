# Tit for tat
# Tit for 2 tat
# Random
# Grim Trigger
# Always cooperate

from abc import ABC, abstractmethod
import random

COOP = 0
DEFECT = 1


class Strategy(ABC):
    @property
    @abstractmethod
    def history(self):
        pass

    @abstractmethod
    def next_move(self, opponent):
        pass

    @abstractmethod
    def update_history(self, move):
        pass

    @abstractmethod
    def clear_history(self):
        pass


class TitForTat(Strategy):
    _history = []

    def next_move(self, opponent):
        nxt = COOP
        if opponent.history:
            nxt = opponent.history[-1]
        return nxt

    def update_history(self, move):
        self._history.append(move)

    def clear_history(self):
        self._history = []

    @property
    def history(self):
        return self._history


class GrimTrigger(Strategy):
    _history = []

    def next_move(self, opponent):
        nxt = COOP
        if opponent.history and DEFECT in opponent.history:
            nxt = DEFECT
        return nxt

    def update_history(self, move):
        self._history.append(move)

    def clear_history(self):
        self._history = []

    @property
    def history(self):
        return self._history


class AlwaysCoop(Strategy):
    _history = []

    def next_move(self, opponent):
        nxt = COOP
        return nxt

    def update_history(self, move):
        self._history.append(move)

    def clear_history(self):
        self._history = []

    @property
    def history(self):
        return self._history


class AlwaysDefect(Strategy):
    _history = []

    def next_move(self, opponent):
        nxt = DEFECT
        return nxt

    def update_history(self, move):
        self._history.append(move)

    def clear_history(self):
        self._history = []

    @property
    def history(self):
        return self._history


class Alternate(Strategy):
    _history = []

    def next_move(self, opponent):
        nxt = COOP
        if self.history and self.history[-1] == COOP:
            nxt = DEFECT
        return nxt

    def update_history(self, move):
        self._history.append(move)

    def clear_history(self):
        self._history = []

    @property
    def history(self):
        return self._history


class Random(Strategy):
    _history = []

    def next_move(self, opponent):
        random.seed(0)
        nxt = random.sample([COOP, DEFECT], 1)[0]
        return nxt

    def update_history(self, move):
        self._history.append(move)

    def clear_history(self):
        self._history = []

    @property
    def history(self):
        return self._history


class StrategyFactory:
    def __init__(self):
        self._builders = {}

    def register_builder(self, key, builder):
        self._builders[key] = builder

    def create(self, key, **kwargs):
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)


def main():
    factory = StrategyFactory()
    factory.register_builder('TitForTAT', TitForTat)
    factory.register_builder('AlwaysCoop', AlwaysCoop)
    tit_for_tat = factory.create("TitForTAT")
    always_coop = factory.create("AlwaysCoop")
    print(tit_for_tat.history)
    print(always_coop.history)


if __name__ == "__main__":
    main()
