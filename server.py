import os
import json
import datetime
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000
WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE_PATH = os.path.join(WORKSPACE_DIR, "login_audit.log")

import urllib.parse

class CustomHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Decode URL-encoded path (percent-encoding like %20 for spaces)
        decoded_path = urllib.parse.unquote(path)
        relative_path = decoded_path.lstrip('/')
        # Prevent path traversal outside workspace
        target = os.path.abspath(os.path.join(WORKSPACE_DIR, relative_path))
        if not target.startswith(os.path.abspath(WORKSPACE_DIR)):
            return os.path.join(WORKSPACE_DIR, "index.html")
        return target

    def do_POST(self):
        if self.path == '/log_login':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                login_data = json.loads(post_data.decode('utf-8'))
                username = login_data.get('username', 'Unknown')
                unit = login_data.get('unit', 'Office')
                
                # Get client IP address dynamically
                ip_address = self.client_address[0]
                
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Format log entry
                log_entry = f"[{timestamp}] User: {username} | Unit: {unit} | IP: {ip_address}\n"
                
                # Append to login_audit.log
                with open(LOG_FILE_PATH, 'a', encoding='utf-8') as f:
                    f.write(log_entry)
                
                # Send successful JSON response
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                response = {"status": "success", "message": "Login logged successfully."}
                self.wfile.write(json.dumps(response).encode('utf-8'))
                print(f"Logged login: {log_entry.strip()}")
            except Exception as e:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {"status": "error", "message": str(e)}
                self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        # Support CORS preflight requests
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

def run_server():
    os.chdir(WORKSPACE_DIR)
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, CustomHandler)
    print(f"=========================================================")
    print(f"   DLV THONG LO 2.0 - CUSTOM AUDITED WEB SERVER STARTED  ")
    print(f"=========================================================")
    print(f"Web portal:  http://localhost:{PORT}/index.html")
    print(f"Audit log:   {LOG_FILE_PATH}\n")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
