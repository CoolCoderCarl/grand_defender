import os
import platform
import time
from threading import Event, Thread, Timer

WARNING_MSG = """
            Please, input password. 
            PC will shutdown:
            1) If you did not input correct password 
            2) When the timer is ends
            3) If you close this window
"""

TIMER_MSG = "Time is up !"
SHUTDOWN_WIN = "shutdown /s /t 1"
SHUTDOWN_NIX = "shutdown now -h"


def is_timer_finished(t: int) -> bool:
    """
    Return True when timer is finished
    :param t:
    :return:
    """
    while t > 0:
        t -= 1
        time.sleep(1)
    return True


def get_pass() -> str:
    """
    Read password from file
    :return:
    """
    try:
        password_file = open("password", "r")
        password = password_file.read()
        return password
    except FileNotFoundError:
        exit(1)


def is_linux() -> bool:
    """
    Check is current system Linux
    :return:
    """
    if "linux" in str(platform.system()).lower():
        return True
    else:
        return False


def shutdown_system():
    """
    Shutdown the system
    Win or nix
    :return:
    """
    if is_linux():
        print("TURN OFF")
        # os.system(SHUTDOWN_NIX)
    else:
        print("TURN OFF")
        # os.system(SHUTDOWN_WIN)


def timer(t=10, *args):
    """
    If time is up, notify user about it and shutdown system
    :return:
    """
    if is_timer_finished(t):
        print(TIMER_MSG)
        # if event.is_set():
        #     exit(0)
        shutdown_system()


def check_the_pass():
    """
    Check is password is correct
    If not shutdown system
    :return:
    """
    input_password = input("Password:") or "\n"
    if input_password == get_pass():
        exit(0)
    else:
        shutdown_system()


if __name__ == "__main__":

    event = Event()
    print(WARNING_MSG)

    timer_thread = Thread(target=timer, args=(10, event.set()))
    passw_thread = Thread(target=check_the_pass)

    passw_thread.daemon = True
    timer_thread.start()
    passw_thread.start()
