'''
TODO:binary fill entire popup
'''
import tkinter as tk
import random

def the_fun_stuff():
    binary_str = ""
    for i in range(10):
        num = random.randint(0, 1)
        binary_str += str(num)
    return binary_str

def show_popup():
    popup = tk.Tk()
    popup.title("look at me. Im the popup now")
    popup.geometry("1000x1000")
    output_text = tk.Text(popup, font=("Helvetica", 10))
    output_text.pack(fill=tk.BOTH, expand=True)
    
    while True:
        binary_output = the_fun_stuff()
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, binary_output)
        popup.update_idletasks()
        popup.update()

if __name__ == "__main__":
    show_popup()
