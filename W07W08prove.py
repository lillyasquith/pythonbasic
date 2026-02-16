
secret_word = "apple"
word_count = len(secret_word)
#print(word_count)


#**************************************#
#Milestone Requirements:
#**************************************#

# print ("Welcome to the word guessing game! \n")

# guess_count = 0
# guess = ""

# while guess != secret_word:
#     guess = input ("What is your guess? ")
#     guess_count += 1

#     if guess != secret_word:
#         print("Your guess was not correct.")
        
     
# print("Congratulation! You guessed it!") 
# print(f"It took you {guess_count} guesses.") 


#**************************************#
#Final Requirements
#**************************************#

guess = ""
guess_count = 0

print ("Welcome to the word guessing game! \n")

#Generate the initial hint
print("Your hint is: ", end="")
for i in secret_word:
    print("_ ", end="")

while guess != secret_word: 
    print() 
    guess = input ("What is your guess? ").lower()
    guess_count += 1

    #If length is not correct
    if len(guess) != word_count:
        print("Sorry the guess must have the same number of letters as the sescret word.")

    #The length is correct, check the guess
    elif guess != secret_word:
    #Note: If use ELSE instead of elif here, it will runs for EVERY word that is the right length... EVEN if that word is the correct answer!
        print("Your hint is: ", end="")
        for i in range(len(guess)):
            letter = guess[i]
            # print(letter, end="")
            # if letter in secret_word:
            if letter == secret_word[i]:
                print(letter.upper(), end="")
            elif letter in secret_word:
                ##NOTE: Do not use "letter in secret_word[i]"" cuz it won't work.
                print(letter.lower(), end="")
            else:
                print("_ ", end="")
#Success message:
print("Congratulation! You guessed it!") 
print(f"It took you {guess_count} guesses.") 


        