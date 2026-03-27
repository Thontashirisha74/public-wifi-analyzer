import pywifi
from pywifi import const
import time

print("Scanning nearby WiFi networks...\n")

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

iface.scan()
time.sleep(3)

results = iface.scan_results()

seen_networks = set()

for network in results:

    ssid = network.ssid
    signal = network.signal

    if ssid in seen_networks:
        continue

    seen_networks.add(ssid)

    # Detect encryption type
    if network.akm:
        encryption = "WPA/WPA2"
        security = "Secure"
        warning = "Protected network"
    else:
        encryption = "Open Network"
        security = "Insecure"
        warning = "High risk of data theft"

    print("Network Name:", ssid if ssid else "Hidden Network")
    print("Signal Strength:", signal)
    print("Encryption:", encryption)
    print("Security Level:", security)
    print("Warning:", warning)
    print("-----------------------------------")