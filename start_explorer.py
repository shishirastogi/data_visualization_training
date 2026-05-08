import http.server
import socketserver
import json
import os
import urllib.parse
import webbrowser
import threading
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

HIDDEN_FILES = {'.git', '__pycache__', '.gitignore', 'start_explorer.py', 'explorer_ui', 'implementation_plan.md'}

class ExplorerHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        
        # API endpoint for listing files
        if parsed_path.path == '/api/files':
            query = urllib.parse.parse_qs(parsed_path.query)
            target_dir = query.get('dir', [''])[0]
            
            # Prevent directory traversal
            target_dir = os.path.normpath(target_dir).lstrip('\\/')
            if '..' in target_dir.split(os.sep):
                self.send_error(403, "Access denied")
                return
                
            full_path = os.path.join(DIRECTORY, target_dir)
            
            if not full_path.startswith(DIRECTORY):
                self.send_error(403, "Access denied")
                return
                
            if not os.path.exists(full_path) or not os.path.isdir(full_path):
                self.send_error(404, "Directory not found")
                return
                
            try:
                items = os.listdir(full_path)
                result = []
                
                # Add parent directory if not at root
                if full_path != DIRECTORY:
                    parent_rel = os.path.relpath(os.path.dirname(full_path), DIRECTORY)
                    if parent_rel == '.':
                        parent_rel = ''
                    result.append({"name": "..", "type": "directory", "path": parent_rel.replace('\\', '/')})
                    
                for item in items:
                    if item in HIDDEN_FILES or item.startswith('.'):
                        continue
                        
                    item_path = os.path.join(full_path, item)
                    rel_path = os.path.relpath(item_path, DIRECTORY)
                    
                    if os.path.isdir(item_path):
                        result.append({"name": item, "type": "directory", "path": rel_path.replace('\\', '/')})
                    else:
                        result.append({"name": item, "type": "file", "path": rel_path.replace('\\', '/')})
                        
                # Sort: directories first, then files
                result.sort(key=lambda x: (x['name'] != '..', x['type'] != 'directory', x['name'].lower()))
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(result).encode())
            except Exception as e:
                self.send_error(500, str(e))
                
        # API endpoint for reading file content
        elif parsed_path.path == '/api/file_content':
            query = urllib.parse.parse_qs(parsed_path.query)
            target_file = query.get('file', [''])[0]
            target_file = os.path.normpath(target_file).lstrip('\\/')
            
            if '..' in target_file.split(os.sep):
                self.send_error(403, "Access denied")
                return
                
            full_path = os.path.join(DIRECTORY, target_file)
            
            if not full_path.startswith(DIRECTORY) or not os.path.isfile(full_path):
                self.send_error(404, "File not found")
                return
                
            try:
                with open(full_path, 'rb') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/plain; charset=utf-8')
                self.end_headers()
                self.wfile.write(content)
            except Exception as e:
                self.send_error(500, str(e))
                
        # Serve frontend UI
        elif parsed_path.path == '/' or parsed_path.path == '/index.html':
            self.path = '/explorer_ui/index.html'
            super().do_GET()
        elif parsed_path.path == '/style.css':
            self.path = '/explorer_ui/style.css'
            super().do_GET()
        elif parsed_path.path == '/script.js':
            self.path = '/explorer_ui/script.js'
            super().do_GET()
        elif parsed_path.path.startswith('/explorer_ui/'):
            super().do_GET()
        else:
            self.send_error(403, "Direct file access via URL is forbidden. Use the explorer UI.")

def start_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), ExplorerHandler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    print("Opening browser...")
    webbrowser.open(f'http://localhost:{PORT}')
    
    print("Press Ctrl+C to stop the server.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)
