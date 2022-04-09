import os
import sys
import time
import platform
import threading

warning = """
            Please, input password. 
            PC will shutdown:
            1) If you did not input correct password 
            2) When the timer is ends
            3) If you close this window
"""

timer_msg = "Time is up !"
shutdown_win = "shutdown /s /t 1"
shutdown_nix = "shutdown now -h"


def is_timer_finished(t=10):
    """
    Return True when timer is finished
    :param t:
    :return:
    """
    while t > 0:
        t -= 1
        time.sleep(1)
    return True


def get_pass():
    """
    Read password from file
    :return:
    """
    password_file = open("password", "r")
    password = password_file.read()
    return password


def is_linux():
    """
    Check is current system Linux
    :return:
    """
    if 'Linux' in platform.system():
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
        os.system(shutdown_nix)
    else:
        print("FAIL")
        os.system(shutdown_win)


def timer():
    """
    If time is up, notify user about it and shutdown system
    :return:
    """
    if is_timer_finished():
        print(timer_msg)
        shutdown_system()


def is_pass_correct():
    """
    Check is password is correct
    If not shutdown system
    :return:
    """
    input_password = input("Password:")
    if input_password == get_pass():
        sys.exit()
    else:
        shutdown_system()


if __name__ == '__main__':

    print(warning)
    # Run timer
    # Check pass
