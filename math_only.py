# Copyright (c) [2024] [Panupong Utvichai]

# Licensed under the Mozilla Public License Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://mozilla.org/MPL/2.0/

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.   

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
newVoiceRate = 140
volume = 0.9
engine.setProperty('volume', volume)
engine.setProperty('rate', newVoiceRate)

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

print("Starting Math dot dot dot")
engine.say("Starting Math program.")
engine.runAndWait()
engine.say(instruction)
engine.runAndWait()

with open("math_only.txt", "r") as file:
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
        question_counter += 1
        print("")
        # time.sleep(5)

engine.say("Ending Math program")
engine.runAndWait()
print("Ending Math")