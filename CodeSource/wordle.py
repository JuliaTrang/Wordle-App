import random

def loadWordList(path, length):
    with open(path, 'r', encoding = 'utf-8') as f:
        words = f.readlines()

    wordlist = []
    for w in words:
        chooseWord = w.strip().upper()
        if len(chooseWord) == length:
            wordlist.append(chooseWord)
    return wordlist

def chooseSecret(wordlist):
    if not wordlist:
        return None
    secret = random.choice(wordlist)
    return secret

def evaluateGuess(guess, secret):
    result = ["gray"] * len(guess)
    guess = guess.upper()
    secret = secret.upper()
    letterCount = {}
    for ch in secret:
        letterCount[ch] = letterCount.get(ch, 0) + 1
    for i in range(len(secret)):
        if(guess[i] == secret[i]):
            result[i] = "green"
            letterCount[guess[i]] -= 1
    for i in range(len(secret)):
        if(result[i] == "gray"):
            ch = guess[i]
            if(ch in letterCount and letterCount[ch] > 0):
                result[i] = "yellow"
                letterCount[ch] -=1
    return result

def validateGuess(guess, wordlist, length):
    guess = guess.strip().upper()
    if(len(guess) != length):
        print(f"Guess must have {length} words")
        return False
    if(guess not in wordlist):
        return False
    return True



        


        

