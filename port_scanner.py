#!/usr/bin/env python3

import socket
import argparse
import signal
import sys
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored
import ipaddress

open_sockets = []

def print_header():
    ascii_header = """
======================================== 
 ___  __  ___ _____  __   ___ __  __  _  
| _,\/__\| _ \_   _/' _/ / _//  \|  \| | 
| v_/ \/ | v / | | `._`.| \_| /\ | | ' | 
|_|  \__/|_|_\ |_| |___/ \__/_||_|_|\__|       

========================================
        Fast Python Port Scanner
        by tay
    """
    print(colored(ascii_header, 'cyan'))

def def_handler(sig, frame):
    print(colored(f"\n[!] Exiting...", 'red'))

    for s in open_sockets:
        s.close()

    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def get_arguments():
    parser = argparse.ArgumentParser(description='Fast TCP Port Scanner')
    parser.add_argument("-t", "--target", dest="target", required=True, help="Victim Target to scan (Ex: -t 192.168.1.1)")
    parser.add_argument("-p", "--port", dest="port", required=True, help="Port range to scan (Ex: -p 1-1000)")
    parser.add_argument("-w", "--workers", dest="workers", type=int, default=100, help="Number of threads to use (default: 100)")
    parser.add_argument("-o", "--output", dest="output", help="Output file to save results")
    options = parser.parse_args()

    return options.target, options.port, options.workers, options.output

def create_socket(ip_version=4):
    if ip_version == 4:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    else:
        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

    s.settimeout(0.5)
    open_sockets.append(s)

    return s

def port_scanner(port, host, ip_version=4):
    s = create_socket(ip_version)
    try:
        s.connect((host, port))
        service_name = socket.getservbyport(port, 'tcp') if port <= 1024 else 'Unknown'
        result = f"[+] The port {port} is open ({service_name})"
        return result
    except (socket.timeout, ConnectionRefusedError, OSError):
        return None
    finally:
        s.close()

def scan_ports(ports, target, workers, ip_version=4):
    results = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for result in executor.map(lambda port: port_scanner(port, target, ip_version), ports):
            if result:
                results.append(result)
                print(colored(result, 'green'), flush=True)

    return results

def parse_ports(ports_str):
    if '-' in ports_str:
        start, end = map(int, ports_str.split('-'))
        return range(start, end + 1)
    elif ',' in ports_str:
        return map(int, ports_str.split(','))
    else:
        return (int(ports_str),)

def validate_ip(target):
    try:
        ip = ipaddress.ip_address(target)
        return ip.version
    except ValueError:
        print(colored(f"\n[!] Wrong Ip address: {target}", 'red'))
        sys.exit(1)

def save_results(output_file, results):
    if output_file:
        try:
            with open(output_file, 'w') as f:
                for line in results:
                    f.write(line + '\n')
            print(colored(f"\n[+] Saved results in: {output_file}", 'yellow'))
        except Exception as e:
            print(colored(f"[!] The file can't be saved: {e}", 'red'))

def main():
    print_header()

    target, ports_str, workers, output_file = get_arguments()

    ip_version = validate_ip(target)
    ports = parse_ports(ports_str)
    
    print(colored(f"\n[+] Scanning {target} with {workers} threads...\n", 'cyan'))

    results = scan_ports(ports, target, workers, ip_version)
    
    if results:
        save_results(output_file, results)
    else:
        print(colored("[!] No open ports found", 'yellow'))

if __name__ == '__main__':
    main()
