# Write your code here
import random

print("H A N G M A N")
answers = ["python", "java", "swift", "javascript"]
answer = random.choice(answers)
letters = dict({c: '-' for c in answer})
for _ in range(8):
    print("\n" + "".join(letters[c] for c in answer))
    guess = input("Input a letter:")
    if guess in letters:
        letters[guess] = guess
    else:
        print("That letter doesn't appear in the word.")
print("Thanks for playing!")