import random
import pyttsx3
import keyboard
import time
import math

engine = pyttsx3.init()

# voice sound
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# voice speed -- Default 200 wpm
newVoiceRate = 130
volume = 0.75
engine.setProperty('volume', volume)
engine.setProperty('rate', newVoiceRate)

instruction_set = ["rectangle", "circle", "triangle","red", "blue", "yellow", "none"]
random_instruction_left = "Left hand: " + random.choice(instruction_set)
random_instruction_right = "Right hand: " + random.choice(instruction_set)
print(random_instruction_left + " | " + random_instruction_right + "\n")

print("Starting Text_To_Speech dot dot dot")
engine.say("Starting Text To Speech program.")
engine.runAndWait()
engine.say(random_instruction_left + " " + random_instruction_right)
engine.runAndWait()

with open("text_to_read.txt", "r") as file:
    lines = file.readlines()
    print("Total Sentences: " + str(len(lines)))

done_read_sentences = set()
time_used_set = set()

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
        sentence_split = random_line.split('|')
        question = sentence_split[0]
        answer = sentence_split[1].strip()
        keyboard.wait('space')
        done_read_sentences.add(random_line)
        engine.say(question)
        print("Question " + str(question_counter) + ": "  + question)
        engine.runAndWait()

        start_time = time.time()

        keyboard.wait('space')
        engine.say(answer)
        print("Answer: " + answer)

        end_time = time.time()
        elasped_time = end_time - start_time
        time_used_set.add(elasped_time)
        print(f"Time Used: {elasped_time:.2f} seconds")

        total_time = math.fsum(time_used_set)
        total_answered = len(time_used_set)
        avg = total_time/total_answered
        print(f"Time Avg: {avg:.2f} seconds")

        engine.runAndWait()

        question_counter += 1
        print("")
        # time.sleep(5)

engine.say("Ending Text To Speech program")
engine.runAndWait()
print("Ending Text_To_Speech")