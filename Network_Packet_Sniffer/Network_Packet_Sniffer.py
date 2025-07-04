from scapy.all import sniff, IP, TCP, UDP

def process_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto

        print(f"\n[+] Packet:")
        print(f"    Source IP      : {src_ip}")
        print(f"    Destination IP : {dst_ip}")
        print(f"    Protocol       : {proto}")

        if TCP in packet or UDP in packet:
            payload = bytes(packet[TCP].payload) if TCP in packet else bytes(packet[UDP].payload)
            print(f"    Payload        : {payload[:50]}...")  # Display first 50 bytes

# Start sniffing
print("Starting packet sniffing... Press CTRL+C to stop.\n")
sniff(prn=process_packet, store=False)