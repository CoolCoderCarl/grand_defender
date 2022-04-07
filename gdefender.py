import os
import sys
import time
import threading

warning = """
            Please, input password. 
            PC will shutdown:
            1) If you did not input correct password 
            2) When the timer is ends
            3) If you close this window
"""

print(warning)

timer_msg = "Time is up !"
shutdown_cmd = "shutdown /s /t 1"


def is_timer_finished(t=10):
    while t > 0:
        t -= 1
        time.sleep(1)
    return True


def timer():
    if is_timer_finished():
        print(timer_msg)
        sys.exit()
        # os.system(shutdown_cmd)


def get_pass():
    password_file = open("password", "r")
    password = password_file.read()
    return password


def shutdown_check():
    input_password = input("Password:")
    if input_password == get_pass():
        sys.exit()
    else:
        print("FAIL")
        sys.exit()
        # os.system(shutdown_cmd)


if __name__ == '__main__':

    shutdown_check()
