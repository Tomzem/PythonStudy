import threading
import time

def do():
    semaphro.acquire()
    print("this is {0} set the semaphore".format(threading.current_thread().getName()))
    time.sleep(2)
    semaphro.release()
    print("\033[1;30mthi is {0} release the semaphore\033[0m".format(threading.current_thread().getName()))


if __name__ == "__main__":
    semaphro = threading.Semaphore(2)
    for i in range(10):
        t = threading.Thread(target=do)
        t.setName("Thread_{0}".format(str(i)))
        t.start()
    print("finished")
