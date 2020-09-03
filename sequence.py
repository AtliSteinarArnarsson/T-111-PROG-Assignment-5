n = int(input("Enter the length of the sequence: ")) # Do not change this line
sequence = []

for length in range(0, n):
    total = 0
    if length == 0:
        total = 1
    elif length == 1:
        total = length + sequence[length - 1]
    elif length == 2:
        total = sequence[length - 1] + sequence[length - 2]
    else:
        total = sequence[length - 1] + sequence[length - 2] + sequence[length - 3]
    sequence.append(total)
    print(total)