import os #Library for OS control and OS commands
import time #Library to set a timer
import signal
import sys
from datetime import datetime

#Create a objet to save monitored ARP table
arp_table = {}

#Function to send arp command
def get_arp_table():
    arp_output = os.popen('arp -n').read()
    return arp_output

#Function to parse arp table data
def parse_arp_table(arp_output):
    lines = arp_output.split('\n')
    arp_dict = {}
    #Parsing line per line from table
    for line in lines:
        if 'incomplete' in line or len(line) == 0 or line.startswith("Address"):
            continue
        parts = line.split()
        if len(parts) >= 4:
            ip = parts[0]
            mac = parts[2]
            arp_dict[ip] = mac
    return arp_dict

#Function for monitoring arp table every 10 seconds
def monitor_arp_table(interval=10):
    global arp_table
    try:
        while True:
            #Obtaining previous ARP table
            arp_output = get_arp_table()
            current_arp_table = parse_arp_table(arp_output)

            #Conditional to compare previous ARP table(10 sec ago) and current
            #If previous and current table are different, log an Alert message with 
            #datetime for print when was detected
            if arp_table and arp_table != current_arp_table:
                diff = set(arp_table.items()) ^ set(current_arp_table.items())
                for ip, mac in diff:
                    log_msg = f"[{datetime.now()}] ARP Spoofing detectado: IP {ip} ahora tiene MAC {mac}\n"
                    print(log_msg)
                    #Here we sent the logs messages on a .txt file for a posterior report!
                    with open("arp_spoofing_log.txt", "a") as log_file:
                        log_file.write(log_msg)
            
            arp_table = current_arp_table
            time.sleep(interval)#Finally we sent a timer to iterate operation every 10 sec
    except KeyboardInterrupt:
        print("\nMonitorización ARP detenida")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        interval = int(sys.argv[1])
    else:
        interval = 10  #10sec interval value defined
    
    monitor_arp_table(interval)
