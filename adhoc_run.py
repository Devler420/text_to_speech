import random
import pyttsx3
import keyboard
from datetime import timedelta

engine = pyttsx3.init()

# voice sound
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# voice speed -- Default 200 wpm
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)

print("Starting Text_To_Speech dot dot dot")
engine.say("Starting Time program.")
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

with open("debug_text.txt", "r") as file:
    lines = file.readlines()
    print("Total Sentences: " + str(len(lines)))

done_read_sentences = set()

question_counter = 1
while len(done_read_sentences) < len(lines):
    random_line = random.choice(lines)
    if random_line not in done_read_sentences:
        if question_counter == 10:
            engine.say("Question Number 10")
            engine.runAndWait()

        question = random_line
        keyboard.wait('space')
        done_read_sentences.add(random_line)
        engine.say(question)
        print("Question " + str(question_counter) + ": "  + question)
        engine.runAndWait()
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