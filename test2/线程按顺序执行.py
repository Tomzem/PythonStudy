import threading
import time


def do_thread(num):
    print("第{}个线程{}开始".format(num+1, time.ctime()))
    time.sleep(1)


if __name__ == '__main__':
    start_time = time.time()
    for i in range(10):
        t = threading.Thread(target=do_thread, args=(i,))
        t.start()
        t.join()
        print("第{}个线程{}结束".format(i + 1, time.ctime()))
    end_time = time.time()
    print("总共时长{}".format(end_time - start_time))
