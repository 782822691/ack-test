import threading
from threading import current_thread
import time
import random
import queue
q = queue.Queue(5)
class provider(threading.Thread):
    def run(self):
        global q
        while True:
            tmp = random.randint(1,100)
            q.put(tmp)
            print('生产者%s生产了%d个数据' %(current_thread().name,tmp))
            t = random.randint(1,5)
            time.sleep(t)
            print('生产者休息了%d秒' %t)
class customer(threading.Thread):
    def run(self):
        global q
        while True:
            tmp = q.get()
            print('消费者%s消费了%d数据' %(current_thread().name,tmp))
            # q.task_done()
            t = random.randint(1,5)
            time.sleep(t)
            print('消费者休息了%d秒' %t)
            q.task_done()
c1 = customer()
c2 = customer()
p1 = provider()
p2 = provider()
c1.start()
c2.start()
p1.start()

