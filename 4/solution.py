import csv


class Elf():
    def __init__(self, shift: str):
        self.shift = shift
        split = self.split_shift()
        self.start = int(split[0])
        self.end = int(split[1])


    def split_shift(self):
        return self.shift.split("-")


    def __repr__(self):
        return f"{self.start}-{self.end}"


def read_file(filename: str) -> list:
    result_list = []
    with open(filename, "r") as f:
        reader = csv.reader(f)

        for line in reader:
            result_list.append(line)

        return result_list


def map_elves(assignments: list) -> list:
    elves = []

    for assignment in assignments:
        elve_pair = (Elf(assignment[0]), Elf(assignment[1]))
        elves.append(elve_pair)

    return elves


def count_overlapping_shifts(elve_pairs: list) -> int:
    overlapping_shifts = 0

    for elves in elve_pairs:
        overlapping_shifts += add_fully_overlapping_shift(elves)

    return overlapping_shifts


def add_fully_overlapping_shift(elves: tuple) -> int:

    if elves[0].start >= elves[1].start and elves[0].end <= elves[1].end:
        return 1
    elif elves[1].start >= elves[0].start and elves[1].end <= elves[0].end:
        return 1

    return 0


def count_partly_overlapping_shifts(elve_pairs: list) -> int:
    total_pairs = len(elve_pairs)

    for elves in elve_pairs:
        total_pairs -= add_non_overlapping_shift(elves)

    return total_pairs


def add_non_overlapping_shift(elves: tuple) -> int:
    if elves[0].end < elves[1].start:
        return 1
    elif elves[1].end < elves[0].start:
        return 1

    return 0


if __name__ == "__main__":

    all_assignments = read_file("input.csv")
    elve_pair_list = map_elves(all_assignments)

    part_one_result = count_overlapping_shifts(elve_pair_list)
    print(f"There are {part_one_result} fully overlapping shifts")

    part_two_result = count_partly_overlapping_shifts(elve_pair_list)
    print(f"There are {part_two_result} partly overlapping shifts")

