def hangman_game():
    import random

    from hangman_words import word_list
    from hangman_art import logo, stages

    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    print(logo)
    
    # Testing code
    #print(f'Pssst, the solution is {chosen_word}.')

    print("hint: bike and car names")

    # Creating blanks
    display = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        if guess in display:
            print(f"you have already guessed {guess}")

        # Checking guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter

        # Checking if user is wrong.
        if guess not in chosen_word:

            print(f"you enterd {guess}, that's not in the display,so you will lose a life")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win.")

        print(stages[lives])
