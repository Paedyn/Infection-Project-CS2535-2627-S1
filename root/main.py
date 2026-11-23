import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Plague Simulator")
clock = pygame.time.Clock()

running = True

colours = {
    "susceptible": (70, 150, 240),
    "infected": (240, 80, 80),
    "recovered": (80, 200, 120),
    "dead": (150, 150, 150)
}

radius = 25
infection_percentage=0.5
infection_radius=radius*1.5

circles = [
    (100, 100), (250, 100), (400, 100), (550, 100), (700, 100),
    (100, 250), (250, 250), (400, 250), (550, 250), (700, 250),
    (100, 400), (250, 400), (400, 400), (550, 400), (700, 400),
    (100, 550), (250, 550), (400, 550), (550, 550), (700, 550)
]

population = []

for centre in circles:

    velocity = pygame.Vector2(300, 0)
    velocity = velocity.rotate(random.randint(0, 360))

    person = {
        "x": centre[0],
        "y": centre[1],
        "x_speed": velocity.x,
        "y_speed": velocity.y,
        "status": "susceptible"
    }

    population.append(person)
    population[0]["status"] = "infected"
#SUSPECTIBLE IF WITHINT INFECTED RADIUS
for infected in population:
     if infected["status"] == "infected":
         for susceptible in population:
             if susceptible["status"] == "susceptible":
                  x_distance = infected["x"] - susceptible["x"]
                  y_distance = infected["y"] - susceptible["y"]
                  distance = math.sqrt(x_distance ** 2 + y_distance ** 2)
                  if distance <= infection_radius:
                      if random.random() < infection_percentage:
                          susceptible["status"] = "infected"


def run_sim():

    seconds = clock.get_time() / 1000

    for person in population:

        person["x"] = person["x"] + person["x_speed"] * seconds
        person["y"] = person["y"] + person["y_speed"] * seconds

        if person["x"] <= radius:
            person["x_speed"] = abs(person["x_speed"])

        if person["x"] >= screen.get_width() - radius:
            person["x_speed"] = -abs(person["x_speed"])

        if person["y"] <= radius:
            person["y_speed"] = abs(person["y_speed"])

        if person["y"] >= screen.get_height() - radius:
            person["y_speed"] = -abs(person["y_speed"])

        colour = colours[person["status"]]

        pygame.draw.circle(
            screen,
            colour,
            (int(person["x"]), int(person["y"])),
            radius
        )


while running:

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.quit:
            running = False
            seconds_per_day = 5.0
            calendar = {"day": 0, "elapsed_seconds": 0.0}


            def run_sim():
                seconds = clock.get_time() / 1000
                calendar["elapsed_seconds"] += seconds


                while calendar["elapsed_seconds"] >= seconds_per_day:
                    calendar["elapsed_seconds"] -= seconds_per_day
                    calendar["day"] += 1
                    print(f"Day {calendar['day']} completed")


                pygame.display.set_caption(f"Simulation day: {calendar['day']}")

    screen.fill((30, 30, 40))

    run_sim()

    pygame.display.flip()

    clock.tick(200)

pygame.quit()