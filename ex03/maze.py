import tkinter as tk
import maze_maker

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my
    if key == "Up":
        my -= 1
    elif key == "Down":
        my += 1
    elif key == "Left":
        mx -= 1
    elif key == "Right":
        mx += 1
    cx = 50 + 100 * mx
    cy = 50 + 100 * my
    canvas.coords("tori", cx, cy)
    canvas.pack()
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root, width="1500", height="900", bg="black")
    canvas.pack()

    meiro = maze_maker.make_maze(15, 9)
    maze_maker.show_maze(canvas, meiro)

    mx, my = 1, 1
    cx, cy = 100 * mx, 100 * my
    tori = tk.PhotoImage(file="ex03/fig/2.png")
    canvas.create_image(cx, cy, image=tori, tag="tori")
    canvas.pack()

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()
    root.mainloop()