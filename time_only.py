import random
import pyttsx3
import keyboard
from datetime import timedelta
import time
import math

engine = pyttsx3.init()

# voice sound
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# voice speed -- Default 200 wpm
newVoiceRate = 120
volume = 0.75
engine.setProperty('volume', volume)
engine.setProperty('rate', newVoiceRate)

instruction_set = ["rectangle", "circle", "triangle","red", "blue", "yellow", "none"]
random_instruction_left = "Left hand: " + random.choice(instruction_set)
random_instruction_right = "Right hand: " + random.choice(instruction_set)
print(random_instruction_left + " | " + random_instruction_right + "\n")

print("Starting Time dot dot dot")
engine.say("Starting Time program.")
engine.runAndWait()
engine.say(random_instruction_left + " " + random_instruction_right)
engine.runAndWait()

def calculate_time(question):
    """Calculates the time based on the given question."""
    question_split = question.split()
    operation = question_split[1]
    times = [question_split[0], question_split[2]]
    if operation == "plus":
        result = timedelta(hours=int(times[0].split(":")[0]), minutes=int(times[0].split(":")[1])) + timedelta(hours=int(times[1].split(":")[0]), minutes=int(times[1].split(":")[1]))
    elif operation == "minus":
        result = timedelta(hours=int(times[0].split(":")[0]), minutes=int(times[0].split(":")[1])) - timedelta(hours=int(times[1].split(":")[0]), minutes=int(times[1].split(":")[1]))
    else:
        raise ValueError("Invalid operation")
    return result

with open("time_only.txt", "r") as file:
    lines = file.readlines()
    print("Total Sentences: " + str(len(lines)))

done_read_sentences = set()
time_used_set = set()

question_counter = 1
while len(done_read_sentences) < len(lines):
    random_line = random.choice(lines)
    if random_line not in done_read_sentences:
        if question_counter == 10:
            engine.say("Question Number 10")
            engine.runAndWait()

        question = random_line.strip()
        keyboard.wait('space')
        done_read_sentences.add(random_line)
        engine.say(question)
        print("Question " + str(question_counter) + ": "  + question)
        engine.runAndWait()

        start_time = time.time()

        keyboard.wait('space')
        try:
            result = calculate_time(question)
            total_seconds = result.total_seconds()

            hours = int(total_seconds // 3600)
            if hours > 24 :
                hours = hours - 24
                
            minutes = int((total_seconds % 3600) // 60)

            if len(str(hours)) == 1:
                hours = f"0{hours}"
            if len(str(minutes)) == 1:
                minutes = f"0{minutes}"

            engine.say(f"{hours}:{minutes}")
            print(f"Answer: {hours}:{minutes}")

            end_time = time.time()
            elasped_time = end_time - start_time
            time_used_set.add(elasped_time)
            print(f"Time Used: {elasped_time:.2f} seconds")

            total_time = math.fsum(time_used_set)
            total_answered = len(time_used_set)
            avg = total_time/total_answered
            print(f"Time Avg: {avg:.2f} seconds")

        except ValueError:
            engine.say("Question Invalid")
            print("Invalid question format")
        engine.runAndWait() 
        question_counter += 1
        print("")
        # time.sleep(5)

engine.say("Ending Time program")
engine.runAndWait()
print("Ending Text_To_Speech")