####################
## A simple TCP port scanner.
####################

from socket import *
from datetime import datetime
import sys, time

# Scanning Function
def scan_target(target, port, r_code = 1):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        code = s.connect_ex((target, port))
        
        if code == 0:
            r_code = code
        
        s.close()
    except Exception:
        pass
    
    return r_code

# User Input
while True:
    try:
        target = input("[+] Enter Target Address: ")
        min_port = int(input("[+] Enter Port Range (Min): "))
        max_port = int(input("[+] Enter Port Range (Max): "))
        break
    except ValueError:
        print("\n[-] User Has Entered Invalid Input.\n")
    except KeyboardInterrupt:
        print("\n[-] User Has Requested an Interrupt.")
        print("[-] Application Exiting.")
        sys.exit(1)

# Determines Target IP Based on Address
targetip = gethostbyname(target)
print("\n[+] Target Address: %s | IP: %s" % (target, targetip))
print("[+] Scan Commenced at %s\n" % (time.strftime("%H:%M:%S")))
start_time = datetime.now()

# Port Scanning
for port in range(min_port, max_port):
    try:
        result = scan_target(target, port)

        if result == 0:
            print("[+] Port %d: Open" % (port))
    except Exception:
        pass

stop_time = datetime.now()
total_time = stop_time - start_time
print("\n[+] Scan Completed at %s" % (time.strftime("%H:%M:%S")))
print("[+] Scan Duration: %s" % (total_time))
