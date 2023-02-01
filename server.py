from http.server import BaseHTTPRequestHandler, HTTPServer
from sheepbot26 import token, get_uptime
import socket

hostName = socket.gethostbyname(socket.gethostname())
serverPort = 8080

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Sheepbot26</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        # setTimeout(function() {}, 1000);
        self.wfile.write(bytes("<script>function toggle_token() {var token = document.getElementById('token'); if(document.getElementById('token_button').innerHTML == 'Hide token'){ document.getElementById('token_button').innerHTML = 'Show token';} else{document.getElementById('token_button').innerHTML = 'Hide token'} if (token.style.display === 'none') {token.style.display = 'block';} else {token.style.display = 'none';}}</script>", "utf-8"))
        self.wfile.write(bytes("<h1>Welcome to sheepbot26</h1>", "utf-8"))
        self.wfile.write(bytes(f"<p id = 'uptime'>Uptime: {get_uptime()}<p>", "utf-8"))
        self.wfile.write(bytes(f"<p id = 'token'>Token: {token}</p> <button onclick='toggle_token()'><label id = 'token_button'>Hide token</label></button>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":      
    webServer = HTTPServer((hostName, serverPort), Server)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")