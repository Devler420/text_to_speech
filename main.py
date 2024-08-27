import random
import time
import pyttsx3

engine = pyttsx3.init()

print("Starting Text_To_Speech")

with open("text_to_read.txt", "r") as file:
    lines = file.readlines()

while True:
    random_line = random.choice(lines)
    print(random_line)
    engine.say(random_line)
    engine.runAndWait()
    time.sleep(5)