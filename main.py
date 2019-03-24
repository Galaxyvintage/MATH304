from game import *
from strategies import *
from itertools import *
from collections import defaultdict
import matplotlib.pyplot as plt


def tournament(payoff_matrix, factory):
    strat_strings = ["TitForTat",  "TitForTwoTat", "GrimTrigger", "AlwaysCoop", "AlwaysDefect", "Random"]
    strats = []
    for x in strat_strings:
        fst_instance, snd_instance = factory.create(x), factory.create(x)
        strats.append((fst_instance, snd_instance))

    total_payoff = defaultdict(int)
    tft_payoff = defaultdict(tuple)

    for strat in strats:
        pd = PrisonerDilemma(payoff_matrix, strat[0], strat[1])
        payoff_a, payoff_b = pd.play()
        total_payoff[strat[0].__class__.__name__] += payoff_a

    for strat_pair in combinations(strats, 2):
        strat_a = strat_pair[0][0]
        strat_b = strat_pair[1][0]

        pd = PrisonerDilemma(payoff_matrix, strat_a, strat_b)
        payoff_a, payoff_b = pd.play()
        if strat_a.__class__.__name__ == "TitForTat":
            if strat_b.__class__.__name__ == "AlwaysDefect":
                print(payoff_a, payoff_b)
            tft_payoff[strat_b.__class__.__name__] = (payoff_a, payoff_b);
        total_payoff[strat_a.__class__.__name__] += payoff_a
        total_payoff[strat_b.__class__.__name__] += payoff_b

    print(total_payoff)
    print(tft_payoff)
    x_pos = range(len(total_payoff.keys()))
    new_x = [2 * i for i in x_pos]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    bars = ax.bar(new_x, list(total_payoff.values()), align="center")
    bars[0].set_color("orange")
    ax.set_xticks(new_x)
    ax.set_xticklabels(total_payoff.keys(), rotation=45)
    ax.set_ylabel("Total payoff")
    ax.set_title("Axelrod Tournament: 200 turns of Prisoner\'s Dilemma")
    ax.axhline(total_payoff["TitForTat"], color="grey")

    current_bar = 0
    for x, y in zip(new_x, total_payoff.values()):
        ax.text(x - bars[current_bar].get_width()/2, y*1.01, str(y), color="black",)

    fig.tight_layout()
    plt.show()




def main():
    factory = StrategyFactory()
    factory.register_builder('TitForTat', TitForTat)
    factory.register_builder('TitForTwoTat', TitForTwoTat)
    factory.register_builder('AlwaysCoop', AlwaysCoop)
    factory.register_builder("AlwaysDefect", AlwaysDefect)
    factory.register_builder("Alternate", Alternate)
    factory.register_builder("Random", Random)
    factory.register_builder("GrimTrigger", GrimTrigger)

    payoff_matrix = [[(3, 3), (0, 5)],
                     [(5, 0), (1, 1)]]
    tournament(payoff_matrix, factory)


if __name__ == "__main__":
    main();