from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            with open("./my_files/index.html", "r", encoding="utf-8") as f:
                response = f.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(response.encode("utf-8"))

    def do_POST(self):
        if self.path == "/submit":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            decoded_data = post_data.decode('utf-8')
            form_data = urllib.parse.parse_qs(decoded_data)

            name = form_data.get("name", [""])[0]

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            response = f"<h1>Вы отправили: {name}</h1>"
            self.wfile.write(response.encode("utf-8"))

def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Сервер запущен на порту', port)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
