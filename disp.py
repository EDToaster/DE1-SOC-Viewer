import sys
import pygame
from pygame.locals import *
from pygame import gfxdraw
import time

class Event:
    pass

class TimeStamp(Event):
    def __init__(self, at: int):
        self.at = at

    def __repr__(self):
        return f"Time Stamp at {self.at}"

class State(Event):
    def __init__(self, identifier: str, state: list):
        self.identifier = identifier
        self.state = state

    def __repr__(self):
        return f"State change for {self.identifier} to {self.state}"

class LED():
    def __init__(self, vertices, inverted):
        self.vertices = vertices
        self.inverted = inverted
        self.state = 1.0 if inverted else 0.0

    def __repr__(self):
        return repr(self.vertices)

class Display():
    def __init__(self):

        self.cluster = {}

        with open("show.define", "r") as fp:

            current_id = None
            inverted = None

            for line in fp:
                if(line.startswith("_")):
                    split = line.split(" ")
                    current_id = split[0][1:]
                    inverted = int(split[1]) == 1

                    self.cluster[current_id] = []
                else:
                    split = line.split(" ")
                    vertices = []
                    for i in range(len(split) // 2):
                        x = int(split[i * 2])
                        y = int(split[i * 2 + 1])
                        vertices.append((x,y))
                    
                    self.cluster[current_id].append(LED(vertices, inverted))

    def show(self, events):
        pygame.init()

        size = width, height = 700, 573

        screen = pygame.display.set_mode(size)
        BACK = (51, 51, 51)
        RED = (255, 0, 0)
        skin = pygame.image.load("skin.jpg")
        skinrect = skin.get_rect()

        control_surface = pygame.Surface(size, pygame.SRCALPHA)

        curr = 0

        for event in events:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if isinstance(event, State):
                print(f"{event.identifier}\t{event.state}")
                for i, j in enumerate(self.cluster[event.identifier]):
                    j.state = event.state[i]
                pass
            elif isinstance(event, TimeStamp):
                
                time.sleep((event.at - curr) / 1000)
                curr = event.at
                continue

            screen.fill(BACK)
            control_surface.fill((0,0,0,0))
            screen.blit(skin, skinrect)

            for _, item in self.cluster.items():
                for segment in item:
                    fill = RED + (((1 - segment.state) if segment.inverted else (segment.state)) * 255,)
                    pygame.gfxdraw.aapolygon(control_surface, tuple(segment.vertices), fill)
                    pygame.gfxdraw.filled_polygon(control_surface, tuple(segment.vertices), fill)
            screen.blit(control_surface, skinrect)
            pygame.display.flip()

if __name__ == "__main__":
    Display().show()
