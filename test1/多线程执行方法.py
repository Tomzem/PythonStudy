import time
from threading import Thread


def do_thread(num):
    print("this is thread %s" % str(num))
    time.sleep(3)


for i in range(5):
    t = Thread(target=do_thread, args=(i,))
    t.start()
    t.setName("{0}".format(str(i)))
    print(t.getName())

