import time
import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

# get current time
time_now = datetime.datetime.now()

win = tk.Tk()
win.title("Calculate your age in Future") # window title
win.geometry("395x267") # window size
win.resizable(0,0) # window not resizable
win.configure(background="#FF55FF") # background color

age_now = tk.IntVar()
future_year = tk.IntVar()

# =================== Command =============
def age_future():
	# =============================== Calculations ===============================
	# get current year
	current_year = time_now.year

	if future_year.get() < current_year: # if user insert year < current year
		messagebox.showerror("Error", "Please Insert the year superior to {}".format(current_year)) # show error
		time.sleep(0.5) # sleep 0.5s
		win.destroy() # then destroy
	else:

		# get born year by remove his age with the current year
		born_year = int(current_year) - int(age_now.get())
		# get his future age by remove born_year and future year
		age_in_that_year = int(future_year.get()) - int(born_year)
		# format the text to output after calculation
		out = "In {} You'll be {} Years Old".format(future_year.get(), age_in_that_year)
	# ==============================================================================

	# ========= make scrolled text field ==
	output_field = ScrolledText(win, width=30, height=2)
	output_field.grid(row=5, column=1, columnspan=3)
	#-------------------------
	output_field.insert(tk.INSERT, out) # Show the output in scrolled text field
# =========================================


# ================== Main window =============

labelDescri = tk.Label(win, text="Your Age In Future", bg="#FF55FF", fg="dodgerblue")
labelDescri.grid(row=0, column=1, columnspan=3)

label_your_age_now = tk.Label(win, text="Your Age Now:", bg="#FF55FF",fg="dodgerblue")
label_your_age_now.grid(row=1, column=0)

entry_your_age_now = tk.Entry(win,fg="dodgerblue", textvariable = age_now)
entry_your_age_now.grid(row=1, column=2)

label_future_year = tk.Label(win, text="Future Year :", bg="#FF55FF", fg="dodgerblue")
label_future_year.grid(row=3, column=0)

entry_future_year = tk.Entry(win,fg="dodgerblue", textvariable = future_year)
entry_future_year.grid(row=3, column=2)

submit_btn = tk.Button(win, text="Submit", bg="#FF55FF", fg="dodgerblue", command=age_future)
submit_btn.grid(row=4, column=1, columnspan=3)
# ===============================================


win.mainloop()
