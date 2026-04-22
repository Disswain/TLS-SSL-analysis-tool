def analyze_security(cert, cipher, tls):
    issues = []

    if cert["is_expired"]:
        issues.append("Expired Certificate")

    if tls in ["TLSv1", "TLSv1.1"]:
        issues.append("Deprecated TLS Version")

    weak = ["RC4", "DES", "3DES"]
    if any(w in cipher["name"] for w in weak):
        issues.append("Weak Cipher")

    if not issues:
        risk = "Low"
    elif len(issues) == 1:
        risk = "Medium"
    else:
        risk = "High"

    return {
        "issues": issues,
        "risk": risk
    }