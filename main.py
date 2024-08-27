import random
import time
import pyttsx3

engine = pyttsx3.init()

print("Starting Text_To_Speech dot dot dot")
engine.say("Starting Text To Speech program")

with open("text_to_read.txt", "r") as file:
    lines = file.readlines()
    print("Total Sentences: " + str(len(lines)))

done_read_sentences = set()

while len(done_read_sentences) < len(lines):
    random_line = random.choice(lines)
    if random_line not in done_read_sentences:
        print(random_line)
        done_read_sentences.add(random_line)
        engine.say(random_line)
        engine.runAndWait()
        time.sleep(5)

engine.say("Ending Text To Speech program dot dot dot")
engine.runAndWait()
print("Ending Text_To_Speech")