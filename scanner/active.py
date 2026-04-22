import socket
import ssl

def get_tls_info(host):
    context = ssl.create_default_context()

    with socket.create_connection((host, 443), timeout=5) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            return {
                "tls_version": ssock.version(),
                "cipher": ssock.cipher(),
                "cert": ssock.getpeercert()
            }