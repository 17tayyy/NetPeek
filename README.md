
## Requirements

- Python 3.x
- `termcolor` package (for colored output)

You can install the required package with:
```bash
pip install termcolor
````
## Usage
To run the script, you must specify the target and the port range to scan. The script accepts the following command-line arguments:

- -t or --target: The IP address or domain of the target to scan.
- -p or --port: The range of ports to scan. This can be specified as a range (e.g., 1-1000) or a comma-separated list (e.g., 22,80,443).

### Basic Usage

````bash
./port_scanner.py -t <target> -p <port-range>
````
### Examples

1. Scan ports 1 to 100 on target 192.168.1.1:
````bash
./port_scanner.py -t 192.168.1.1 -p 1-100
````

2. Scan specific ports (22, 80, 443) on target example.com:
````bash
./port_scanner.py -t example.com -p 22,80,443
````
