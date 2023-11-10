from io import TextIOWrapper
from random import randrange

QUESTION_COUNT = 10

# Give user 10 questions.
# At the end give a % mark.

file: TextIOWrapper = open("resources/countriescapitals.txt")
lines: list[str] = file.readlines()

score: int = 0

for i in range (0, QUESTION_COUNT):
    random_line: int = randrange(0, len(lines));
    selection: str = lines[random_line]
    country_capital_pair: list[str] = selection.strip().split(",")

    print(f"Question {i + 1}/{QUESTION_COUNT}:")
    response: str = input(f"What is the capital of {country_capital_pair[0]}? ").lower()

    answer: str = country_capital_pair[1].lower()

    if response == answer:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer was {answer}.")
    print()

percentage: float = (score / QUESTION_COUNT) * 100
print(f"Finished! Your score was {score}/{QUESTION_COUNT} ({percentage:.1f}%)")