import threading


lock = threading.Lock()
lock.acquire()
lock.acquire()
print("lock")
lock.release()
lock.release()
