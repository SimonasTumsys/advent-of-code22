import csv


def get_summed_cal_list(filename: str) -> list:
    elf_list = []
    total_calories = 0
    
    with open(filename, "r") as f:
        reader = csv.reader(f)
        
        for i in reader:
            try:
                total_calories += int(i[0])
            except IndexError:
                elf_list.append(total_calories)
                total_calories = 0

    return elf_list


def sum_top_three(summed_cals: list):
    summed_cals.sort(reverse=True)
    return sum(summed_cals[0:3])

if __name__ == "__main__":

    elf_list = get_summed_cal_list("input.csv")

    print(f"Elf carrying the most calories has {max(elf_list)} calories.")

    print(f"Top three elves have {sum_top_three(elf_list)} calories")

