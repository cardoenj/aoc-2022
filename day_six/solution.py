import os

def find_marker(message):
    for i in range(0, len(message)):
        subset = set(message[i:i+4])
        if len(subset) == 4:
            print(f"{subset} is a marker")
            return i + 4


def find_message(message):
    start_index = find_marker(message)
    for i in range(start_index, len(message)):
        subset = set(message[i:i+14])
        if len(subset) == 14:
            print(f"{subset} is a message")
            return i + 14

message = None

with open("input.dat") as fp:
    message = fp.readline()


position_of_marker = find_marker(message)
print(position_of_marker)


position_of_message = find_message(message)
print(position_of_message)