import sys

# read from stdin file
file_input = sys.stdin.read()

# split newlines to list
file_list = file_input.split("\n")
file_list = [item for item in file_list if item != ''] # remove '' as entry

# test case
# file_list = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

# seperate directions and numbers
direct = [item[:1] for item in file_list]
number = [item.replace("R", "").replace("L", "") for item in file_list]

# set default values
pos = 50
i = 0
pw_counter = 0

while i < len(direct):
    if direct[i] == "R": 
        for turn in range(0, int(number[i])):
            pos += 1
            if pos == 100: 
                pos = 0
                pw_counter += 1
    
    elif direct[i] == "L":
        for turn in range(0, int(number[i])):
            pos -= 1
            if pos == 0:
                pw_counter += 1
            if pos == -1: 
                pos = 99
    i += 1

print(f"Position end: {pos}, Password: {pw_counter}")