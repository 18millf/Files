substring = input("Enter substring: ")
scrabble = open("resources/sowpods.txt", "r")

matches = [word.strip() for word in scrabble.readlines() if substring in word]

print(f"Found: {', '.join(matches)}")