import sys
from scanner.active import get_tls_info
from scanner.capture import capture_packets
from scanner.parser import parse_certificate, parse_cipher, parse_handshake
from scanner.analyzer import analyze_security
from scanner.report import print_report, save_json


def main():
    if len(sys.argv) < 2:
        domain = input("Enter domain: ")
    else:
        domain = sys.argv[1]

    print(f"\n🚀 Scanning {domain}...")

    tls_data = get_tls_info(domain)

    cert = parse_certificate(tls_data["cert"])
    cipher = parse_cipher(tls_data["cipher"])
    tls_version = tls_data["tls_version"]

    packets = capture_packets(domain)
    handshake = parse_handshake(packets)

    analysis = analyze_security(cert, cipher, tls_version)

    print_report(domain, tls_version, cipher, cert, analysis, handshake)

    save_json({
        "domain": domain,
        "tls": tls_version,
        "cipher": cipher,
        "certificate": cert,
        "handshake": handshake,
        "analysis": analysis
    })


if __name__ == "__main__":
    main()