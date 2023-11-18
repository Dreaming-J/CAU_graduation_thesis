import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from util.SoundPlayer import play
import time

isRinging = False


def alarm(elapsed_time):
    global isRinging

    if isRinging is True:
        return

    isRinging = True
    if elapsed_time > 9:
        play("strong_alarm")
    elif elapsed_time > 6:
        play("normal_alarm")
    elif elapsed_time > 3:
        play("beep")
    time.sleep(3)
    isRinging = False
