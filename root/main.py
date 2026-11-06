import pygame

def run_sim():
    centre = (400, 300)
    radius = 50
    fill_colour = (70, 150, 240)
    stroke_colour = (20, 30, 50)
    stroke_width = 4

    # Fill first, then draw the outline over the fill.
    pygame.draw.circle(screen, fill_colour, centre, radius, width=0)
    pygame.draw.circle(screen, stroke_colour, centre, radius, width=stroke_width)


# Prepare Pygame and create the drawing surface.
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Project")
clock = pygame.time.Clock()
running = True

while running:
    # Handle the window's events each frame.
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Clear the old frame, then draw the new one.
    screen.fill((30, 30, 40))
    run_sim()
    pygame.display.flip()
    clock.tick(60)  # Limit the loop to 60 frames per second.

pygame.quit()