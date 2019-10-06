import threading

def startThread(func, args=tuple(), daemon=False):
    thread = threading.Thread(target=func, args=args, daemon=daemon)
    thread.start()


def startListenerThread(condition, func, args=tuple(), daemon=False):
    def listener():
        while True:
            while not condition():
                pass
            thread = threading.Thread(
                target=func, 
                args=args,
                daemon=daemon
            )
            thread.start()
            while condition():
                pass
    
    listener_thread = threading.Thread(target=listener, daemon=True)
    listener_thread.start()
