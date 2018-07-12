import time
from threading import Thread


def do_thread(num):
    print("子线程 %s" % str(num))
    time.sleep(3)


for i in range(5):
    t = Thread(target=do_thread, args=(i,))
    t.start()
    t.join()
    t.setName("执行完子线程{0}，才执行这里".format(str(i)))
    print(t.getName())
# 当执行join()后主线程就停了，直到子线程完成后才开始接着主线程执行，整个程序是线性的
# setDaemon() 为前台线程时，所有的线程都在同时运行，主线程也在运行。
# 只不过是主线程运行完以后等待所有子线程结束。这个还是一个并行的执行，执行效率肯定要高于join()方法的。
