#Page 222
#Q2

filename = input("Input file: ")
file = open(filename, "r")

lines = file.readlines()

for i in range (0, len(lines)):
    print(f"{i+1}    {lines[i].strip()}")

file.close()