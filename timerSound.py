from timer import * 

from math import floor
from random import *
import winsound
from winsound import *
import threading
import time
import sys
import wave
import threading


def TimerSound(_timer, _beginTime): 
    _emptyLoop = 2
    while Timer(_timer, _beginTime) > 0 :
        if Timer(_timer, _beginTime) <= 10 and _emptyLoop == 1: 
            PlaySound("coeur", SND_ASYNC | SND_LOOP | SND_FILENAME)
            _emptyLoop = 0
        elif Timer(_timer, _beginTime) > 10 and _emptyLoop == 2:
            PlaySound("clock", SND_ASYNC | SND_LOOP | SND_FILENAME)
            _emptyLoop = 1
    PlaySound(None, SND_ASYNC | SND_FILENAME)
    return Timer(_timer, _beginTime)


