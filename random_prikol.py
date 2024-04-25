from random import choice
from string import ascii_letters, digits
from time import sleep

try:
    string = ascii_letters + digits
    cycle = ""
    print('Generating a random string...\n\n') 
    for sequence in range(51):
        print(cycle, end="\r")
        if sequence < 9:
            sleep(1)
        sleep(0.05)
        cycle += "".join(choice(string) for i in range(1))

    print("\n")
except NameError:
    print('Автор дурачок. [NameError]                              \n')