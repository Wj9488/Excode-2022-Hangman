import requests


def play_hangman():
    res = requests.get("https://random-word-api.herokuapp.com/word").text
    word = res.translate({ord(i): None for i in '[""]'})
    word_letters = ["_"] * len(word)
    used_letters = []
    lives = 6

    while True:
        print("Current word: ", " ".join(word_letters))
        print("Used letters: ", " ".join(used_letters))
        print("Lives remaining: ", lives)

        guess = input("Enter a letter or type 'exit' to quit: ")
        if guess == "exit":
            break
        elif guess in used_letters:
            print("You have already used that letter. Try again.")
            continue
        elif guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    word_letters[i] = guess
            if "_" not in word_letters:
                print("Congratulations! You have won the game!")
                print("The word was: ", word)
                break
        else:
            lives -= 1
            if lives == 0:
                print("You have lost the game. Better luck next time!")
                print("The word was: ", word)
                break
            else:
                print("That letter is not in the word. Try again.")
        used_letters.append(guess)


play_hangman()
