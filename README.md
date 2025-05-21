# 📦 port-checker

### PCAP Port Analysis Tool

This script analyzes PCAP files to extract and count destination TCP and UDP ports per device.  
It outputs a JSON report with the results.

---

## 📁 Directory Structure Required

Before running the script, structure your main directory as follows:

```
main_pcap_folder/
│
├── pcap1/
│   ├── name.txt      # contains the name of the device (e.g., Laptop_Office)
|   ├── mac.txt       # contains the mac of the device (e.g, cc:8d:a2:a0:09:78)
│   └── *.pcap        # one or more PCAP files to analyze
│
├── pcap2/
│   ├── name.txt
|   ├── mac.txt       # contains the mac of the device (e.g, cc:8d:a2:a0:09:78)
│   └── *.pcap
│
...
```

Each subfolder must be named with the prefix `pcap` followed by a number (e.g., `pcap1`, `pcap2`, ...).

- `mac.txt`: contains the mac of the device.
- `name.txt`: contains a readable name for the device.
- One or more `.pcap` files must be present for analysis.

---

## 🛠️ Requirements

- Python 3.x
- **TShark** (part of Wireshark) installed and accessible via command line.

### Install TShark

<details>
<summary>Ubuntu/Debian</summary>

```bash
sudo apt install tshark
```
</details>

<details>
<summary>macOS (with Homebrew)</summary>

```bash
brew install wireshark
```
</details>

<details>
<summary>Windows</summary>

Download and install Wireshark from [https://www.wireshark.org/](https://www.wireshark.org/)  
Make sure **TShark** is added to your system's PATH.
</details>

---

## ▶️ How to Run the Script

1. Place the script in a folder of your choice together with find_ip.py, which finds the IP by analyzing communications between the device and the DHCP server.
2. Open a terminal or command prompt.
3. Run the script:

   ```bash
   python3 main.py
   ```

4. When prompted, enter the full path to your main directory:

   ```
   Enter the path of the main directory: /home/YOUR_USER/pcap_folder
   ```

---

## 📤 Output

After execution, a new folder named `log` will be created inside your main directory.  
It will contain one JSON file for each device analyzed:

```
main_pcap_folder/
├── log/
│   ├── port_analysis_1.json
│   ├── port_analysis_2.json
│   ...
```

Each JSON file includes:

- Device name and local IP
- Total number of different TCP/UDP ports found
- Ports used only once
- Full list of ports sorted by frequency

---

## 📝 Notes

- Private/internal IP addresses (e.g., `192.168.x.x`, `10.x.x.x`) are excluded from the analysis.
- Only:
  - **TCP packets** with the **SYN** flag and **no ACK** (new connections)
  - **All UDP packets**
  - **Packets** with the **mac IP** as **source**
  are considered.
