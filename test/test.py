import threading
from threading import current_thread
import random
import time
#经典小蚂蚁吃蛋糕
cake = random.randint(10,30)
print('蛋糕还剩%d' %cake)
lock = threading.Lock()
class Red_ant(threading.Thread):
    def run(self):
        global cake
        while cake != 0:
            eat = random.randint(1,5)
            if eat > cake:
                print('红蚂蚁胃口太大，没吃到，蛋糕还剩%d' %cake)
                time.sleep(3)
                print('红蚂蚁睡了3秒')
            else:
                with threading.Lock():
                    cake -= eat
                print('红蚂蚁吃了%d，蛋糕还剩%d' %(eat,cake))
                time.sleep(3)
                print('红蚂蚁睡了3秒')
class Black_ant(threading.Thread):
    def run(self):
        global cake
        while cake != 0:
            eat = random.randint(1,5)
            if eat > cake:
                print('黑蚂蚁胃口太大，没吃到，蛋糕还剩%d' % cake)
                time.sleep(3)
                print('黑蚂蚁睡了3秒')
            else:
                lock.acquire()
                cake -= eat
                lock.release()
                print('黑蚂蚁吃了%d,蛋糕还剩%d' %(eat,cake))
                time.sleep(5)
                print('黑蚂蚁睡了3秒')
r1 = Red_ant()
r2 = Black_ant()
r3 = Red_ant()
r1.start()
r2.start()

r1.join()
r2.join()

print('蛋糕还剩%d' %cake)