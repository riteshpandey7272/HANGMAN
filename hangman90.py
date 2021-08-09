# HANGMAN
import random
import time

name = input("What is your name: ")
print("Welcome " + name + "! Best of Luck...")
time.sleep(2)
print("Test begins now...\n")
time.sleep(2)


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_again
    secret_word = ["ball", "doll", "golf", "secret", "thief","calf", "cow", "boxer"]
    word = random.choice(secret_word)
    length = len(word)
    count = 0
    display = '*' * length
    already_guessed = []
    play_again = ""


def again_play():
    global play_again
    play_again = input("Do You want to play again? 1 = yes, 2 = no \n")
    while play_again not in ["1", "2"]:
        play_again = input("Do You want to play again? 1 = yes, 2 = no \n")
    if play_again == "1":
        main()
    elif play_again == "2":
        exit()


def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_again
    limit = 3
    guess = input("This is Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Enter a single LETTER only (Also No Numbers)\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "*" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("You have already guessed this letter. Try another letter\n")

    else:
        count += 1

        if count == 1:
            print("Wrong input. " + str(limit - count) + " guess remaining\n")
            print("   ___ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "_|_\n")

        elif count == 2:
            print("Wrong input. " + str(limit - count) + " guess remaining\n")
            print("   ___ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "_|_\n")

        elif count == 3:
            print("Wrong input. You are hanged\n")
            print("   ___ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "_|_\n")
            again_play()

    if word == '*' * length:
        print("Congrats! You have guessed it sussessfully...")
        again_play()

    elif count != limit:
        hangman()


main()


hangman()
