import http.server
import socketserver

PORT = 8000

# Change the directory to where your index.html is located
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"Serving at http://localhost:{PORT}")
httpd.serve_forever()
