import logging
import threading
from typing import Any

from fastapi_study.memory_updater import MemoryUpdater
logger = logging.getLogger(__name__)

class MemoryUpdateQueue:

    def __init__(self):
        self._queue = []
        self._lock = threading.Lock()
        self._timer: threading.Timer | None = None
        self._processing = False


    def add(
            self,
            messages: list[Any],
    ):
        with self._lock:
            self._queue.append(messages)
            # for msg in messages:
            #     self._queue.append(msg)
            self.reset_timer(10)

    def reset_timer(self, interval_time):
        if self._timer is not None:
            self._timer.cancel()
        self._timer = threading.Timer(
            interval_time,
            self.process_queue,
        )
        self._timer.daemon = True
        self._timer.start()

    def process_queue(self):
        logger.info('定时器触发执行。。。')
        with self._lock:
            print(f'当前队列信息为：{self._queue}')
            #_processing存在作用是同一时刻只会有一个线程进来更新记忆
            if self._processing:
                #若同时多个线程进来只会有一个线程成功去获取队列消息，其余线程进行重试类型cas的重试机制
                #之所以没有将锁粒度扩散到整段逻辑是因为后续整合记忆调用llm较耗时，所以采取策略是减小锁粒度
                #同时通过_processing配合保证同一时间只有一个线程能成功获取队列消息
                self.reset_timer(0)
                return
            if not self._queue:
                #这块保证了避免空的队列重复去持久化记忆，比如线程1 线程2 一块要持久化记忆，但是线程1先拿到锁了
                #然后获取队列信息并清空队列释放锁调用llm去持久化记忆
                #在线程1调用llm持久化记忆期间因为self.reset_timer(0) 线程2又进来了发现队列已经为空那就没必要再去重复持久化记忆了，直接返回
                return
            self._processing = True
            context_process =self._queue.copy()
            self._queue.clear()
            self._timer = None
        try:
            updater = MemoryUpdater()
            for msg in context_process:
                success = updater.updateMemory(msg)
                if success:
                    logger.info('记忆持久化成功。。。')
                else:
                    logger.warning('记忆持久化失败。。。')
        except Exception as e:
            logger.error(f'记忆持久化失败，失败原因：{e}')

        finally:
            with self._lock:
                self._processing = False