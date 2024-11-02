

# Fast Python Port Scanner


![image](https://github.com/user-attachments/assets/05d0e130-5268-4e36-be70-7cfde1fd0e01)


A simple and fast python TCP port scanner. This script allows you to scan a range of ports on a target IP address to identify open ports and their associated services.

## Features

- Fast scanning using multithreading
- Support for both IPv4 and IPv6
- Displays open ports and their corresponding services
- Optional output to a text file

## Requirements

- `termcolor` library (for colored output)

You can install the required library using pip:

```
pip3 install termcolor
```

## Usage

Run the script from the command line with the following arguments:

```
python3 port_scanner.py -t <target> -p <port_range> -w <workers> -o <output_file>
```

### Arguments

- `-t`, `--target`: The target IP address or hostname you want to scan (e.g., `-t 192.168.1.1`).
- `-p`, `--port`: The range of ports to scan (e.g., `-p 1-1000` or `-p 22,80,443`).
- `-w`, `--workers`: (Optional) The number of threads to use for scanning. Default is 100.
- `-o`, `--output`: (Optional) A file to save the results. If provided, open ports will be saved to this file.

### Example

To scan ports 1 through 1000 on the target IP `192.168.1.1` using 50 worker threads, you would run:

```
python port_scanner.py -t 192.168.1.1 -p 1-1000 -w 50
```

To save the results to a file named `results.txt`, you would run:

```
python port_scanner.py -t 192.168.1.1 -p 1-1000 -o results.txt
```
