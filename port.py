import socket
import sys
import threading
import argparse

def banner():
    print(r"""
     █████╗      ██╗
    ██╔══██╗     ██║
    ███████║     ██║
    ██╔══██║██   ██║
    ██║  ██║╚█████╔╝
    ╚═╝  ╚═╝ ╚════╝ 
        Port Scanner
    """)
    print("-" * 40)
    print(" Author : AJ")
    print(" LinkedIn: https://www.linkedin.com/in/blue-aj")
    print(" Github : https://github.com/0xAj-Krishna")
    print(" Twitter : https://x.com/B1ue_Aj")
    print("-" * 40)

banner()


parser = argparse.ArgumentParser(description="Simple Multi-threaded Port Scanner")
parser.add_argument("target", help="Target host (IP or domain)")

parser.add_argument("-p", metavar="Port-Number", type=int, help="Scan a specific port (e.g., -p 80)")
parser.add_argument("-p-", metavar="Port-range", dest="portrange", nargs="?", const="all",
                    help="Scan a range (e.g., -p- 20-100) or all ports (if used without value)")

args = parser.parse_args()

try:
    target = socket.gethostbyname(args.target)
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit(1)

print(f"[+] Target: {args.target} ({target})")

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN")
    sock.close()

try:

    if args.p:
        print(f"[+] Scanning {target} on port {args.p}...\n")
        scan_port(args.p)
    elif args.portrange:
        if args.portrange == "all":
            start_port, end_port = 1, 65535
        else:
            try:
                start_port, end_port = args.portrange.split("-")
                start_port, end_port = int(start_port), int(end_port)
            except ValueError:
                print("[-] Invalid range format. Use: -p- 20-100")
                sys.exit(1)

        print(f"[+] Scanning {target} from port {start_port} to {end_port}...\n")
        for port in range(start_port, end_port + 1):
            thread = threading.Thread(target=scan_port, args=(port,))
            thread.start()

    else:
        print("[-] You must specify either -p (single port) or -p- (range/all).")
        sys.exit(1)

except KeyboardInterrupt:
    print("\n[-] Scan interrupted by user.")
    sys.exit(0)