import time
import  sys

# Typing-Effekt Funktion
def type_text(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# function for number guessing
def guessing_number():
    favorite_number = int(4)
    guess_number = int(input("I'll only tell you if you can guess my favorite number. It's below 10, that's the only hint you'll get from me. "))
    if guess_number == favorite_number:
        type_text("You're a smartypants huh?")
        return story_telling()

    elif 0 <= guess_number <= 9:
        second_guess = int(input("NOO, IT'S OBVIOUSLY WRONG. I see, you're not very smart. Let's make it easier. \n If you have 5 Apples, and Andrea, your annoying neighbour steals 3 of them, but then she feels kinda bad and returns 2 of them, how many apples do you have? \n Oh and don't be so sad about that one apple she ate, you'll get over it."))
        if second_guess == favorite_number:
            type_text("Well that was obvious. Congrats.")
            return story_telling()
        else:
            type_text("I think you're mentally not really equipped to hear my story. Wish you a wonderful day. Heads up, keep going, someday you'll be ready.")
            return False

    elif guess_number >= 10:
        type_text("Didn't I just tell you it's BELOW 10? I think you're mentally not really equipped to hear my story. Wish you a wonderful day. Heads up, keep going, someday you'll be ready.")
        return False

    elif guess_number < 0:
        third_guess = int(input("You really believe I'd have a favorite number below zero? That's psycho. I see, you're not very smart. Let's make it easier. \n If you have 5 Apples, and Andrea, your annoying neighbour steals 3 of them, but then she s and returns 2 of them, how many apples do you have? \n Oh and don't be so sad about that one apple she ate, you'll get over it."))
        if third_guess == favorite_number:
            type_text("Well that was obvious. Congrats.")
            return story_telling()
        else:
            type_text("I think you're mentally not really equipped to hear my story. Wish you a wonderful day. Heads up, keep going, someday you'll be ready.")
            return False

    else:
        type_text("What do you think 'NUMBER' means?? I think you're mentally not really equipped to hear my story. Wish you a wonderful day. Heads up, keep going, someday you'll be ready.")
        return False

# Function for the real gaming part
def story_telling():
    time.sleep(4)
    type_text("So now you want to know why I didn't prepare a game, right? Well, that's funny because...")
    time.sleep(4)
    type_text("You are playing one right now!")
    time.sleep(2)
    type_text("Yeah, let that sink in for a second, I know it might be shocking. At first I didn't believe it myself, but I guess I'm actually capable of creating my own games now!")
    time.sleep(3)
    type_text("You're wondering what's the point of this game? Well I don't know, you tell me. I guess you're supposed to win or to loose this, and considering the conversation we had so far, I sense there's no huge potential for you to win this - sorry.")
    time.sleep(3)
    rating = input("I think you can try anyways, you're probably used to failing. For you're final task, I want you to rate this game. \n And because I want to make it really easy for you, you don't even have to use numbers or letters - no, I'll give you little pictures instead. You have these to choose from: 😍👍🏻🥱😭 - but only pick one!")
    if rating == "😍":
        type_text("That's what I expected. You're totally in love with this game, you'd even name your first child after this.")
        time.sleep(3)
        type_text("That's something only true winners would do! Congratulations! And bye. Finally.")
        return False
    elif rating == "👍🏻":
        type_text("So I guess you liked it? That's nice, I would have chosen the Heart-Eyes Emoji though, I think that one is expressing the right amount of excitement.")
        time.sleep(3)
        type_text("But I'll take that thumbs up and officially announce you are a winner! Congratulations! And bye. Finally.")
        return False
    elif rating == "🥱":
        type_text("What? Do you even know what this one means?? I BORED YOU??? Well, well, well,  that's very bold to say, from someone who wanted to know my story soooooo bad. Next time someone tells you they have a secret and you don't even want to know, maybe don't ask in the first place.")
        time.sleep(4)
        type_text("Oh you're waiting for your end result? Oh sorry, I didn't want to bore you again, by saying...")
        time.sleep(3)
        type_text("YOU'RE A LOSER")
        return False
    elif rating == "😭":
        type_text("Oh, was I maybe a little to harsh on you? Well, I'm sorry, but then you should probably focus on some other games, maybe try playing some memory game or something. I don't know. But one thing is clear...")
        time.sleep(3)
        type_text("YOU'RE A LOSER")
        return False

# Game Intro and Loop
while True:
    type_text("Uh, hello, what are you doing here?? I hope you don't want to play a game right now, because I have no such thing prepared.")
    time.sleep(2)
    starter = input("Please just enter 'No game' so that we can stop this as fast as possible: ")

    if starter.lower() == "no game":
        type_text("Ah perfect, you are not here to play anything. Good Bye.")
        time.sleep(4)
        type_text("Actually, wait a sec, I have a question for you. Why didn't you want to play a game? Not that I would have had anything to offer, but I guess everybody wants to play something, right?")
        time.sleep(2)

        play_or_not = input("If hypothetically there would be some game for you to play, would you play it? Just say 'yes' or 'no': ")

        if play_or_not.lower() == "yes":
            type_text("Interesting.")
            time.sleep(3)
            type_text("Uhm, what are you waiting for? A game? I just told you I don't have any game.")
            time.sleep(2)
            type_text("Don't look at the screen like that. I have my reasons for not preparing a game. But they're a secret!")
            time.sleep(1)

            curious = input("Guess why: ")
            if curious.lower() in ["why", "why?"]:
                type_text("Ah, someone's getting curious...")
                if not guessing_number():
                    break
            else:
                curious_now = input("I said ASK ME 'WHY': ")
                if curious_now.lower() in ["why", "why?"]:
                    if not guessing_number():
                        break
                else:
                    type_text("I guess you are just a really ignorant person. Bye then.")
                    break
        else:
            type_text("Alright. You're clearly not ready for this hypothetical game anyway. Have a good one.")
            break
    else:
        type_text("Well, that's very sad, because I just wanted you to do ONE thing and you failed. Looks like even if I would have had a game, you would have failed. SO we can just end this here and now. Goodbye.")
        break
