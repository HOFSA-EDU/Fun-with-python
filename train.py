import time
import os
import sys

# ASCII-Zug (kann angepasst werden)
train = r"""
      ====        ________                ___________ 
  _D _|  |_______/  2GIN  \__I_I_____===__|_________| 
   |(_)---  |   H\___<3___/ |   |        =|___ ___|   
   /     |  |   H  |  |     |   |         ||_| |_||   
  |      |  |   H  |__--------------------| [___] |   
  | ________|___H__/__|_____/[][]~\_______|       |   
  |/ |   |-----------I_____I [][] []  D   |=======|__
__|_|___|________________________________|__________|_
"""

# Terminal-Größe holen
def get_terminal_width():
    return os.get_terminal_size().columns

def clear_line():
    sys.stdout.write("\r" + " " * get_terminal_width())
    sys.stdout.flush()

def move_train():
    width = get_terminal_width()
    train_lines = train.strip("\n").split("\n")
    train_height = len(train_lines)
    train_length = max(len(line) for line in train_lines)

    for offset in range(width + train_length):
        clear_screen()
        for line in train_lines:
            space = " " * max(0, width - offset)
            print(space + line)
        time.sleep(0.05)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Endlos-Fahrt (Strg+C zum Abbrechen)
try:
    while True:
        move_train()
except KeyboardInterrupt:
    print("\nZugfahrt beendet.")