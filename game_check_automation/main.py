from collections import automate_collections
from quests import automate_quests
import tkinter as tk


def start_quest_check_script(root):
    root.destroy()  # Close the GUI window
    automate_quests()

def start_collection_check_script(root):
    root.destroy()  # Close the GUI window
    automate_collections()


def create_gui():
    root = tk.Tk()
    root.title("Automation Script")

    start_button = tk.Button(root, text="Quest Check", command=lambda: start_quest_check_script(root))
    start_button.pack(pady=20)

    launch_button = tk.Button(root, text="Collection Check", command=lambda: start_collection_check_script(root))
    launch_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()


