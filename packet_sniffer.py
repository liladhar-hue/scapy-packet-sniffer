from scapy.all import *
from datetime import datetime

#protocol number to name 
PROTOCOL = {
        1: "ICMP",
        6: "TCP",
        17: "UDP"
        }
#port to service name 
PORTS = {
        80: "HTTP",
    443: "HTTPS",
    22: "SSH",
    53: "DNS",
    21: "FTP",
    3306: "MySQL"
}
def packet_handler(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto_num = packet[IP].proto

        proto_name = PROTOCOL.get(proto_num, f"UNKNOWN{proto_num}")

        #just for showing the time
        time_now = datetime.now().strftime("%H:%M:%S")

        print(f" [{time_now}] {src_ip} --> {dst_ip} | {proto_name} ")

        if packet.haslayer(TCP):
            dport=packet[TCP].dport
            sport=packet[TCP].sport
            flags=packet[TCP].flags
            service=PORTS.get(dport, "?")
            print(f" TCP src_port={sport} dst_port={dport} ({service}) flags={flags}")
        elif packet.haslayer(UDP):
            dport=packet[UDP].dport
            sport=packet[UDP].sport
            service=PORTS.get(dport, "?")
            print(f" UDP src_port={sport} dst_port={dport} ({service}) ")
        elif packet.haslayer(ICMP):
            print(f" ICMP type={packet[ICMP].type}")  #8=ping, 0 =reply

print("[+] Starting packet sniffing.....") 
print("[+] press Ctrl + C to stop sniffing!\n")

try:
    sniff(prn=packet_handler, store=False)
except KeyboardInterrpt:
    print("\n[+] Stopping sniffing....")


