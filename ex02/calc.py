import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    button = event.widget
    num = button["text"]
    entry.insert(tk.END, num)
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("計算機")
    #root.geometry("300x500")

    entry = tk.Entry(root, justify="right", width=10, font=("Times New Roman", 40))
    entry.grid(row=0, column = 0, columnspan=3)

    r = 1
    for num in range(9, -1, -1):
        button = tk.Button(root, width=4, height=2, text=str(num), font=("Times New Roman", 30))
        button.bind("<1>", button_click)
        button.grid(row=r, column=num%3)
        if (num-1)%3 == 0:
            r += 1
    
    button = tk.Button(root, width=4, height=2, text="+", font=("Times New Roman", 30))
    button.bind("<1>", button_click)
    button.grid(row=4, column=1)

    root.mainloop()