import time
from threading import Thread


def do_thread(num):
    print("this is thread %s" % str(num))
    time.sleep(3)
    print("OK {}".format(num))


for i in range(2):
    t = Thread(target=do_thread, args=(i,))
    # 不设置 就是前台进程 主线程等子线程执行完才可以结束
    # 设置为TRUE 则为后天进程  主线程直接结束
    # t.setDaemon(True)
    t.start()
    t.setName("{0}".format(str(i)))
    print(t.getName())
