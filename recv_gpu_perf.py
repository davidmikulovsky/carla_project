import sys
import zmq

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from gpu performance monitor server ")
print("gpu_name,timestamp,utilization.gpu,utilization.memory,memory.total,memory.used")

socket.connect("tcp://esgteaching.cs.hut.fi:20009")

socket.setsockopt(zmq.SUBSCRIBE, '')
while True:
    string = socket.recv_string()
    print(str(string))
