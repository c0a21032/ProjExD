import tkinter as tk

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy
    if key == "Up":
        cy -= 20
    elif key == "Down":
        cy += 20
    elif key == "Left":
        cx -= 20
    elif key == "Right":
        cx += 20
    canvas.coords("tori", cx, cy)
    canvas.pack()
    root.after(10, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    cx, cy = 300, 400
    tori = tk.PhotoImage(file="ex03/fig/2.png")
    canvas = tk.Canvas(width="1500", height="900", bg="black")
    canvas.create_image(cx, cy, image=tori, tag="tori")
    canvas.pack()

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    root.after(0, main_proc)
    root.mainloop()