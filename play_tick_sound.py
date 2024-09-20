import pygame
import random
import time

def play_tick(bpm, sound_file, volume = 1):
  duration = 60 / bpm
  pygame.mixer.init()
  sound = pygame.mixer.Sound(sound_file)
  sound.play()
  time.sleep(duration)

while True:
  bpm = random.randint(45, 120)
  sound_file = "tick_sound.wav"
  play_tick(bpm, sound_file)