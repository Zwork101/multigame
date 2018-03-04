from json import load

import pygame
from pygame.locals import KEYDOWN, K_DOWN, K_LEFT, K_RIGHT, K_UP, QUIT

from quicknet.client import QClient

with open('settings.json') as file:
    SETTINGS = load(file)
SELF = None
RUN = True
PLAYERS = {}
game_client = QClient(SETTINGS["ip_addr"], SETTINGS["port"])


@game_client.on("WELCOME")
def welcome_client(msg, id, players):
    global PLAYERS, SELF
    print(msg)
    PLAYERS = players
    SELF = id


@game_client.on("PLAYER_MOVED")
def move_player(player_name, rect):
    PLAYERS[player_name] = rect


@game_client.on("NEW_PLAYER")
def new_player(player_name, rect):
    print("New Player!", player_name)
    PLAYERS[player_name] = rect


pygame.init()
screen = pygame.display.set_mode(SETTINGS["window_size"])
pygame.display.set_caption("My ONLINE game!")
clock = pygame.time.Clock()
game_client.start()
print("Started socket client")

while RUN:
    for event in pygame.event.get():
        if event.type == QUIT:
            print("Exiting")
            RUN = False
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                game_client.call("MOVE", "UP")
            elif event.key == K_LEFT:
                game_client.call("MOVE", "LEFT")
            elif event.key == K_RIGHT:
                game_client.call("MOVE", "RIGHT")
            elif event.key == K_DOWN:
                game_client.call("MOVE", "DOWN")

    screen.fill((0, 0, 0))  # Clear the screen

    for player, rect in PLAYERS.items():
        if player == SELF:
            pygame.draw.rect(screen, (100, 100, 100), rect)
        else:
            pygame.draw.rect(screen, (200, 100, 200), rect)

    pygame.display.flip()
    clock.tick(30)

game_client.quit()
