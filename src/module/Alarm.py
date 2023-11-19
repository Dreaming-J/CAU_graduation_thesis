import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from util.SoundPlayer import play
from util.Constant import *
from util.Variable import *
import time
import threading


def alarm(elapsed_time):
    global isRinging

    if isRinging is True or elapsed_time < 3:
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


def getAlarmStatus(elapsed_time):
    if elapsed_time > 9:
        alarm_status = ("ALERT!!!", RED)
    elif elapsed_time > 6:
        alarm_status = ("Warning!!", ORANGE)
    elif elapsed_time > 3:
        alarm_status = ("watch!", YELLOW)
    else:
        alarm_status = ("normal", GREEN)
    return alarm_status


def threadAlarm(isclosed):
    global start_closed_eye, elapsed_time
    if isclosed is False:
        start_closed_eye = time.time()
        elapsed_time = 0
    elif isclosed is True:
        elapsed_time = time.time() - start_closed_eye

    alarm_thread = threading.Thread(target=alarm, args=(elapsed_time,))
    alarm_thread.start()

    return getAlarmStatus(elapsed_time), elapsed_time
