from http.server import SimpleHTTPRequestHandler
import os
import json
from urllib.parse import urlsplit, unquote

class Handler(SimpleHTTPRequestHandler):
    def send_json(self, data: dict, status: int = 200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile(json.dumps(data).encode('utf-8'))

