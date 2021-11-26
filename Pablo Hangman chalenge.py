import random
print(" ")
print("Welcome to Hangman!")
words = [["m","o","u","s","e"],["p","l","a","n","e"],["p","h","o","n","e"],["p","a","r","t","y"],
        ["h","o","u","s","e"],["p","h","o","t","o"],["g","l","a","s","s"],["s","h","a","r","e"],
        ["m","e","t","a","l"],["s","a","u","c","e"],["m","a","s","k","s"],["c","o","v","i","d"],
        ["w","h","a","l","e"],["m","o","n","e","y"],["o","l","i","v","e"],["a","p","p","l","e"],
        ["c","l","o","c","k"],["c","o","l","o","r"],["g","h","o","s","t"],["j","u","i","c","e"],
        ["h","a","p","p","y"],["w","a","t","e","r"],["f","r","u","i","t"],["h","o","r","s","e"],
        ["t","i","g","e","r"],["c","a","m","e","l"],["g","r","e","e","n"],["e","a","r","t","h"]]
rounds = int(input("How many rounds do you want to play?(Enter a number): "))
r = 0
while r < rounds:
    fails = 0
    a = 0
    spots = ["_", "_", "_", "_", "_"]
    currentword = random.choice(words)
    print(currentword)

    print("Round", r + 1)
    while a < 5 and fails < 15:
        if a == 0 and fails == 0:
            guess = str(input("""
_ _ _ _ _

    Guess any letter: """))
                
        else:
            guess = str(input("Guess another letter: "))
        for i in range(0,5):
            if guess in spots[i]:
                print("You already guessed", guess)  #in case the user selects again a succesful letter
            if guess in currentword[i] and guess not in spots[i]:
                spots[i]=guess
                print(spots[0],spots[1],spots[2],spots[3],spots[4])
                print("Correct!")
                a += 1
        if guess not in currentword:
            print("Incorrect")
            fails += 1
        if fails == 15:
            print("""You lose. Better luck next time
You guessed the wrong letter 15 times
The correct answer was""", currentword[0]+currentword[1]+currentword[2]+currentword[3]+currentword[4]+'.')
    r += 1
    words.remove(currentword)
print("Thanks for Playing!!!")
