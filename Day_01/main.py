import numpy as np
import pandas as pd


def main(day_1: bool, day_2: bool):
    input = pd.read_csv("input.txt", sep="\s+", header=None)
    input_numpy = input.to_numpy()
    list_1, list_2 = np.sort(input_numpy[:, 0]), np.sort(input_numpy[:, 1])
    if day_1:
        # PART 1
        print("Part 1 solution:")
        print(np.sum(np.abs(list_1 - list_2)))
        print("\n")

    if day_2:
        # PART 2
        similiarity = 0
        for entry_1 in list_1:
            appearances = 0
            for entry_2 in list_2:
                if entry_1 == entry_2:
                    appearances = appearances + 1
            similiarity += appearances * entry_1

        print("Part 2 solution:")
        print(similiarity)


if __name__ == "__main__":
    main(True, True)