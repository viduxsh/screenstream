from vidstream import StreamingServer
import threading, socket, platform

if(platform.system()=='Windows'):
    hostname=socket.gethostname()
    local_ip=socket.gethostbyname(hostname)
else:
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip=s.getsockname()[0]

print(local_ip)
print("Write STOP to kill the streaming")

receiver=StreamingServer(local_ip, 9999)

t=threading.Thread(target=receiver.start_server)
t.start()

while input("")!='STOP':
    continue

receiver.stop_server()
