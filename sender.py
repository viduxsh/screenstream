from vidstream import ScreenShareClient
import threading

ip=input("Server IP: ")
sender=ScreenShareClient(ip, 9999)

print("Write STOP to kill the streaming")

t=threading.Thread(target=sender.start_stream)
t.start()

while input("")!='STOP':
    continue

sender.stop_stream()
