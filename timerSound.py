import enigma, combat, labyrinthe, timer, timerSound
from math import floor
from random import *
import winsound
from winsound import *
import threading
import time
import sys
import wave
import threading

def TimerSound(_timer): 
    while _timer >= 0:
        PlaySound("clock", SND_ASYNC | SND_LOOP | SND_FILENAME)
    else:
        PlaySound(None, SND_ASYNC | SND_FILENAME)

