import time
import threading


def do_thread(num):
    global public_num
    #枷锁
    lock.acquire()
    public_num -= 1
    # #解锁
    lock.release()
    time.sleep(1)
    print("公共数字在线程{0}中是{1}".format(num, public_num))


public_num = 100
threads_list = []
lock = threading.Lock()
for i in range(50):
    t = threading.Thread(target=do_thread, args=(i,))
    t.setName("线程{}".format(i))
    t.start()
    threads_list.append(t)
# 等待所有子线程结束
for t in threads_list:
    t.join()

print("最终公共数字为{}".format(public_num))
