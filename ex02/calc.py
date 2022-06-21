import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("計算機")
    root.geometry("300x500")

    r, c = 0, 0
    for num in range(9, -1, -1):
        button = tk.Button(root, width=4, height=2, text=str(num), font=("Times New Roman", 30))
        button.grid(row=r, column=c)
        c += 1
        if (num-1)%3 == 0:
            r += 1
            c = 0

    root.mainloop()