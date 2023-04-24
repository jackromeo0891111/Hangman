# Write your code here
import random
import string

print("H A N G M A N")
answers = ["python", "java", "swift", "javascript"]
options = ["play", "results", "exit"]
answer = random.choice(answers)
is_game_on = True
won = 0
lost = 0
while is_game_on:
    guessed = set()
    attempt = 0
    letters = dict({c: '-' for c in answer})
    option = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if option in options:
        if option == "play":
            while attempt <= 8:
                updated_answer = "".join(letters[c] for c in answer)
                if attempt < 8 and answer == updated_answer:
                    print(f"You guessed the word {updated_answer}!")
                    print("You survived!")
                    updated_answer = ""
                    letters = {}
                    guessed = set()
                    won += 1
                    break
                elif attempt == 8 and answer != updated_answer:
                    print("You lost!")
                    lost += 1
                    break
                else:
                    print()
                    print(updated_answer)
                    guess = input("Input a letter:")
                    if len(guess) == 1 and guess in string.ascii_lowercase:
                        if guess in guessed:
                            print("You've already guessed this letter.")
                        else:
                            if guess in letters:
                                letters[guess] = guess
                                guessed.add(guess)
                            elif guess not in letters:
                                attempt += 1
                                guessed.add(guess)
                                print("That letter doesn't appear in the word.")
                    elif len(guess) == 1 and guess not in string.ascii_lowercase:
                        print("Please, enter a lowercase letter from the English alphabet.")
                    else:
                        print("Please, input a single letter.")
        elif option == "results":
            print(f"You won: {won} times.")
            print(f"You lost: {lost} times.")
        elif option == "exit":
            is_game_on = False
            break