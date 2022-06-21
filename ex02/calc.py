import tkinter as tk
import tkinter.messagebox as tkm


def button_click(event):
    button = event.widget
    num = button["text"]
    if num == "=":
        eqn = entry.get()
        res = eval(eqn)
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)
    elif num == "clear":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, num)

    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("計算機")
    #root.geometry("300x500")

    entry = tk.Entry(root, justify="right", width=10, font=("Times New Roman", 40))
    entry.grid(row=0, column = 0, columnspan=4)

    r, c = 4, 1
    for i in range(10):
        button = tk.Button(root, width=4, height=2, text=i, font=("Times New Roman", 30))
        button.bind("<1>", button_click)
        button.grid(row=r, column=c)
        c += 1
        if i%3 == 0:
            r -= 1
            c = 0
    
    for i, num in enumerate(["+", "-", "*", "/"]):
        button = tk.Button(root, width=4, height=2, text=num, font=("Times New Roman", 30))
        button.bind("<1>",button_click)
        button.grid(row=i+1, column=3)

    for i, num in enumerate(["clear", "="]):
        button = tk.Button(root, width=4, height=2, text=num, font=("Times New Roman", 30)) 
        button.bind("<1>",button_click)
        button.grid(row=4, column=i*2)

    root.mainloop()