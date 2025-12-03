import sys

def is_invalid(n: str):
    list_str = list(n)
    
    first = ""
    for i in range(0, len(list_str) // 2):
        first = f"{first}{list_str[i]}"
        print(first)
        print(n[:2])
        for j in range(0, len(list_str) // 2 // len(first)):
            for z in range(0, len(list_str) // len(first)):
                if first == n[z * len(first):(z + 1) * len(first)]:
                    print("HERE")

is_invalid("11")

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