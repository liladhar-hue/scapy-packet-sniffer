# 🕵️ Scapy Packet Sniffer

A Python-based packet sniffer built using Scapy to capture and analyze network traffic in real-time.

## 🚀 Features

* Captures live packets
* Shows source & destination IP
* Detects protocol (TCP, UDP, ICMP)
* Displays ports and services
* Shows TCP flags
* Real-time timestamps

## 🛠️ Requirements

* Python 3
* Scapy

Install:

```bash
pip install scapy
```

## ▶️ Usage

```bash
sudo python3 packet_sniffer.py
```

## 📌 Example Output

```
[12:30:01] 192.168.1.5 --> 8.8.8.8 | TCP
 TCP src_port=54321 dst_port=443 (HTTPS) flags=S
```

## ⚠️ Note

Run with root privileges.

## 👨‍💻 Author

Liladhar Parihar
