from random import randint

def getRandomWord():
    words = ["jameson", "pinapple", "python", "panda", "penguin"]
    stringWord = words[randint(0, len(words) - 1)]
    word = []
    for i in stringWord:
        word.append(i)
    return word

def createSpaces(word):
    spaces = []
    for i in word:
        spaces.append("_")
    return spaces

def replaceSpaces(word, guess, spaces):
    i = 0
    while i < len(word):
        if word[i] == guess:
            spaces[i] = guess
        i += 1
    return spaces

def getGuess():
    guess = input("Enter a letter:", )
    return guess

def prettyPrint(spaces):
    for i in spaces:
        print(i, " ", end = "")

def playGame():
    word = getRandomWord()
    spaces = createSpaces(word)
    Xs = ["|   |", "|X  |", "|XX |", "|XXX|"]
    xCount = 0
    print("Welcome to the game!", "\n")
    playing = True
    prettyPrint(spaces)
    while playing:
        print("\n")
        guess = getGuess()
        if guess in word:
            replaceSpaces(word, guess, spaces)
            prettyPrint(spaces)
            print("Good guess!")
        else:
            xCount += 1
            prettyPrint(spaces)
            print("Guess again!", "\n")
            print(Xs[xCount])
        if xCount == 3 or spaces == word:
            playing = False
    if xCount == 3:
        print("\n", "You lost the game!")
    else:
        print("\n", "You won the game!")

playGame()
