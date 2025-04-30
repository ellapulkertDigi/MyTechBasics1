import time
import sys


# typing effect function
def type_text(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# intro
def intro():
    type_text(
        "Uh, hello, what are you doing here?? I hope you don't want to play a game right now, because I have no such thing prepared.")
    time.sleep(2)
    starter = input("Please just enter 'No game' so that we can stop this as fast as possible: ")
    if starter.lower() == "no game":
        type_text("Ah perfect, you are not here to play anything. Good Bye.")
        time.sleep(4)
        type_text(
            "Actually, wait a sec, I have a question for you. Why didn't you want to play a game? Not that I would have had anything to offer, but I guess everybody wants to play something, right?")
        time.sleep(2)
        return 'start'
    else:
        type_text(
            "Well, that's very sad, because I just wanted you to do ONE thing and you failed. Looks like even if I would have had a game, you would have failed. SO we can just end this here and now. Goodbye.")
        return 'end'


# asking the player to start the game
def scene_starting_game():
    play_or_not = input(
        "If hypothetically there would be some game for you to play, would you play it? Just say 'yes' or 'no': ")
    return play_or_not.lower()


# the game tests the users curiosity
def scene_getting_curious():
    type_text("Interesting.")
    time.sleep(3)
    type_text("Uhm, what are you waiting for? A game? I just told you I don't have any game.")
    time.sleep(2)
    type_text("Don't look at the screen like that. I have my reasons for not preparing a game. But they're a secret!")
    time.sleep(1)
    curious = input("Guess why: ")
    if curious.lower() in ["why", "why?"]:
        type_text("Ah, someone's getting curious...")
        return 'curious'
    else:
        curious_now = input("I said ASK ME 'WHY': ")
        if curious_now.lower() in ["why", "why?"]:
            type_text("Ah, someone's getting curious...")
            return 'curious'
        else:
            type_text("I guess you are just a really ignorant person. Bye then.")
            return 'not_curious'


# the user needs to guess a number in oder to find out why there is no game prepared
def scene_guessing_number():
    favorite_number = 4
    guess_number = int(input(
        "I'll only tell you if you can guess my favorite number. It's below 10, that's the only hint you'll get from me. "))
    if guess_number == favorite_number:
        type_text("You're a smartypants huh?")
        return 'correct'
    elif 0 <= guess_number <= 9:
        second_guess = int(input(
            "NOO, IT'S OBVIOUSLY WRONG. Let's make it easier. If you have 5 apples, and Andrea steals 3 but returns 2, how many do you have? "))
        if second_guess == favorite_number:
            type_text("Well that was obvious. Congrats.")
            return 'correct'
        else:
            type_text("I think you're mentally not really equipped to hear my story. Wish you a wonderful day.")
            return 'incorrect'
    elif guess_number < 0:
        third_guess = int(input(
            "You really believe I'd have a favorite number below zero? Let's make it easier. If you have 5 apples, and Andrea steals 3 but returns 2, how many do you have? "))
        if third_guess == favorite_number:
            type_text("Well that was obvious. Congrats.")
            return 'correct'
        else:
            type_text("I think you're mentally not really equipped to hear my story. Wish you a wonderful day.")
            return 'incorrect'
    else:
        type_text(
            "Didn't I just tell you it's BELOW 10? I think you're mentally not really equipped to hear my story. Wish you a wonderful day.")
        return 'incorrect'


# the user is told that they are actually playing a game
def story_telling():
    time.sleep(4)
    type_text("So now you want to know why I didn't prepare a game, right? Well, that's funny because...")
    time.sleep(4)
    type_text("You are playing one right now!")
    time.sleep(2)
    type_text("Yeah, let that sink in for a second, I know it might be shocking.")
    time.sleep(3)
    type_text("You're wondering what's the point of this game? Well I don't know, you tell me.")
    time.sleep(3)
    return 'continue'


# the user is asked to rate the game and can therefore win or loose
def scene_rating_game():
    rating = input("I want you to rate this game. Choose one: 😍 👍🏻 🥱 😭 : ")
    if rating == "😍":
        type_text("That's what I expected. You're totally in love with this game.")
        time.sleep(3)
        type_text("That's something only true winners would do! Congratulations! And bye. Finally.")
        return 'winner'
    elif rating == "👍🏻":
        type_text("So I guess you liked it? That's nice.")
        time.sleep(3)
        type_text(
            "I'll take that thumbs up and officially announce you are a winner! Congratulations! And bye. Finally.")
        return 'winner'
    elif rating == "🥱":
        type_text("What? Do you even know what this one means?? I BORED YOU???")
        time.sleep(4)
        type_text("YOU'RE A LOSER")
        return 'loser'
    elif rating == "😭":
        type_text("Oh, was I maybe a little to harsh on you? Well, I'm sorry.")
        time.sleep(3)
        type_text("YOU'RE A LOSER")
        return 'loser'
    else:
        type_text("Invalid input. YOU'RE A LOSER")
        return 'loser'


# Main function
def main():
    status = intro()
    if status == 'start':
        play_or_not = scene_starting_game()
        if play_or_not == 'yes':
            curiosity = scene_getting_curious()
            if curiosity == 'curious':
                guess_result = scene_guessing_number()
                if guess_result == 'correct':
                    story_status = story_telling()
                    if story_status == 'continue':
                        rating_result = scene_rating_game()
                        if rating_result == 'winner':
                            type_text("Thanks for playing! Goodbye.")
                        else:
                            type_text("Better luck next time. Goodbye.")
                else:
                    type_text("Game over. Goodbye.")
            else:
                type_text("Game over. Goodbye.")
        else:
            type_text("Alright. You're clearly not ready for this hypothetical game anyway. Have a good one.")
    else:
        type_text("Goodbye.")


if __name__ == "__main__":
    main()
