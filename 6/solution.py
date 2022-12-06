import sys

def read_file(filename: str):
    with open(filename) as f:
        return f.readline()


## scan four chars, check if all unique. After scan, move one up the string. Scan.
## If all four unique - return last char index.

def scan_four_chars(input: str, start_index: int):
    result_list = []

    for i in input[start_index:start_index + 14]:
        result_list.append(i)

    start_index += 1

    if len(set(result_list)) != len(result_list):
        return scan_four_chars(input, start_index)
    else:
        return start_index + 13 

if __name__ == "__main__":
    

    sys.setrecursionlimit(4100)

    input_string = read_file("input.txt")

    print(scan_four_chars(input_string, 0))
