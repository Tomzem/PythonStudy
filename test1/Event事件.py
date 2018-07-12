import threading


def do(event):
    print("start")
    # 阻塞
    event.wait()
    print("execute")


if __name__ == '__main__':
    event_obj = threading.Event()
    for i in range(5):
        t = threading.Thread(target=do, args=(event_obj,))
        t.start()

    while not event_obj.is_set():
        if input("") == 't':
            event_obj.set()
        else:
            event_obj.clear()

