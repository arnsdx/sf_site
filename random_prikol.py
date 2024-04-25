from random import choice
from string import ascii_letters
from time import sleep

try:
    cycle = ""
    print('Generating a random string...\n\n') 
    for sequence in range(51):
        print(cycle, end="\r")
        if sequence < 9:
            sleep(1)
        sleep(0.05)
        cycle += "".join(choice(ascii_letters) for i in range(1))

    pint("\n")
except NameError:
    print('Автор дурачок. [NameError]                              \n')