#http://symfoware.blog68.fc2.com/blog-entry-885.html
#https://docs.python.jp/3/library/socketserver.html
#import SocketServer
import socketserver as SocketServer
import logging
#http://testpy.hatenablog.com/entry/2017/03/17/000626
#import cPickle, struct
import _pickle as cPickle
import struct
class SocketLogHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        print("connect from:", self.client_address)
        alldata = ""
        while True:
            chunk = self.request.recv(4)
            if len(chunk) < 4:
                break
                
            slen = struct.unpack(">L", chunk)[0]
            chunk = self.request.recv(slen)
            while len(chunk) < slen:
                chunk = chunk + self.request.recv(slen - len(chunk))
                    
#            obj = cPickle.loads(chunk)
            obj = cPickle.loads(chunk, encoding='utf-8')
            
            record = logging.makeLogRecord(obj)
            
#            print(unicode(record.msg, 'utf-8'))
            print(record.msg)
            
        
        self.request.close()
if __name__ == '__main__':
    
    server = SocketServer.ThreadingTCPServer(('localhost', 12345), SocketLogHandler)
    print('listening:', server.socket.getsockname())
    server.serve_forever()
