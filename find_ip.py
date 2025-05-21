import subprocess

# This script extracts the client IP from a DHCP ACK packet in a pcap file using tshark.

def extract_ip_from_dhcp(pcap_path):
    """
    Extracts the client IP (DHCP ACK recipient) from the first DHCP ACK packet in the pcap file.
    """
    try:
        command = [
            "tshark", "-r", pcap_path,
            "-Y", "bootp.option.dhcp == 5",
            "-T", "fields",
            "-e", "ip.dst"
        ]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        lines = result.stdout.strip().splitlines()
        if lines:
            return lines[0]  # Takes the first client IP found
        else:
            print(f"[WARNING] No DHCP ACK packet found in {pcap_path}")
            return None
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] tshark failed during DHCP extraction on {pcap_path}: {e}")
        return None