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

# save start, iterator and password counter for the solution
start = 50
i = 0
pw_counter = 0

# iterate for the amount of elements
while (i < len(number)): 
    # decide addition/subtraction of number based on direction
    if direct[i] == "R": start += int(number[i])
    else: start -= int(number[i])
    
    # repeat overflow fix till in valid range
    while (start < 0 or start > 99):
        if start < 0: start = 100 + start
        elif start >= 100: start = start - 100
    
    # if current value is at 0, count up for the password
    if start == 0: pw_counter += 1
    
    i += 1
    # print(f"{start}\t{pw_counter}")
    
# print result
print(f"Password is: \t{pw_counter}\n=====================\nIterations: \t{i}\nLast value: \t{direct[i-1]}{start}")