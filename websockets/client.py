#!/usr/bin/env python

"""Client using the threading API."""
import time

from websockets.sync.client import connect


def hello():
    with connect("ws://localhost:8765") as websocket:
        i = 0
        while True:
            websocket.send(f"Hello world {i}")
            message = websocket.recv()
            print(message)
            time.sleep(i)
            i+=1



if __name__ == "__main__":
    hello()