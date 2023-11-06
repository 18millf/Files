from random import randrange

file = open("resources/countriescapitals.txt")
lines = file.readlines()

random_line = randrange(0, len(lines));
selection = lines[random_line]

arr = selection.split(",")

answer = input(f"What is the capital of {arr[0]}? ")
if answer.lower() == arr[1].lower().strip():
    print("Well done, you got it right!")
else:
    print(f"Incorrect answer, the correct answer is {arr[1]}")