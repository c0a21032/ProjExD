import tkinter as tk
import tkinter.messagebox as tkm


def button_click(event):
    button = event.widget
    num = button["text"]
    eqn = entry.get()
    if num in ["たす", "ひく", "かける", "わる"]:
        if num == eqn[-1]:
            pass
        else:
            entry.insert(tk.END, enzan[num])
    elif num == "こたえ":
        num = "="
        res = eval(eqn)
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)
    elif num == "けす":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, num)

    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("計算機")

    entry = tk.Entry(root, justify="right", width=10, font=("Times New Roman", 40))
    entry.grid(row=0, column = 0, columnspan=4)

    r, c = 4, 0
    for i in range(10):
        button = tk.Button(root, width=5, height=2, text=i, font=("Times New Roman", 30), bg="lemon chiffon")
        button.bind("<1>", button_click)
        button.grid(row=r, column=c)
        c += 1
        if i%3 == 0:
            r -= 1
            c = 0
    
    enzan = {"たす":"+", "ひく":"-", "かける":"*", "わる":"/"}
    for i, num in enumerate(enzan.keys()):
        button = tk.Button(root, width=5, height=2, text=num, font=("Times New Roman", 30), bg="azure")
        button.bind("<1>",button_click)
        button.grid(row=i+1, column=3)

    button = tk.Button(root, width=5, height=2, text="けす", font=("Times New Roman", 30), bg="red3", fg="white") 
    button.bind("<1>",button_click)
    button.grid(row=4, column=1)

    button = tk.Button(root, width=5, height=2, text="こたえ", font=("Times New Roman", 30), bg="cyan3", fg="white") 
    button.bind("<1>",button_click)
    button.grid(row=4, column=2)

    root.mainloop()