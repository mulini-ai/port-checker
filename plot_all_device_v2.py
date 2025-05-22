import os
import json
import matplotlib.pyplot as plt

# This script generates bar plots of the most contacted TCP and UDP ports
# from the JSON files created by the PCAP analysis script.

def load_json_data(log_dir):
    """
    Loads all JSON result files from the given log directory.
    """
    data_files = [f for f in os.listdir(log_dir) if f.startswith("port_analysis_") and f.endswith(".json")]
    data = []

    for file in data_files:
        file_path = os.path.join(log_dir, file)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = json.load(f)
                data.append(content)
        except Exception as e:
            print(f"[ERROR] Failed to read {file}: {e}")
    
    return data

def plot_top_ports(port_data, protocol, device_name, top_n=10, output_dir="plots"):
    """
    Creates and saves a bar plot for the top N contacted ports (TCP or UDP).
    """
    ports = port_data.get("ports", [])[:top_n]
    if not ports:
        print(f"[INFO] No {protocol.upper()} ports to plot for {device_name}")
        return

    port_numbers = [str(p[0]) for p in ports]
    counts = [p[1] for p in ports]

    plt.figure(figsize=(10, 6))
    plt.bar(port_numbers, counts, color='skyblue' if protocol == 'tcp' else 'lightgreen')
    plt.xlabel(f"{protocol.upper()} Destination Port")
    plt.ylabel("Connection Count")
    plt.title(f"{device_name} - Top {top_n} {protocol.upper()} Ports")
    plt.xticks(rotation=45)
    plt.tight_layout()

    os.makedirs(output_dir, exist_ok=True)
    filename = f"{device_name.replace(' ', '_')}_{protocol}_top{top_n}.png"
    filepath = os.path.join(output_dir, filename)
    plt.savefig(filepath)
    plt.close()

    print(f"[SUCCESS] Plot saved to {filepath}")

def main():
    """
    Main entry point for the plotting script.
    Prompts the user for the log directory containing the JSON files.
    """
    print("== Port Usage Plot Generator ==")
    log_dir = input("Enter the path of the 'log' directory containing the JSON files: ").strip()

    if not os.path.isdir(log_dir):
        print(f"[ERROR] The folder '{log_dir}' does not exist.")
        return

    data = load_json_data(log_dir)

    for device in data:
        device_name = device.get("device_name", "unknown_device")
        plot_top_ports(device.get("tcp", {}), "tcp", device_name)
        plot_top_ports(device.get("udp", {}), "udp", device_name)

if __name__ == "__main__":
    main()

