📶 Public Wi-Fi Security Analyzer

🚀 Project Overview

Public Wi-Fi Security Analyzer is a **Python-based web application** that scans nearby Wi-Fi networks and evaluates their security risks in real-time.

This tool helps users detect **unsafe public networks**, including open Wi-Fi and potential **Evil Twin attacks**, ensuring safer internet usage.


 🎯 Key Features

* 🔍 Scan nearby Wi-Fi networks using PyWiFi
* 🔐 Detect encryption type (Open / WPA / WPA2)
* ⚠️ Identify security risks:

  * Open networks (high risk)
  * Multiple BSSIDs (possible fake hotspot)
  * Signal strength variations
* 📊 Interactive dashboard with:

  * Total networks count
  * Safe / Moderate / High-risk classification
* 🔄 Real-time scanning with refresh option
* 🎨 Clean and responsive UI with graphs and tables

 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Networking:** PyWiFi
* **Frontend:** HTML, CSS
* **Concepts Used:** Cybersecurity, Network Analysis

🧠 How It Works

1. The application scans nearby Wi-Fi networks using PyWiFi
2. Networks are grouped based on SSID
3. For each network:

   * Encryption type is identified
   * Signal strengths are analyzed
   * Multiple access points (BSSID) are checked
4. A **risk score** is calculated
5. Results are displayed in a **dashboard UI**


⚠️ Risk Evaluation Logic

* **Open Network → High Risk (90%)**
* **Multiple BSSIDs + Signal variation → Possible Evil Twin**
* **Secure Network → Low Risk**

| Risk Score | Security Level |
| ---------- | -------------- |
| 0 – 39     | Safe           |
| 40 – 69    | Moderate       |
| 70 – 100   | High Risk      |


📂 Project Structure

public-wifi-analyzer/
│
├── app.py
├── templates/
│   └── new_index.html
├── README.md

▶️ How to Run the Project

1️⃣ Clone Repository

git clone https://github.com/Thontashirisha74/public-wifi-analyzer.git

2️⃣ Navigate to Project

cd public-wifi-analyzer

3️⃣ Install Dependencies

pip install flask pywifi

4️⃣ Run Application

python app.py

5️⃣ Open Browser

http://127.0.0.1:5000/


📊 Sample Output

* Displays all nearby Wi-Fi networks
* Shows encryption type, risk score, and warning
* Highlights unsafe networks in red
* Provides graphical risk distribution


 🔒 Security Insights Provided

* Detects **open networks vulnerable to attacks**
* Identifies **fake access points (Evil Twin attacks)**
* Helps users avoid insecure public Wi-Fi


🚀 Future Enhancements

* 🔔 Real-time alerts for high-risk networks
* 📡 Continuous background monitoring
* 📱 Mobile-friendly UI
* 📍 Location-based tracking of networks
* 🧠 Machine Learning-based risk prediction


