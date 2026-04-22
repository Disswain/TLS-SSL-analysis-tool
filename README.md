# TLS-SSL-analysis-tool

A modular Python-based cybersecurity tool that analyzes the security posture of HTTPS servers by inspecting TLS configurations, certificates, cipher suites, and handshake behavior.

---

## 🚀 Features

* 🔍 Certificate validation (issuer, subject, expiry)
* 🔐 Cipher suite analysis (detect weak encryption)
* 📡 TLS version inspection (identify deprecated protocols)
* 🧪 Packet-level TLS handshake capture using tshark
* ⚠️ Rule-based vulnerability detection engine
* 📊 Risk classification (Low / Medium / High)
* 📁 JSON report generation

---

## 🛠️ Tech Stack

* Python (`socket`, `ssl`)
* OpenSSL (for TLS concepts and validation)
* Wireshark / tshark (packet capture & analysis)

---

## 📁 Project Structure

```
tls-analyzer/
│
├── scanner/
│   ├── active.py      # TLS connection + certificate extraction
│   ├── capture.py     # tshark-based packet capture
│   ├── parser.py      # parse TLS & certificate data
│   ├── analyzer.py    # rule engine (detect weak configs)
│   └── report.py      # output + JSON reporting
│
├── cli.py             # main entry point
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

```bash
git clone https://github.com/Disswain/TLS-SSL-analysis-tool.git
cd TLS-SSL-analysis-tool
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python cli.py example.com
```

---

## 🧠 How It Works

1. Takes a domain as input
2. Establishes a TLS connection using Python
3. Extracts certificate and cipher details
4. Captures handshake packets using tshark
5. Parses and analyzes security parameters
6. Detects vulnerabilities using rule-based logic
7. Generates a structured report

---

## ⚠️ Security Checks Performed

* Expired or invalid certificates
* Weak cipher suites (RC4, DES, 3DES)
* Deprecated TLS versions (TLS 1.0, 1.1)
* TLS handshake behavior analysis

---

## 📊 Sample Output

```
🔍 TLS Security Report
========================================
Domain: ex.com

TLS Version: TLSv1.3
Cipher: TLS_AES_256_GCM_SHA384

Certificate:
Issued To: example.com
Issued By: DigiCert Inc
Expired: False

Handshake Packets: 5

Issues Found:
✅ No major issues

Risk Level: Low
```

---

## 🎯 Key Learning Outcomes

* Hands-on understanding of TLS/SSL protocols
* Certificate trust chain validation
* Cipher suite and encryption analysis
* Packet-level inspection using Wireshark
* Building modular cybersecurity tools

---

## 🔮 Future Improvements

* Multi-domain scanning
* CLI flags (`--json`, `--verbose`)
* HSTS & OCSP checks
* GUI dashboard
* Integration with vulnerability scanners

---

## 👨‍💻 Author

Disita Swain
Cybersecurity Enthusiast
