import Tkinter as tk


def write_slogan():
    print("Tkinter is easy to use!")


root = tk.Tk()
frame = tk.Frame(root, width=200, height=100)
frame.pack()



button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()