import json
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime

DECOY_PATHS = ["/.decoy", "/.decoy/", "/.decoy/credentials.txt", "/.decoy/admin.html"]

REQUEST_LOG = {}
BANNED_IPS = {}

RATE_LIMIT = 10
WINDOW = 10
BAN_TIME = 60

class SecureHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        ip = self.client_address[0]
        now = time.time()

        # 1 Check if IP is banned
        if ip in BANNED_IPS:
            if now < BANNED_IPS[ip]:
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b"IP temporarily banned. Try later.")
                return
            else:
                del BANNED_IPS[ip]

        # 2 Track requests
        REQUEST_LOG.setdefault(ip, [])
        REQUEST_LOG[ip] = [t for t in REQUEST_LOG[ip] if now -t < WINDOW]
        REQUEST_LOG[ip].append(now)

        # 3 Enforce rate limit
        if len(REQUEST_LOG[ip]) > RATE_LIMIT:
            BANNED_IPS[ip] = now + BAN_TIME
            self.send_response(429)
            self.end_headers()
            self.wfile.write(b"Too many requests. You are temporarily banned.")
            return
        # 4  HoneyPot / Decoy detection
        if self.path.startswith("/.decoy"):
            event = {
                "timestamp": datetime.utcnow().isoformat() + "2",
                "source_ip": self.client_address[0],
                "path": self.path,
                "user_agent": self.headers.get("User-Agent", "unknown"),
                "event": "honeypot_hit"
            }

            with open("/home/bitguard/ctf_web/honeypot.log", "a") as f:
                f.write(json.dumps(event) + "\n")

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>Access Logged</h1><p>Your activity has been recorded.</p>")

        if self.path in DECOY_PATHS:
           self.send_response(200)
           self.send_header("Content-type", "text/html")
           self.end_headers()
           self.wfile.write(b"<h1>Access Logged</h1><p>Your activity has been recorded.</p>")

           with open("/home/botguard/ctf_web/honeypot.log", "a") as f:
               f.write(f"HONEYPOT HIT from {self.client_address[0]} -> {self.path}\n")
           return

        # 4 Allow request
        super().do_GET()



server = HTTPServer(("0.0.0.0", 8080), SecureHandler)
print("Secure server running on port 8080")
server.serve_forever()
