import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1000, 600
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokémon Center Storage Box")
clock = pygame.time.Clock()

# Fonts and Colors
FONT = pygame.font.SysFont("arial", 25)
BIG_FONT = pygame.font.SysFont("arial", 32, bold=True)
LIGHT_BLUE= (102, 180, 162) #background
GRAY = (220, 220, 220)
DARK_GRAY = (50, 50, 50)
GREEN = (150, 255, 150)
TEAL = (33, 172, 172)
SHINY_COLOR = (255, 215, 0)

# Your Pokémon item list
pokemon_items = [
    "Rayquaza", "Blastoise", "Bulbasaur", 
    "Charmander", "Charizard", "Charmeleon",
    "Christmas Pikachu", "Christmas Dratini", "Christmas Psyduck",
    "Christmas Vulpix", "Christmas Gengar", "Christmas Digglet"
]

# State
selected_index = None
dispensed_text = ""

# Button
button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 90, 200, 50)

# Draw UI
def draw_ui():
    screen.fill(LIGHT_BLUE)

    # Title
    title = BIG_FONT.render("Select a Pokémon", True, DARK_GRAY)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))

    # Draw Pokémon item grid
    for i, name in enumerate(pokemon_items):
        x = 80 + (i % 4) * 220
        y = 80 + (i // 4) * 100
        rect = pygame.Rect(x, y, 200, 60)
        color = GREEN if i == selected_index else GRAY
        pygame.draw.rect(screen, color, rect, border_radius=10)

        text = FONT.render(name, True, DARK_GRAY)
        screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))

    # Draw dispense button
    pygame.draw.rect(screen, TEAL, button_rect, border_radius=10)
    btn_text = FONT.render("Dispense Pokémon", True, DARK_GRAY)
    screen.blit(btn_text, (button_rect.centerx - btn_text.get_width() // 2,
                           button_rect.centery - btn_text.get_height() // 2))

    # Show result
    if dispensed_text:
        result = BIG_FONT.render(dispensed_text, True, SHINY_COLOR if "Shiny" in dispensed_text else DARK_GRAY)
        screen.blit(result, (WIDTH // 2 - result.get_width() // 2, HEIGHT - 40))

    pygame.display.flip()

# Dispense statements
def dispense_pokemon():
    global dispensed_text
    if selected_index is None:
        dispensed_text = "No Pokémon selected!"
        return
    name = pokemon_items[selected_index]
    is_shiny = random.randint(1, 25) == 1
    dispensed_text = f" Dispensing: {'✨ Shiny ' if is_shiny else ''}{name}!"

# Main game loop
def main():
    global selected_index
    running = True

    while running:
        clock.tick(FPS)
        draw_ui()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos

                # Pokémon selection
                for i, name in enumerate(pokemon_items):
                    x = 80 + (i % 4) * 220
                    y = 80 + (i // 4) * 100
                    rect = pygame.Rect(x, y, 200, 60)
                    if rect.collidepoint(mx, my):
                        selected_index = i

                # Dispense button
                if button_rect.collidepoint(mx, my):
                    dispense_pokemon()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

    #add search button
    # add sprites
    # change palette