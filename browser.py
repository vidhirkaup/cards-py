import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))

# https://stackoverflow.com/questions/44773601/getting-a-400-bad-request-error-using-socket-in-python-3?rq=1

# as per tutorial - this does not work
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()

# Option 1 - as per https://stackoverflow.com/questions/44773601/getting-a-400-bad-request-error-using-socket-in-python-3?rq=1
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

# Option 2 - as per same link
# cmd = 'GET /romeo.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode()

mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysocket.close()
