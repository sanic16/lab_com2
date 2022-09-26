import threading

class CustomThread(threading.Thread):
    def run(self):
        print('Custom thread function.\n')

for i in range(3):
    t = CustomThread()
    t.start()