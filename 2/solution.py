import csv

# A X - rock, 1
# B Y - paper, 2
# C Z - scissors, 3

def read_file(filename: str) -> list:
    result_list = []
    
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=" ")

        for i in reader:
            result_list.append(i)

    return result_list


def get_my_score_part1(move: str) -> int:
    if move == "X":
        return 1
    elif move == "Y":
        return 2
    elif move == "Z":
        return 3
    
    return 0


def get_score(move: str) -> int:
    if move == "A":
        return 1
    elif move == "B":
        return 2
    elif move == "C":
        return 3
    
    return 0


def play_round(opponents: str, mine: str) -> int:
    my_score = get_my_score_part1(mine)

    if opponents == "A": # rock
        if mine == "X": # rock
            return my_score + 3
        elif mine == "Y": # paper
            return my_score + 6
        elif mine == "Z": # scissors
            return my_score

    elif opponents == "B": # paper
        if mine == "X": # rock
            return my_score
        elif mine == "Y": # paper
            return my_score + 3
        elif mine == "Z": # scissors
            return my_score + 6
    
    elif opponents == "C": # scissors
        if mine == "X": # rock
            return my_score + 6
        elif mine == "Y": # paper
            return my_score
        elif mine == "Z": # scissors
            return my_score + 3
    return my_score


def get_opposite_move(is_winning: bool, opponents_move: str) -> str:
    if opponents_move == "A":
        return "B" if is_winning else "C"
    elif opponents_move == "B":
        return "C" if is_winning else "A"
    else:
        return "A" if is_winning else "B"


def according_to_plan(my_score: int, opponents_move: str, my_move: str):
    if my_move == "Z":
        return my_score + get_score(get_opposite_move(True, opponents_move))
    elif my_move == "Y":
        return my_score - 3 + get_score(opponents_move)
    else:
        return my_score - 6 + get_score(get_opposite_move(False, opponents_move))


if __name__ == "__main__":
    game_list = read_file("input.csv")

    my_part1_score = 0

    my_final_score = len(game_list) * 6

    for game in game_list:
        my_final_score = according_to_plan(my_final_score, game[0], game[1])

        my_part1_score += play_round(game[0], game[1])


    print(f"After part one, I scored a total of: {my_part1_score} points.")
    print(f"After my plan, I scored a total of {my_final_score} points.")






