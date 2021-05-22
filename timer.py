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


def Timer(_timer, _begninTime):
    _timer = _timer - (time.time() - _beginTime) 
    return _timer
