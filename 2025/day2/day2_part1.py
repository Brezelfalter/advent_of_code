import sys

def is_invalid(n: str):
    # check if its odd, dont continue if so
    if len(n) % 2 != 0: return False
    
    list_str = list(n)
    first = ""
    second = ""
    counter = 0
    
    for i in list_str:
        if counter < len(list_str) / 2:
            first = f"{first}{i}"
        else:
            second = f"{second}{i}"
        counter += 1
    
    if first == second: 
        return True
    else: 
        return False

# read from stdin file
file_input = sys.stdin.read()

# test input
# file_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
ids = file_input.split(",")

i = 0
first = []
second = []

# get ranges start, end
while i < len(ids):
    split = ids[i].split("-")
    
    first.append(split[0])
    second.append(split[1])
    i += 1
    
# check what is invalid, add number to passwd if it is
passwd = 0
for i in range(0, len(first)):
    for x in range(int(first[i]), int(second[i]) + 1): 
        if is_invalid(str(x)) is True: 
            passwd += x


print(f"Password: {passwd}")