# Scapy-Spoofer
A single spoofer with Scapy library.
The next scripts are a brief example about spoofing attack and defense using Scapy.The firs one uses Scapy for ARP functions, more especifcally sends fake ARP packages to intercept network traffic from a target IP and using de IP Gateway, remembering that ARP works with MAC adresses we can spoofing devices on the same network.

To use the attack script we must activate sudo permissions; therefore prompt 'sudo' before the script execute command and then, insert IP target and IP Gateway:
![image](https://github.com/MarioCaudillo/Scapy-Spoofer/assets/110208641/0ac2a807-1cb5-43ea-aa3c-ac9bd6101859)


To use the defender script (honeypot) you must to prompt sudo for network permissions:
![image](https://github.com/MarioCaudillo/Scapy-Spoofer/assets/110208641/937f966e-7188-4851-b1ff-674cfe85533f)
When spoofing (changes on ARP table) is detected, a log message will appear on shell and a .txt file will be built on the path where script is located.
![image](https://github.com/MarioCaudillo/Scapy-Spoofer/assets/110208641/fb8bf8cc-2ba1-4203-b393-d20c924069bb)

A proof about how scripts should works:
![image](https://github.com/MarioCaudillo/Scapy-Spoofer/assets/110208641/b33177c3-f675-41b9-94db-74f260301ec1)

