import tkinter as tk
import tkinterweb
window = tk.Tk()
window.title("Python web browser")
def search():
    a = entry.get()
    frame.load_website(f'{a}')

entry = tk.Entry()
entry.pack()
button = tk.Button(text = "Go", command= search)
button.pack()
frame = tkinterweb.HtmlFrame(window)
frame.pack(fill = "both", expand = True)

window.mainloop()