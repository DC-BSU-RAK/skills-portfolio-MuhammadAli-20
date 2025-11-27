from tkinter import *
import random
from PIL import ImageTk, Image
import pyttsx3
import threading
import pygame

# ---------- MAIN WINDOW ----------
root = Tk()
root.geometry("650x500")
root.title("Random Joke Game")

# ---------- INITIALIZE PYGAME ----------
pygame.mixer.init()

# ---------- BACKGROUND IMAGE ----------
bg_image = Image.open("funny.png")
bg_image = bg_image.resize((650, 500))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(root, image=bg_photo)
bg_label.image = bg_photo
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ---------- GLOBAL LOCK (prevents overlapping TTS) ----------
speech_lock = threading.Lock()

# ---------- PLAY LAUGHING SOUND ----------
def play_laughing_man_sound():
    pygame.mixer.music.load("laughing_man.mp3")
    pygame.mixer.music.play()

# ---------- STABLE SPEAK FUNCTION WITH CALLBACK ----------
def speak(text, after_speech=None):
    def run_tts():
        with speech_lock:
            engine = pyttsx3.init()
            engine.setProperty("rate", 175)
            engine.say(text)
            engine.runAndWait()
            engine.stop()

        # Call the callback AFTER speaking (if provided)
        if after_speech:
            after_speech()

    threading.Thread(target=run_tts, daemon=True).start()

# ---------- LABELS ----------
setup_label = Label(root, text="", font=("Arial", 14), bg="#FFF8ED", width=50)
setup_label.place(x=60, y=120)

punchline_label = Label(root, text="", font=("Arial", 14), bg="#FFF8ED", width=50)
punchline_label.place(x=60, y=150)

# ---------- JOKE GAME CLASS ----------
class JokeGame:
    def __init__(self, root):
        self.root = root

        self.jokes = [
            ("Why did the chicken cross the road?", "To get to the other side."),
            ("What happens if you boil a clown?", "You get a laughing stock."),
            ("Why did the car get a flat tire?", "Because there was a fork in the road!"),
            ("How did the hipster burn his mouth?", "He ate his pizza before it was cool."),
            ("What did the janitor say when he jumped out of the closet?", "SUPPLIES!!!!"),
            ("Have you heard about the band 1023MB?", "It's probably because they haven't got a gig yet…"),
            ("Why does the golfer wear two pants?", "Because he's afraid he might get a hole-in-one."),
            ("Why should you wear glasses to maths class?", "Because it helps with division."),
            ("Why does it take pirates so long to learn the alphabet?", "Because they could spend years at C."),
            ("Why did the woman go on the date with the mushroom?", "Because he was a fun-ghi."),
            ("Why do bananas never get lonely?", "Because they hang out in bunches."),
            ("What did the buffalo say when his kid went to college?", "Bison."),
            ("Why shouldn't you tell secrets in a cornfield?", "Too many ears."),
            ("What do you call someone who doesn't like carbs?", "Lack-Toast Intolerant."),
            ("Why did the can crusher quit his job?", "Because it was soda pressing."),
            ("Why did the birthday boy wrap himself in paper?", "He wanted to live in the present."),
            ("What does a house wear?", "A dress."),
            ("Why couldn't the toilet paper cross the road?", "Because it got stuck in a crack."),
            ("Why didn't the bike want to go anywhere?", "Because it was two-tired!"),
            ("Want to hear a pizza joke?", "Nahhh, it's too cheesy!"),
            ("Why are chemists great at solving problems?", "Because they have all of the solutions!"),
            ("Why is it impossible to starve in the desert?", "Because of all the sand which is there!"),
            ("What did the cheese say when it looked in the mirror?", "Halloumi!"),
            ("Why did the developer go broke?", "Because he used up all his cache."),
            ("Did you know that ants are the only animals that don't get sick?", "Because they have little antibodies."),
            ("Why did the donut go to the dentist?", "To get a filling."),
            ("What do you call a bear with no teeth?", "A gummy bear!"),
            ("What does a vegan zombie like to eat?", "Graaains."),
            ("What do you call a dinosaur with only one eye?", "A Do-you-think-he-saw-us!"),
            ("Why should you never fall in love with a tennis player?", "Because to them... love means NOTHING!"),
            ("What did the full glass say to the empty glass?", "You look drunk."),
            ("What's a potato's favorite form of transportation?", "The gravy train."),
            ("What did one ocean say to the other?", "Nothing, they just waved."),
            ("What did the right eye say to the left eye?", "Honestly, between you and me something smells."),
            ("What do you call a dog that's been run over by a steamroller?", "Spot!"),
            ("What's the difference between a hippo and a zippo?", "One's pretty heavy and the other's a little lighter."),
            ("Why don't scientists trust atoms?", "They make up everything.")
        ]

        self.punchline_text = ""

    def joke_display(self):
        joke_data = random.choice(self.jokes)
        setup_display = joke_data[0]
        punchline_display = joke_data[1]

        setup_label['text'] = setup_display
        punchline_label['text'] = ""
        self.punchline_text = punchline_display

        speak(setup_display)  # Alexa speaks joke setup

    def punchline_reveal(self):
        if self.punchline_text:
            punchline_label['text'] = self.punchline_text
            punchline_label['fg'] = "#00AAFF"

            # Alexa speaks punchline → THEN laughing sound plays
            speak(self.punchline_text, after_speech=play_laughing_man_sound)

    def refresh_joke(self):
        setup_label['text'] = "Getting ready..."
        punchline_label['text'] = ""
        punchline_label['fg'] = "blue"
        self.root.after(500, self.joke_display)

    def close_app(self):
        self.root.quit()

# ---------- BUTTONS ----------
app_controller = JokeGame(root)

button1 = Button(root, text="Alexa tell me a Joke", font=("Arial", 12, "bold"), bg="#ADD8E6",
                 height=2, command=app_controller.joke_display)
button1.place(x=260, y=190)

button2 = Button(root, text="Show Punchline", font=("Arial", 12, "bold"), bg="#FF0000", width=15, height=2,
                 command=app_controller.punchline_reveal)
button2.place(x=260, y=255)

button3 = Button(root, text="Next Joke", font=("Arial", 12, "bold"), bg="#008000", width=15, height=2,
                 command=app_controller.refresh_joke)
button3.place(x=260, y=320)

button4 = Button(root, text="Quit", font=("Arial", 12, "bold"), bg="#FFA500", width=15, height=2,
                 command=app_controller.close_app)
button4.place(x=260, y=385)

# ---------- MAIN LOOP ----------
root.mainloop()

