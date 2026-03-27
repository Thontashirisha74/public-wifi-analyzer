
from flask import Flask, render_template
import pywifi
import time
import os

app = Flask(__name__, template_folder='templates')

print("Template folder path:", os.path.abspath('templates'))

# Disable caching
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


def calculate_risk(encryption, signals, bssids):

    risk = 10
    warning = "Protected network"

    if encryption == "Open Network":
        risk = 90
        warning = "Open network – high risk of data theft"

    elif len(set(bssids)) > 1:
        signal_diff = max(signals) - min(signals)

        if signal_diff > 30:
            risk = 70
            warning = "Possible fake hotspot (Evil Twin)"
        else:
            risk = 20
            warning = "Multiple access points (normal)"

    return risk, warning


def scan_wifi():

    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    time.sleep(3)

    results = iface.scan_results()

    networks = {}

    for net in results:

        ssid = net.ssid if net.ssid else "Hidden Network"
        bssid = net.bssid
        signal = net.signal
        encryption = "Open Network" if not net.akm else "WPA/WPA2"

        if ssid not in networks:
            networks[ssid] = {
                "signals": [],
                "bssids": [],
                "encryption": encryption
            }

        networks[ssid]["signals"].append(signal)
        networks[ssid]["bssids"].append(bssid)

    final_list = []

    for ssid, data in networks.items():

        encryption = data["encryption"]
        signals = data["signals"]
        bssids = data["bssids"]

        risk, warning = calculate_risk(encryption, signals, bssids)

        if risk >= 70:
            security = "High Risk"
        elif risk >= 40:
            security = "Moderate"
        else:
            security = "Safe"

        final_list.append({
            "ssid": ssid,
            "encryption": encryption,
            "risk": risk,
            "security": security,
            "warning": warning
        })

    return final_list


@app.route("/")
def home():
    networks = scan_wifi()
    return render_template("new_index.html", networks=networks)
print("🔥 THIS IS MY APP.PY RUNNING 🔥")


if __name__ == "__main__":
    app.run(debug=True)