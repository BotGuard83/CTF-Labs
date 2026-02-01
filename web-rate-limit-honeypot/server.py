from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        self.send_error(405, "Method Not Allowed")

    def do_OPTIONS(self):
        self.send_error(501, "Unsupported method")

PORT = 8080

with TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
