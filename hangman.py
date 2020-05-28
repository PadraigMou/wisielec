def hangman():

    import random

    wordind = random.randint(0, 10)
    listofwords = ["fox",
                   "cat",
                   "dog",
                   "fold",
                   "gold",
                   "mold",
                   "sold",
                   "goal",
                   "brzeczyszczykiewicz",
                   "golf"
                   ]

    word = listofwords[wordind]

    stages = ["------------",
              "|         | ",
              "|         O ",
              "|        /|\\",
              "|        / \\",
              "|           "
              ]

    board = ["_"] * len(word)
    misses = 0
    rletters = list(word)
    win = False
    
    print(" ".join(board))
    while True:
        guess = input("Input a letter.\n")
        if guess in rletters:
            cind = rletters.index(guess)
            print("That is right!")
            board[cind] = guess
            print(" ".join(board))
            rletters[cind] = "$"
        else:
            print('Wrong.')
            misses += 1
            if misses == 6:
                print("You've lost. The word is " + word)
                print("\n".join(stages[0:misses]) + "\n")
                break
        print("\n".join(stages[0:misses]) + "\n")
        if "_" not in board:
            print("You've won! It's \"" + word + "\".")
            break


hangman()
