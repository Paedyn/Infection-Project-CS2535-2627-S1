import pygame
import random


def run_sim():
    fill_colour = (70, 150, 240)
    radius = (25)
    stroke_colour = (20, 30, 50)
    stroke_width = 4

    circles = [
        (100, 100), (250, 100), (400, 100), (550, 100), (700, 100),
        (100, 250), (250, 250), (400, 250), (550, 250), (700, 250),
        (100, 400), (250, 400), (400, 400), (550, 400), (700, 400),
        (100, 550), (250, 550), (400, 550), (550, 550), (700, 550)
    ]

    # Fill first, then draw the outline over the fill.
    for centre in circles:
       pygame.draw.circle(screen, fill_colour, centre, radius, width=0)
    pygame.draw.circle(screen, stroke_colour, centre, radius, width=stroke_width)


# Prepare Pygame and create the drawing surface.
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Project")
clock = pygame.time.Clock()
running = True
colours = {"susceptible": (70, 150, 240), "infected": (240, 80, 80),
           "recovered": (80, 200, 120), "dead": (150, 150, 150)}
population = []
radius=(25)
for _ in range(50):
    velocity = pygame.Vector2(60, 0).rotate(random.uniform(0, 360))
    population.append({
        "x": random.randint(radius, screen.get_width() - radius),
        "y": random.randint(radius, screen.get_height() - radius),
        "x_speed": velocity.x, "y_speed": velocity.y,
        "status": "susceptible", "immune": False,
    })

def run_sim():
    seconds = clock.get_time() / 1000
    for circles in population:
        if person["status"] != "dead":
            person["x"] += person["x_speed"] * seconds
            person["y"] += person["y_speed"] * seconds
        colour = colours[person["status"]]
    pygame.draw.circle(screen, colour, (person["x"], person["y"]), radius)

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