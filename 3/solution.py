import csv


class Item():
    def __init__(self, letter: str, priority: int):
        self.letter = letter
        self.priority = priority

    def __repr__(self):
        return f"{self.letter}: {self.priority}"


def read_file(filename: str):
    result_list = []

    with open(filename) as f:
        reader = csv.reader(f)

        for rucksack in reader:
            result_list.append(rucksack[0])

    return result_list


def split_into_two_compartments(rucksack: str) -> list:
    ruck_size = len(rucksack)
    half_split_index = int(ruck_size / 2)
    return [rucksack[0:half_split_index], rucksack[half_split_index:ruck_size]]


def find_common_item(compartments: list):
    for i in compartments[0]:
        if i in compartments[1]:
            return i
    return


def make_alphabet(ascii_start: int, ascii_end: int) -> list:
    return list(map(chr, range(ascii_start, ascii_end)))


def map_letters_to_items() -> list:
    result_list = []
    lowercase_alphabet = make_alphabet(97, 123)
    uppercase_alphabet = make_alphabet(65, 91)

    for (letter, priority) in zip(lowercase_alphabet, range(1,27)):
        result_list.append(Item(letter, priority))

    for (letter, priority) in zip(uppercase_alphabet, range(27,53)):
        result_list.append(Item(letter, priority))

    return result_list


def group_rucksacks(rucksacks: list) -> list:
    i = 0
    result_list = []

    group_list = []

    for rucksack in rucksacks:
        group_list.append(rucksack)
        i += 1
        
        if i % 3 == 0:
            result_list.append(group_list)
            group_list = []

    return result_list


def find_badge_in_group(group: list):
    for i in group[0]:
        if i in group[1] and i in group[2]:
            return i


if __name__ == "__main__":
    rucksacks = read_file("input.csv")

    ## Part one:

    items = map_letters_to_items()
    common_items = []
    part_one_result = 0

    for rucksack in rucksacks:
        compartments = split_into_two_compartments(rucksack)
        common_items.append(find_common_item(compartments))

    for item in items:
        for common_item in common_items:
            if common_item == item.letter:
                part_one_result += item.priority

    print(f"Part one. The sum of priorities is {part_one_result}.")

    ## Part two:
    part_two_result = 0
    badges = []
    grouped_rucksascks = group_rucksacks(rucksacks)

    for group in grouped_rucksascks:
        badges.append(find_badge_in_group(group))

    for item in items:
        for badge in badges:
            if item.letter == badge:
                part_two_result += item.priority
            
        

    print(f"Part two. The sum of priorities is {part_two_result}.")
    




























