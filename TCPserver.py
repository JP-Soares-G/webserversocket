#!/usr/bin/python
import socket
HOST = '192.0.2.21'
PORT = 80
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, client = tcp.accept()
    print 'Conectado por', client
    response_body = '<html><body>%s</body></html>' % (socket.gethostname())
    response_headers = {
        'Content-Type': 'text/html; enconding=utf8',
        'Content-Length': len(response_body),
        'Connection': 'Close',    
    }
    response_headers_raw = ''.join('%s: %s\n'% (k, v) for k, v in response_headers.iteritems())
    response_proto = 'HTTP/1.1'
    response_status = '200'
    response_status_text = 'OK'

    con.send('%s %s %s' % (response_proto, response_status, response_status_text))
    con.send('\n')
    con.send(response_headers_raw)
    con.send('\n')
    con.send(response_body)
    print 'Finalizando conexão do cliente', client
    con.close()
