import numpy as np
import pandas as pd


def main(day_1: bool, day_2: bool):
    report = []
    with open("input.txt", 'r') as input:
        for line in input:
            report.append(np.fromstring(line, dtype=int,  sep=' '))
    if day_1:
        # PART 1
        safe_reports = 0
        for entry in report:
            safe = True
            diff_prev = 1
            for i in range(len(entry)-1):
                diff = entry[i] - entry[i+1]
                if diff_prev*diff <= 0 or (diff < 1 or diff > 3):
                    safe = False
                    break
                diff_prev = diff
            if safe:
                print(entry)
                safe_reports += 1

        print("Part 1 solution:")
        print(safe_reports)
        print("\n")

    if day_2:
        # PART 2

        print("Part 2 solution:")
        print()


if __name__ == "__main__":
    main(True, False)