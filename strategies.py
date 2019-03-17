# Tit for tat
# Tit for 2 tat
# Random
# Grim Trigger
# Always cooperate

from abc import ABC, abstractmethod

COOP = 0
DEFECT = 1


class Strategy(ABC):
    _history = []
    @abstractmethod
    def next_move(self, opponent):
        pass

    @property
    def history(self):
        return self._history


class TitForTat(Strategy):
    def next_move(self, opponent):
        nxt = COOP
        if DEFECT in opponent.get_history():
            nxt = DEFECT
        self._history.append(nxt)
        return nxt


class AlwaysCoop(Strategy):
    def next_move(self, opponent):
        nxt = COOP
        self._history.append(nxt)
        return nxt


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
    TFT = factory.create("TitForTAT")
    AC = factory.create("AlwaysCoop")
    print(TFT.history)
    print(AC.history)


if __name__ == "__main__":
    main()