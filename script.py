import pygame

# Initialize Pygame
pygame.init()

# Set up window
window_size = (1000, 500)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Visualizacion de bola")

# Set up clock
clock = pygame.time.Clock()

# Define star parameters
star_color = (255, 0,0)
star_position = (250, 250)
star_radius = 50

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    window.fill((100, 0, 0))

    # Draw star
    pygame.draw.circle(window, star_color, star_position, star_radius)

    # Update display
    pygame.display.update()
    clock.tick(60)

# Quit game
pygame.quit()
