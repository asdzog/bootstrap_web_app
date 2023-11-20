from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from page_content import html_content


hostname = 'localhost'
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    @staticmethod
    def __get_html_content():
        return html_content

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        with open("index.html", "r", encoding='utf-8') as f:
            page_content = f.read()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostname, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostname, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
