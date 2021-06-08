from cipher import cipher_enc
from secret_bid import secret_auction
from pswd import password_generator
from hangman import hangman_game
from treasure_island import treasure
from rps import rockpaper

selection = input("enter s for thrinethra\n"
                  "enter g for games\n")


if selection == "s":
    thrinethra = input("enter p for password generator\n"
                       "enter c for cipher encryption\n"
                       "enter b for bidding\n")
    if thrinethra == "p":
        password_generator()
    elif thrinethra == "c":
        cipher_enc()
    elif thrinethra == "b":
        secret_auction()
    else:
        print("invalid command")
elif selection == "g":
    kalabhairava = input("enter h for hangman\n"
                         "enter t for treasure island game\n"
                         "enter r for rock paper scissors\n")
    if kalabhairava == "h":
        hangman_game()
    elif kalabhairava == "r":
        rockpaper()
    elif kalabhairava == "t":
        treasure()
    else:
        print("invalid command")

else:
    print("invalid prompt")
