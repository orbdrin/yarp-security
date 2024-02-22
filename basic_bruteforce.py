########################################
## Basic Password Breaker (Brute-Force)
## ------------------------------------
## A simple password guesser, for simplicity max length of the password is obtained from length of user input.
########################################

import itertools, string, time

def bruteforce_attack(password):
	chars = string.printable.strip()
	for i in range(1, len(password) + 1):
		for guess in itertools.product(chars, repeat=i):
			guess = ''.join(guess)
			if guess == password:
				return password;
	return None

password = input("[+] Enter Password to Break: ")
start_time = time.time()
guess = bruteforce_attack(password)
run_time = time.time() - start_time

if guess:
	print(f"[+] Operation Time: {run_time}s. Password is {guess}.")
else:
	print(f"[-] Operation Time: {run_time}s. Password was not broken.")