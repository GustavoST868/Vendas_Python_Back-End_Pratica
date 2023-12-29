import tkinter as tk
class InterfaceProduct:
    def __init__(self):
        self.window = tk.Tk()

    def Window(self):
        self.window.title("")
        self.window.geometry("1000x600")
        self.window.mainloop()

i = InterfaceProduct()
i.Window()
