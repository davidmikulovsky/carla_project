import sys
import zmq

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from cpu performance monitor server ")
print("time  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle")

socket.connect("tcp://esgteaching.cs.hut.fi:20008")

socket.setsockopt(zmq.SUBSCRIBE, '')
while True:
    string = socket.recv_string()
    print(str(string))
