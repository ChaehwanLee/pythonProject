import random
import time

def sendData(data):
    print('Send Data:', data);

while True:
    temp = 0;
    temp = random.randint(1,100);
    sendData(temp);
    time.sleep(3); # 3s