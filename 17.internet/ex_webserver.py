# coding: utf-8

'''
  http.server 모듈
    - 초간단 웹서버
'''

from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        from urllib.parse import urlparse

        print('DoGet Call!!')
        parts = urlparse(self.path)
        print(parts.query)

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write('Complete 끝!!'.encode('utf-8'))


def main():
    try:
        server = HTTPServer(('localhost', 8080), MyHandler)
        print('started http server...')
        server.serve_forever()

    except KeyboardInterrupt:
        print('shutdown web server')
        server.socket.close()


if __name__ == '__main__':
    main()