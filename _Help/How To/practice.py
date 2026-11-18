import pygame
import random
import random

radius = 6
colours = {"susceptible": (70, 150, 240), "infected": (240, 80, 80),
           "recovered": (80, 200, 120), "dead": (150, 150, 150)}
population = []
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
    for person in population:
        if person["status"] != "dead":
            person["x"] += person["x_speed"] * seconds
            person["y"] += person["y_speed"] * seconds
        colour = colours[person["status"]]
        pygame.draw.circle(screen, colour, (person["x"], person["y"]), radius)

radius = 6
colours = {"susceptible": (70, 150, 240), "infected": (240, 80, 80),
           "recovered": (80, 200, 120), "dead": (150, 150, 150)}
population = []
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
    for person in population:
        if person["status"] != "dead":
            person["x"] += person["x_speed"] * seconds
            person["y"] += person["y_speed"] * seconds
        colour = colours[person["status"]]
        pygame.draw.circle(screen, colour, (person["x"], person["y"]), radius)