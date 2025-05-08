# port-checker
==============================
 PCAP Port Analysis Tool
==============================
This script analyzes PCAP files to extract and count destination TCP and UDP ports per device. 
It outputs a JSON report with the results.
------------------------------
 Directory Structure Required
------------------------------
Before running the script, you must prepare a main directory structured as follows:
main_pcap_folder/
│
├── pcap1/
│   ├── ip.txt        -> contains the local IP of the device (e.g., 192.168.1.100)
│   ├── name.txt      -> contains the name of the device (e.g., Laptop_Office)
│   └── *.pcap        -> one or more PCAP files to analyze
│
├── pcap2/
│   ├── ip.txt
│   ├── name.txt
│   └── *.pcap
│
...
Each subfolder must be named with the prefix "pcap" followed by a number (e.g., pcap1, pcap2, ...).
- "ip.txt": contains the local IP address of the device recorded in the PCAPs.
- "name.txt": contains a readable name for the device.
- The folder must also contain one or more `.pcap` files to analyze.
------------------------------
 Requirements
------------------------------
- Python 3.x
- TShark (part of Wireshark) installed and accessible via command line.
To install TShark:
Ubuntu/Debian:
    sudo apt install tshark
macOS (with Homebrew):
    brew install wireshark
Windows:
    Download and install Wireshark from https://www.wireshark.org/, and ensure TShark is added to PATH.
------------------------------
 How to Run the Script
------------------------------
1. Place the script in a folder of your choice.
2. Open a terminal or command prompt.
3. Run the script with:
    python your_script_name.py
4. When prompted, enter the full path to your main directory (the one containing the pcap folders):
    Example:
    Enter the path of the main directory: C:\Users\YourName\Documents\pcap_data
------------------------------
 Output
------------------------------
After execution, a new folder named "log" will be created inside your main directory. 
This folder will contain one JSON file for each device analyzed:
main_pcap_folder/
├── log/
│   ├── port_analysis_1.json
│   ├── port_analysis_2.json
│   ...
Each JSON file contains:
- Device name and local IP
- Total number of different TCP/UDP ports found
- Ports used only once
- Full list of ports sorted by frequency
------------------------------
 Notes
------------------------------
- Private/internal IP addresses (e.g., 192.168.x.x, 10.x.x.x) are excluded from the analysis.
- Only TCP packets with SYN flag and no ACK (new connections) and all UDP packets are considered.
