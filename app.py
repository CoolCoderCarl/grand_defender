import tkinter
import gdefender


def check_pass_btn():
    pass


def cancel_btn():
    pass


# Window initialization and properties
window = tkinter.Tk()
window.title('Grand Defender 2022')
window.geometry('400x400')
window.minsize(width=400, height=400)
window.maxsize(width=400, height=400)

# Timer variable
second = tkinter.StringVar()
second.set("30")

# Frames
frame_warning = tkinter.Frame(window, width=200, height=200)
frame_timer = tkinter.Frame(window, width=200, height=200)
frame_input = tkinter.Frame(window, width=400, height=200, bg='blue')

frame_warning.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)
frame_timer.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.5)
frame_input.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

frame_warning.grid(row=0, column=0, sticky="wens")
frame_timer.grid(row=0, column=1, sticky="wens")
# frame_input.grid(row=1, column=1, columnspan=2, sticky="wens")

# Labels
lbl_warning_message = tkinter.Label(frame_warning, text=gdefender.warning_message, font=("Arial", 10, ""))
lbl_warning_message.grid(row=0, column=0, sticky="w", padx=10, pady=10)

lbl_timer = tkinter.Label(frame_timer, textvariable=second, font=("Arial", 20, ""))
lbl_timer.grid(row=0, column=0, padx=10, pady=10)


# lbl = tkinter.Label()
# lbl = tkinter.Label()
# lbl = tkinter.Label()


# Input


# Buttons


# Start window
window.mainloop()

