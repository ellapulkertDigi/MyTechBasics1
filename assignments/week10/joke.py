import pyjokes
import cowsay
import jokevariance

kind_of_joke = input("Do you want to hear a kinda good joke or a kinda bad joke? Please type 'good' or 'bad': ").strip().lower()

if kind_of_joke == "good":
    cowsay.cow(pyjokes.get_joke())
elif kind_of_joke == "bad":
    cowsay.cow(jokevariance.dadjoke)
else:
    print("Now you won't hear any type of joke ):")



