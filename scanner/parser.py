from datetime import datetime

def parse_certificate(cert):
    subject = dict(x[0] for x in cert.get('subject', []))
    issuer = dict(x[0] for x in cert.get('issuer', []))

    expiry = cert.get('notAfter')
    expiry_date = None

    if expiry:
        expiry_date = datetime.strptime(expiry, "%b %d %H:%M:%S %Y %Z")

    return {
        "issued_to": subject.get("commonName"),
        "issued_by": issuer.get("commonName"),
        "expiry": str(expiry_date) if expiry_date else None,
        "is_expired": expiry_date < datetime.utcnow() if expiry_date else None
    }


def parse_cipher(cipher):
    return {
        "name": cipher[0],
        "protocol": cipher[1]
    }


def parse_handshake(data):
    return {
        "handshake_steps": data,
        "count": len(data)
    }