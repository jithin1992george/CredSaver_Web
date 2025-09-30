# run_local.py
import http.server
import socketserver
import webbrowser
import os

PORT = 8085

# Serve files from the current directory
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving CredSaver_Web at http://localhost:{PORT}/CredSaver_Web.html")
    # Open default browser automatically
    webbrowser.open(f"http://localhost:{PORT}/CredSaver_Web.html")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()
