# These lines you can keep as is
print("Think of a number between 1 and 100 (inclusive)")
print("I am going to guess what it is")
input("Press enter when you are ready to play")

# Here you might want to initialize some variables

count = 0
guess = 50
high = 100
low = 1
# Then start a while loop
while count != 7:
    count += 1
    # These lines you can keep as is
    print("Is the number", guess, "?")
    print("Type one of the following letters and press enter:")
    print("h: if the guess is too (h)igh")
    print("l: if the guess is too (l)ow")
    print("c: if the guess is (c)orrect")
    print("q: to (q)uit the game")
    cmd = input()
    # Now it's up to you to check the command and take appropriate action
    if cmd == 'h':
        if guess <= 50:
            high = guess -1
            guess = (high + low) // 2
        elif guess >= 50:
            high = guess -1
            guess = (high + low) // 2
        continue
    elif cmd == 'l':
        if guess >= 50:
            low = guess + 1
            guess = (high + low) // 2
        elif guess <= 50:
            low = guess + 1
            guess = (high + low) // 2
        continue
    elif cmd == 'c':
        print("I AM VICTORIOUS")
        break
    elif cmd == 'q':
        print("Quitter")
        break

# If you detect that the user has not been truthful, you should print the following
else:
    print("Tsk, tsk, don't try to cheat me")
