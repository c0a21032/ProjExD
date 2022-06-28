import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker
import random

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global mcx, mcy, mx, my
    if key == "Up" and meiro[my-1][mx] == 0:
        my -= 1
    elif key == "Down" and meiro[my+1][mx] == 0:
        my += 1
    elif key == "Left" and meiro[my][mx-1] == 0:
        mx -= 1
    elif key == "Right" and meiro[my][mx+1] == 0:
        mx += 1
    mcx = 50 + 100 * mx
    mcy = 50 + 100 * my
    canvas.coords("tori", mcx, mcy)
    canvas.pack()
    root.after(100, main_proc)

def enemy():
    global ecx, ecy, ex, ey
    delta = random.randint(1, 4)
    if delta == 1 and ey-1 > 0:
        ey -= 1
    elif delta == 2 and ey+1 < 9:
        ey += 1
    elif delta == 3 and ex-1 > 0:
        ex -= 1
    elif delta == 4 and ex+1 < 14:
        ex += 1
    ecx = 50 + 100 * ex
    ecy = 50 + 100 * ey
    canvas.coords("teki", ecx, ecy)
    canvas.pack()
    root.after(500, enemy)

def isclear():
    global stars
    if (mx, my) in stars:
        stars.remove((mx, my))
    if (mx, my) == (ex, ey) and len(stars)==0:
        tkm.showinfo("Congratulations!!", "クリアです！おめでとうございます！")
    root.after(100, isclear)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root, width="1500", height="900", bg="black")
    canvas.pack()

    meiro = maze_maker.make_maze(15, 9)
    maze_maker.show_maze(canvas, meiro)

    stars = []
    star = tk.PhotoImage(file="ex03/fig/star.png")
    while len(stars) < 9:
        sx = random.randint(0, 14)
        sy = random.randint(0, 8)
        if meiro[sy][sx] == 0 and (sx, sy) not in stars:
            stars.append((sx, sy))
            canvas.create_image(50 + 100 * sx, 50 + 100 * sy, image=star)
            canvas.pack()

    mx, my = 1, 1
    mcx, mcy = 50 + 100 * mx, 50 + 100 * my
    tori = tk.PhotoImage(file="ex03/fig/2.png")
    canvas.create_image(mcx, mcy, image=tori, tag="tori")
    canvas.pack()

    ex, ey = 0, 0
    while True:
        ex = random.randint(7, 14)
        ey = random.randint(4, 8)
        if meiro[ey][ex] == 0:
            break
    ecx, ecy = 50 + 100 * ex, 50 + 100 * ey
    teki = tk.PhotoImage(file="ex03/fig/6.png")
    canvas.create_image(ecx, ecy, image=teki, tag="teki")
    canvas.pack()

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()
    enemy()
    isclear()
    root.mainloop()