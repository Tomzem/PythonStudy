import threading
import time


def do_thread(num):
    print("第{}个线程{}开始".format(num+1, time.ctime()))
    time.sleep(1)
    print("第{}个线程{}结束".format(num + 1, time.ctime()))


if __name__ == '__main__':
    start_time = time.time()
    thread_list = []
    for i in range(10):
        t = threading.Thread(target=do_thread, args=(i,))
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()
    end_time = time.time()
    print("总共时长{}".format(end_time - start_time))