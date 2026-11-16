import pygame

def run_sim():
    centre = (400, 300)
    radius = 50
    fill_colour = (70, 150, 240)
    stroke_colour = (20, 30, 50)
    stroke_width = 4

    circles = [
        (100, 100), (250, 100), (400, 100), (550, 100), (700, 100),
        (100, 250), (250, 250), (400, 250), (550, 250), (700, 250),
        (100, 400), (250, 400), (400, 400), (550, 400), (700, 400)
    ]

    # Fill first, then draw the outline over the fill.
   for center in circles
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