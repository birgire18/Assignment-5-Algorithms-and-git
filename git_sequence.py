n = int(input("Enter the length of the sequence: ")) # Do not change this line
count = 3
sequence = [1, 2, 3]
print(sequence[0])
print(sequence[1])
print(sequence[2])
while count != n:
    newnum = int(sequence[count-3]) + int(sequence[count-2]) + int(sequence[count-1])
    sequence.append(newnum)
    print(sequence[count])
    count += 1