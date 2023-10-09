import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ipv4_match = re.search (r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip.strip())
    if ipv4_match:
        if 0 < int(ipv4_match.group(1)) <= 255 and 0 <= int(ipv4_match.group(2)) <= 255 and 0 <= int(ipv4_match.group(3)) <= 255 and 0 <= int(ipv4_match.group(4)) <= 255:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()