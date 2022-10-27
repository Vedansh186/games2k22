
import random 
import time



print("Hello and Welcome to this GAme of HAngman developed by Vedansh Sharma\n")
name = input("enter your in game name pls\n")
print("hello "+name+" and welcome to the game. its about to begin\n")
time.sleep(2)
print("lets start\n")
time.sleep(3)


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"
                   ,"plants", "flabbergasted", "exasperated", "aditya", "Dimwitted"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""


def play_again():
    global play_game
    print("do you want to play again ? Y for yes N for no\n")
    play_game = input()
    while play_game not in ['y', 'Y', 'n', 'N']:
        print("do you want to play again ? Y for yes N for no\n")
    play_game = input()
    if(play_game == 'y' or play_game =='Y'):
        main()
    elif(play_game == 'n' or play_game == 'n'):
        print("thank you for playing\n")
        exit()
    
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    print("word is:" + display)
    guess = input("enter your choice\n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid. Try a Letter\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Already guessed\n")

    else:
        count+=1
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_again()

    if word == '_'*length:
        print("congrats youve guessed the word right\n")
        play_again()
    elif count != limit:
        hangman()


main()


hangman()