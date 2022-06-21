import tkinter as tk

root = tk.Tk()
root.title("計算機")
root.geometry("300x500")

for i in range(9, 0, -1):
    button = tk.Button(root, text=str(i), font=("Times New Roman", 30))
    button.pack()

root.mainloop()