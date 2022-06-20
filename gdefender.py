import os
import time
import platform
from threading import Thread

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


def is_timer_finished(t=10) -> bool:
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
    if 'linux' in str(platform.system()).lower():
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
        # os.system(shutdown_nix)
        print("TURN OFF")
    else:
        print("TURN OFF")
        # os.system(shutdown_win)


def timer():
    """
    If time is up, notify user about it and shutdown system
    :return:
    """
    if is_timer_finished():
        print(timer_msg)
        shutdown_system()


def check_the_pass():
    """
    Check is password is correct
    If not shutdown system
    :return:
    """
    input_password = input("Password:")
    if input_password == get_pass():
        exit(0)
    else:
        shutdown_system()


if __name__ == '__main__':

    print(warning)

    passw_thread = Thread(target=check_the_pass())
    timer_thread = Thread(target=timer())

    passw_thread.daemon = True
    passw_thread.start()
    timer_thread.start()

    passw_thread.join()
    timer_thread.join()
    # Run timer
    # Check pass
