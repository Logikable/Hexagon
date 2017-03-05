from tkinter import *
from tkinter import ttk

root = Tk()
call_number = StringVar()
text_number = StringVar()
text_msg = StringVar()

import json
def calculate():
	

def calculate1():
	return 123

def calculate2():
	return 123

def main():
	root.title("StealthGuard +")

	mainframe = ttk.Frame(root, padding="5 5 12 12")
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	mainframe.columnconfigure(0, weight=1)
	mainframe.rowconfigure(0, weight=1)

	photo = PhotoImage(file=(sys.argv[1] + "\\image.gif"))
	label = Label(image=photo)
	label.grid(column = 1, row = 0, sticky=N)

	feet_entry = ttk.Entry(mainframe, width=18, textvariable=call_number)
	feet_entry.grid(column=2, row=1, sticky=(W, E))

	feet_entry2 = ttk.Entry(mainframe, width=18, textvariable=text_number)
	feet_entry2.grid(column=2, row=2, sticky=(W, E))

	feet_entry3 = ttk.Entry(mainframe, width=18, textvariable=text_msg)
	feet_entry3.grid(column=2, row=3, sticky=(W, E))

	ttk.Button(mainframe, text="Enter", command=calculate).grid(column=3, row=1, sticky=W)
	ttk.Button(mainframe, text="Enter", command=calculate1).grid(column=3, row=2, sticky=W)
	ttk.Button(mainframe, text="Enter", command=calculate2).grid(column=3, row=3, sticky=W)

	ttk.Label(mainframe, text="Emergency Call Number:").grid(column=1, row=1, sticky=W)
	ttk.Label(mainframe, text="Emergency Text Number:").grid(column=1, row=2, sticky=W)
	ttk.Label(mainframe, text="Emergency Text Message:").grid(column=1, row=3, sticky=W)

	for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

	feet_entry.focus()
	root.bind('<Return>')

	root.mainloop()
	
if __name__ == "__main__":
	main()