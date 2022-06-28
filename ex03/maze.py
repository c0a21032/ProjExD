import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    cx, cy = 300, 400
    tori = tk.PhotoImage(file="ex03/fig/2.png")
    canvas = tk.Canvas(width="1500", height="900", bg="black")
    canvas.create_image(cx, cy, image=tori, tag="tori")
    canvas.pack()

    root.mainloop()