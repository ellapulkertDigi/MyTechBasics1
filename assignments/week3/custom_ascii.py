import random
import time
import sys

def type_text(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# User Input
print("You are going to be creating a tiny weather animation.")
lines = int(input("How high is your sky supposed to be? -> min 5"))
width = int(input("How wide should your landscape be? -> min. 10 "))
weather = input("What's the weather like (rain/sun): ").lower()
faces_count = int(input("How many people are witnessing your weather?"))

# faces depending on the weather
if weather == "rain":
    face = r"\(T_T)/"
    message = "Oh no, it's raining..."
    symbol_list = ["💧", "🌧️", "☔️"]
elif weather == "sun":
    face = r"\(°‿°)/"
    message = "Yippieh, it's sunny!"
    symbol_list = ["☀️", "🌞", "🌤️"]
else:
    face = r"\(._.)/"
    message = ("What kind of weather is that...")
    symbol_list = ["?"]

face_length = len(face) + 1

# max amount of faces
max_faces = width // face_length

if faces_count > max_faces:
    print(f"Oh, that's to many people. I'll do {max_faces} instead.")
    faces_count = max_faces

# weather animation
for i in range(lines):
    line = ""
    for j in range(width):
        if random.randint(0, 5) < 4:
            line += random.choice(symbol_list)
        else:
            line += " "
    type_text(line, delay=0.005)

# building the face
faces_line = (face + " ") * faces_count
type_text(faces_line.center(width), delay=0.02)

# message
type_text(message.center(width), delay=0.04)

