import requests

def get_pokemon_info(pokemon_name):
    """Fetches Pokémon data from PokeAPI."""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk # Install Pillow: pip install Pillow

def display_pokemon_info(pokemon_data):
    """Displays Pokémon information in a new window."""
    if not pokemon_data:
        messagebox.showerror("Error", "Pokémon not found!")
        return

    info_window = tk.Toplevel(root)
    info_window.title(pokemon_data['name'].capitalize())

    # Display basic info
    tk.Label(info_window, text=f"Name: {pokemon_data['name'].capitalize()}").pack()
    tk.Label(info_window, text=f"Height: {pokemon_data['height']}").pack()
    tk.Label(info_window, text=f"Weight: {pokemon_data['weight']}").pack()

    # Display types
    types = ", ".join([t['type']['name'].capitalize() for t in pokemon_data['types']])
    tk.Label(info_window, text=f"Types: {types}").pack()

    # Display image (if available)
    sprite_url = pokemon_data['sprites']['front_default']
    if sprite_url:
        try:
            image_data = requests.get(sprite_url).content
            image = Image.open(io.BytesIO(image_data))
            image = image.resize((100, 100), Image.LANCZOS) # Resize for display
            photo = ImageTk.PhotoImage(image)
            image_label = tk.Label(info_window, image=photo)
            image_label.image = photo # Keep a reference
            image_label.pack()
        except Exception as e:
            print(f"Error loading image: {e}")

def dispense_pokemon():
    """Handles the 'dispense' action."""
    pokemon_name = entry.get()
    if pokemon_name:
        data = get_pokemon_info(pokemon_name)
        display_pokemon_info(data)
    else:
        messagebox.showwarning("Input Error", "Please enter a Pokémon name.")

# Main window setup
root = tk.Tk()
root.title("Pokémon Dispenser")

# Input field
tk.Label(root, text="Enter Pokémon Name:").pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Dispense button
dispense_button = tk.Button(root, text="Dispense Pokémon", command=dispense_pokemon)
dispense_button.pack(pady=10)

root.mainloop()