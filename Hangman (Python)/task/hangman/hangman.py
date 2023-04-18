# Write your code here
import random

print("H A N G M A N")
answers = ["python", "java", "swift", "javascript"]
answer = random.choice(answers)
updated_word = ""
hidden_word = "-" * len(answer)
print(hidden_word)
attempt = 0
while attempt < 8:
    guess = input("Input a letter:")
    if guess in answer:
        for letter in answer:
            if letter == guess:
                hidden_word = hidden_word.replace("-", letter)
            else:
                hidden_word = hidden_word.replace("-", "-")
        print(hidden_word)
        attempt += 1
    else:
        print("That letter doesn't appear in the word.")
        attempt += 1
print("Thanks for playing!")