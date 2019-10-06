import asyncexec as ae
import time

x = 0

def onFive():
    time.sleep(1)
    print('YAY')

ae.startListenerThread(lambda:x == 5, onFive)

x = 5
print(x)
time.sleep(.05)
x = 6
print(x)
time.sleep(.05)
x = 5
print(x)
time.sleep(.05)
x = 6
print(x)
time.sleep(.05)
x = 5
print(x)
time.sleep(.05)
x = 6
print(x)
time.sleep(.05)