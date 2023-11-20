import time

start_closed_eye = time.time()
elapsed_time = 0


def getElapsedTime(isclosed):
    global start_closed_eye, elapsed_time
    if isclosed is False:
        start_closed_eye = time.time()
        elapsed_time = 0
    elif isclosed is True:
        elapsed_time = time.time() - start_closed_eye

    return elapsed_time
