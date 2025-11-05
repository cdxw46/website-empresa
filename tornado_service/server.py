#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse

HTML_PAYLOAD = Path("agent_details.html").read_text(encoding="utf-8")
HTML_BYTES = HTML_PAYLOAD.encode("utf-8")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == "/agent_details":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(HTML_BYTES)))
            self.end_headers()
            self.wfile.write(HTML_BYTES)
            return

        if parsed.path == "/collect":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK\n")
            print("[+] Collect:", self.path, flush=True)
            return

        self.send_response(404)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Not Found\n")

    def log_message(self, fmt, *args):
        print(self.address_string(), "-", fmt % args, flush=True)


def main():
    server = HTTPServer(("0.0.0.0", 8000), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
