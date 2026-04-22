import subprocess

def capture_packets(host):
    try:
        cmd = [
            "tshark",
            "-i", "any",
            "-f", f"host {host} and port 443",
            "-a", "duration:3",
            "-Y", "tls.handshake",
            "-T", "fields",
            "-e", "tls.handshake.type"
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip().split("\n")

    except Exception as e:
        return [f"Error: {str(e)}"]