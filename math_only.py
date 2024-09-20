import random
import pyttsx3
import keyboard

engine = pyttsx3.init()

# voice sound
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# voice speed -- Default 200 wpm
newVoiceRate = 150
volume = 0.75
engine.setProperty('volume', volume)
engine.setProperty('rate', newVoiceRate)

print("Starting Math dot dot dot")
engine.say("Starting Math program.")
engine.runAndWait()

with open("math_only.txt", "r") as file:
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
            engine.say("Question Number 10")
            engine.runAndWait()
        sentence_split = random_line.split('times')
        question = random_line.strip()
        first_num = sentence_split[0].strip()
        second_num = sentence_split[1].strip()
        answer = int(first_num) * int(second_num)
        keyboard.wait('space')
        done_read_sentences.add(random_line)
        engine.say(question)
        print("Question " + str(question_counter) + ": "  + question)
        engine.runAndWait()
        keyboard.wait('space')
        engine.say(str(answer))
        print("Answer: " + str(answer))
        engine.runAndWait()
        question_counter += 1
        print("")
        # time.sleep(5)

engine.say("Ending Math program")
engine.runAndWait()
print("Ending Math")