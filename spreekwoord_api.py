from tkinter import Tk, Label, StringVar
import requests

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("")
        self.label_text = StringVar()
        self.label_text.set("Klik op deze tekst voor een nieuw gezegde of spreekwoord")
        self.label = Label(master, textvariable=self.label_text)
        self.label.bind("<Button-1>", self.retrieve_api)
        self.label.pack()

    def retrieve_api(self, event):
        response = requests.get("https://api.jeroenkreuk.com/spreekwoord?aantal=0")
        spreekwoord = response.json()["Spreekwoord"]
        self.label_text.set(spreekwoord)
        print(spreekwoord)

root = Tk()
gui = GUI(root)
root.mainloop()
