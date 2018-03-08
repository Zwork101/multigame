from json import load
from uuid import uuid4, uuid5

from quicknet.event import ClientWorker
from quicknet.server import QServer

with open('settings.json') as file:
    SETTINGS = load(file)
PLAYERS = {}
server = QServer(SETTINGS['port'])


@server.on("CONNECTION")
def new_connection(_, addr):
    print(f"New Connection from {addr}")
    client_id = str(uuid5(uuid4(),
                          SETTINGS['secret']))  # Prevent timing attacks
    ClientWorker.emit("WELCOME",
                      SETTINGS['welcome_msg'], client_id, PLAYERS)
    PLAYERS[client_id] = [SETTINGS['window_size'][0] / 2, SETTINGS['window_size'][1] / 2]
    server.broadcast("NEW_PLAYER", client_id, PLAYERS[client_id])
    ClientWorker.info["id"] = client_id


@server.on("MOVE")
def move_player(dir):
    if dir == "UP":
        PLAYERS[ClientWorker.info["id"]][1] -= 10
    elif dir == "DOWN":
        PLAYERS[ClientWorker.info["id"]][1] += 10
    elif dir == "LEFT":
        PLAYERS[ClientWorker.info["id"]][0] -= 10
    elif dir == "RIGHT":
        PLAYERS[ClientWorker.info["id"]][0] += 10
    server.broadcast("PLAYER_MOVED", ClientWorker.info["id"],
                     PLAYERS[ClientWorker.info["id"]])


server.run(SETTINGS["max_clients"])
