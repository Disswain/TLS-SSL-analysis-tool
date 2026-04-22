import json

def print_report(domain, tls, cipher, cert, analysis, handshake):
    print("\n🔍 TLS Security Report")
    print("=" * 40)
    print("Domain:", domain)

    print("\nTLS Version:", tls)
    print("Cipher:", cipher["name"])

    print("\nCertificate:")
    print("Issued To:", cert["issued_to"])
    print("Issued By:", cert["issued_by"])
    print("Expired:", cert["is_expired"])

    print("\nHandshake Packets:", handshake["count"])

    print("\nIssues Found:")
    if analysis["issues"]:
        for i in analysis["issues"]:
            print("❌", i)
    else:
        print("✅ No major issues")

    print("\nRisk Level:", analysis["risk"])


def save_json(data, filename="report.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)