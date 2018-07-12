import threading
import time


def thread_a():
    lock_A.acquire()
    print("Thread a1 is run")
    lock_B.acquire()
    print("Thread a2 is run")
    lock_B.release()
    lock_A.release()


def thread_b():
    lock_B.acquire()
    print("Thread b1 is run")
    time.sleep(2)  # 暂停2s后 这里锁了B A被thread_a锁着
    lock_A.acquire()
    print("Thread b2 is run")
    lock_B.release()
    lock_A.release()


if __name__ == '__main__':
    lock_A = threading.Lock()
    lock_B = threading.Lock()
    for i in range(2):
        t_a = threading.Thread(target=thread_a)
        t_b = threading.Thread(target=thread_b)
        t_a.start()
        t_b.start()
