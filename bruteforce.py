####################
## A simple password guesser (Bruteforce).
## For simplicity we determine the max length from the password entered.
####################

from itertools import product
from datetime import datetime
import sys, string

# Bruteforce Function
def bruteforce(password):
    chars = string.printable.strip()
    for length in range(1, len(password) + 1):
        for guess in product(chars, repeat=length):
            guess = ''.join(guess)
            if guess == password:
                return guess
    return None

# User Input
try:
    password = input("[+] Enter Password to Guess: ")
except KeyboardInterrupt:
    print("\n[-] User Has Requested an Interrupt.")
    print("[-] Application Exiting.")
    sys.exit(1)

# Cracking Password
start_time = datetime.now()
guess = bruteforce(password)
stop_time = datetime.now()
total_time = stop_time - start_time

if guess:
    print("[+] Password is %s." % (guess))
    print("[+] Operation Duration: %s" % (total_time))
else:
    print("[-] Password was not broken.")
    print("[-] Operation Duration: %s" % (total_time))