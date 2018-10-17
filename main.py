#!/usr/bin/env python3

import sys
import re
from disp import *



def construct(split: list, display: Display) -> Event:
        if re.match(r"^@[0-9]+$", split[0]):
            return TimeStamp(int(split[0][1:]))
        elif(re.match(r"^[/0-9a-zA-Z_-]+$", split[0]) and re.match(r"^([a-zA-Z0-9]+)$", split[1])):
            split[0] = split[0].split("/")[2]
            if split[0] in display.cluster:
                state = split[1]
                
                state = list(reversed([(0.0 if i in "0" else 1.0 if i in "1" else 0.5) for i in state if i in "01zZxX"]))

                return State(split[0], state)
        else: return None

def main() -> None:
    if(len(sys.argv) != 2):
        print(f"Usage: python3 {sys.argv[0]} filename")
        exit(1)

    events = []

    display = Display()

	
    with open(sys.argv[1]) as fp:
        time = None

        for line in fp:
            if(len(line) == 0): continue

            split = line.split(" ")
            if(len(split) != 2): continue

            constructed = construct(split, display)
            if isinstance(constructed, TimeStamp):
                time = constructed
            elif isinstance(constructed, State): 
                if time is not None:
                    events.append(time)
                time = None
                events.append(constructed)
            else: continue

    display.show(events)


if __name__ == "__main__":
    main()