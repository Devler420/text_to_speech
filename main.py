import random
import pyttsx3
import keyboard

engine = pyttsx3.init()

# voice sound
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# voice speed -- Default 200 wpm
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)

print("Starting Text_To_Speech dot dot dot")
engine.say("Starting Text To Speech program. Press spacebar to continue")
engine.runAndWait()

with open("text_to_read.txt", "r") as file:
    lines = file.readlines()
    print("Total Sentences: " + str(len(lines)))

done_read_sentences = set()

question_counter = 1
while len(done_read_sentences) < len(lines):
    # if keyboard.is_pressed("ctrl"):
    #         print("You pressed CTRL")
    #         break
    random_line = random.choice(lines)
    if random_line not in done_read_sentences:
        if question_counter == 10:
            engine.say("Ten questions completed")
            engine.runAndWait()
        sentence_split = random_line.split('|')
        question = sentence_split[0]
        answer = sentence_split[1].strip()
        keyboard.wait('space')
        done_read_sentences.add(random_line)
        engine.say(question)
        print("Question " + str(question_counter) + ": "  + question)
        engine.runAndWait()
        keyboard.wait('space')
        engine.say(answer)
        print("Answer: " + answer)
        engine.runAndWait()
        question_counter += 1
        print("")
        # time.sleep(5)

engine.say("Ending Text To Speech program")
engine.runAndWait()
print("Ending Text_To_Speech")