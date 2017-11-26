#http://symfoware.blog68.fc2.com/blog-entry-885.html
#https://docs.python.jp/3/library/http.server.html
import http.server
#from BaseHTTPServer import BaseHTTPRequestHandler
import cgi
class PostHandler(http.server.BaseHTTPRequestHandler):
    
    def do_POST(self):
        # POST されたフォームデータを解析する
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        # レスポンス開始
        self.send_response(200)
        self.end_headers()
        # フォームに POST されたデータを表示する
        for field in form.keys():
            field_item = form[field]
            print('%s=%s' % (field, form[field].value))


if __name__ == '__main__':
#    from BaseHTTPServer import HTTPServer
    server = http.server.HTTPServer(('localhost', 8080), PostHandler)
    server.serve_forever()
