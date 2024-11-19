import random
import pyttsx3
import keyboard
import time
import math
from datetime import timedelta
import re

def say_instruction(engine):
    instruction_set = ["rectangle.", "circle.", "triangle.", "red.", "blue.", "yellow.", "none."]
    random_instruction_left = "Left hand: " + random.choice(instruction_set)
    random_instruction_right = "Right hand: " + random.choice(instruction_set)

    random_hand = random.randint(1,3)
    if random_hand == 1:
        tgt_flag = "Left Then Right."
    elif random_hand == 2:
        tgt_flag = "Right Then Left."
    else:
        tgt_flag = "Together."

    instruction = random_instruction_left + " | " + random_instruction_right + " | " + tgt_flag + "\n"
    print(instruction)

    print("Starting Text_To_Speech dot dot dot")
    engine.say("Starting Text To Speech program.")
    engine.runAndWait()
    engine.say(instruction)
    engine.runAndWait()

def read_text_based_question(engine, done_read_sentences, time_used_set, question_counter, random_line):
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

def read_math_based_question(engine, done_read_sentences, time_used_set, question_counter, random_line):
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

    start_time = time.time()

    keyboard.wait('space')
    engine.say(str(answer))
    print("Answer: " + str(answer))

    end_time = time.time()
    elasped_time = end_time - start_time
    time_used_set.add(elasped_time)
    print(f"Time Used: {elasped_time:.2f} seconds")

    total_time = math.fsum(time_used_set)
    total_answered = len(time_used_set)
    avg = total_time/total_answered
    print(f"Time Avg: {avg:.2f} seconds")

    engine.runAndWait()

def read_time_based_question(engine, done_read_sentences, time_used_set, question_counter, random_line, calculate_time):
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
        print("[ERROR] Invalid operation at question number: " + question_counter)
        raise ValueError("Invalid operation")
    return result

def check_if_question_is_time_based(time_string):
    # Checks if the time string matches the required format: HH:MM plus/minus HH:MM
    pattern = r"^(?:[01][0-9]|2[0-3]):[0-5][0-9]\s+(?:plus|minus)\s+(?:[01][0-9]|2[0-3]):[0-5][0-9]$"
    return re.match(pattern, time_string) is not None

# START LOGIC
engine = pyttsx3.init()

# voice sound
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# voice speed -- Default 200 wpm
newVoiceRate = 130
volume = 0.9
engine.setProperty('volume', volume)
engine.setProperty('rate', newVoiceRate)

say_instruction(engine)

with open("text_to_read.txt", "r") as file:
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

        if ("|" in random_line):
            read_text_based_question(engine, done_read_sentences, time_used_set, question_counter, random_line)
        elif ("times" in random_line and len(random_line) == 12):
            read_math_based_question(engine, done_read_sentences, time_used_set, question_counter, random_line)
        elif (check_if_question_is_time_based(random_line)):
            read_time_based_question(engine, done_read_sentences, time_used_set, question_counter, random_line, calculate_time)

        question_counter += 1
        print("")

engine.say("Ending Text To Speech program")
engine.runAndWait()
print("Ending Text_To_Speech")