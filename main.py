from urllib.parse import urlparse
import validators, requests, socket

def scan_ports(hostname, specified_port=None):
    common_ports = [20, 21, 22, 23, 25, 53, 80, 110, 123, 143, 161, 194, 443, 465, 993, 995, 3306, 3389, 5900, 8080]
    open_ports = []
    if specified_port:
        ports_to_scan = [specified_port]
    else:
        ports_to_scan = common_ports 

    for port in ports_to_scan:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((hostname, port))
            if result == 0:
                open_ports.append(port)
    return open_ports

url = input("Enter URL: ")
if validators.url(url):
    try:
        res = requests.get(url, timeout=5)
        if not (200 <= res.status_code < 400):
            print(f"URL unreachable. Status code: {res.status_code}")
        else:
            parsed_url = urlparse(url)
            hostname = parsed_url.hostname
            port = parsed_url.port

            print(f"Port Scanning for the most commonly used ports...")
            open_ports = scan_ports(hostname, specified_port=port)
            
            if open_ports:
                print(f"Open ports: {', '.join(map(str, open_ports))}")
            else:
                print("No open ports found.")
    except requests.exceptions.SSLError as e:
        print(f"SSL certificate error: {e}")
    except requests.exceptions.ConnectionError:
        print("URL is unreachable")
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.RequestException as err:
        print(f"Invalid URL. Reason: {err}")
else:
    print("Invalid URL.")
