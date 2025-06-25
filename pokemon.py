import tkinter as tk
from tkinter import messagebox
import random

# Define your Pokemon item list
pokemon_items = [
    "Rayquaza", "Blastoise", "Bulbasaur", 
    "Charmander", "Charizard", "Charmeleon",
    "Christmas Pikachu", "Christmas Dratini", "Christmas Psyduck",
    "Christmas Vulpix", "Christmas Gengar", "Christmas Digglet"
]

selected_pokemon = {"name": None}

# function to select Pokemon from the list
def select_pokemon(event):
    widget = event.widget
    index = int(widget.curselection()[0])
    value = widget.get(index)
    selected_pokemon["name"] = value

# shiny chance? and then shiny will dispense after shiny chance is rolled
def dispense_pokemon():
    name = selected_pokemon["name"]
    if not name:
        messagebox.showwarning("No Pokémon", "Please select a Pokémon first.")
        return

    is_shiny = random.randint(1, 25) == 1
    result = f"🎉 Dispensing: {'✨ Shiny ' if is_shiny else ''}{name}!"
    messagebox.showinfo("Pokémon Dispensed", result)

    #UI configurations 
def build_ui():
    root = tk.Tk()
    root.title("Pokémon Center Storage Box")
    root.geometry("400x400")
    root.configure(bg="#e6f2ff")

    title = tk.Label(root, text="Select a Pokémon", font=("Arial", 18, "bold"), bg="#e6f2ff")
    title.pack(pady=10)

    listbox = tk.Listbox(root, font=("Arial", 14), width=25, height=10)
    for item in pokemon_items:
        listbox.insert(tk.END, item)
    listbox.pack(pady=10)
    listbox.bind("<<ListboxSelect>>", select_pokemon)

    button = tk.Button(root, text="Dispense Pokémon", font=("Arial", 14), command=dispense_pokemon, bg="#ccffcc")
    button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    build_ui()
