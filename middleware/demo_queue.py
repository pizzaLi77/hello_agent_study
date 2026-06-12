import threading
import time


class DemoQueue:
    def __init__(self):
        self._timer = None
        self._items = []
        #加锁 防并发对队列进行操作
        self._lock = threading.Lock()

    def add(self, item):
        # with等同于try-finally，with块执行完会自动释放锁
        with self._lock:
            self._items.append(item)
            self._schedule_timer(3)
            print(f'获取到锁add方法执行，入参为：{item}')

    def _schedule_timer(self, delay_seconds):
        if self._timer is not None:
            #先取消上一个定时器，可实现短时间内多次触发并只保留最后一次
            self._timer.cancel()
            print('执行cancel逻辑')
        #创建一个定时器，delay_seconds秒后调用self._process_queue方法
        self._timer = threading.Timer(
            delay_seconds,
            self._process_queue,
        )
        #表示主程序退出时不会为了等定时器线程卡住
        self._timer.daemon = True
        #真正启动定时器并创建后台线程并开始倒计时
        self._timer.start()
        print(f'开启定时器。。。')
    def _process_queue(self):
        with self._lock:
            print('获取到锁进入到_process_queue逻辑。。。')
            print(self._items)
            self._items.clear()
            self._timer = None

queue = DemoQueue()
queue.add('A')
time.sleep(1)

queue.add('B')
time.sleep(2)

queue.add('C')
time.sleep(5)