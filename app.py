import tkinter
import gdefender


def check_pass_btn():
    pass


def cancel_btn():
    pass


# Window initialization and properties
window = tkinter.Tk()
window.title('Grand Defender 2022')
window.geometry('500x500')
window.minsize(width=500, height=500)
window.maxsize(width=500, height=500)


# Frames
frame_warning = tkinter.Frame(window, width=250, height=250)
frame_timer = tkinter.Frame(window, width=250, height=250, bg='red')
frame_input = tkinter.Frame(window, width=500, height=250, bg='blue')

frame_warning.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)
frame_timer.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.5)
frame_input.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

frame_warning.grid(row=0, column=0, sticky="wens")
frame_timer.grid(row=0, column=1, sticky="wens")
# frame_input.grid(row=1, column=1, columnspan=2, sticky="wens")

# Labels
warning_message = tkinter.Label(frame_warning, text=gdefender.warning_message)

lbl_status = tkinter.Label(frame_timer, text="Status")
# lbl = tkinter.Label()
# lbl = tkinter.Label()
# lbl = tkinter.Label()

warning_message.grid(row=0, column=0, sticky="w", padx=10, pady=10)

# lbl_status.grid(row=0, column=0, padx=10, pady=10)


# Input


# Buttons


# Start window
window.mainloop()