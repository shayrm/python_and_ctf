secrt_word = "BiBi"
guess = ""
guess_count = 1
guess_limit =5
out_of_guess = False

while guess != secrt_word and not(out_of_guess):
    if guess_count <= guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guess = True  

if out_of_guess:
    print("You reach the limit, you had a limit of "  + str(guess_limit) + " guesses :-( ")
else:
    print("Nice, you manage to guess the")
    print("you guess the correct word after: " + str(guess_count -1) + " attempts!")
    