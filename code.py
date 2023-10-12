'''
TODO:ummmmm wut happened? code can't run, lets get that sorted

FINISH:
binary fill entire popup
'''
import tkinter as tk
import random

def the_fun_stuff():
    binary_str = ""
    for i in range(10000):
        num = random.randint(0, 1)
        binary_str += str(num)
    return binary_str

def show_popup():
    def update_text():
        binary_output = the_fun_stuff()
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, binary_output)
        popup.after(500, update_text)

    popup = tk.Tk()
    popup.title("Look at me. I'm the popup now")
    popup.geometry("1000x1000")
    output_text = tk.Text(popup, font=("Helvetica", 10), fg="green")
    output_text.pack(fill=tk.BOTH, expand=True)
    popup.configure(bg="black")
    
    update_text()

    popup.mainloop()
