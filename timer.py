
from math import floor
from random import *
import winsound
from winsound import *
import threading
import time
import sys
import wave
import threading

def Timer(_timer, _beginTime):
    _timer -= floor(time.time() - _beginTime) 
    return _timer
