import threading
import time
class mythread(threading.Thread):
    def __init__(self,threadID,name,count):
        #表示定义 加self
        #threading.Thread.__init__(self)
        #表示调用 不加self
        super().__init__()
        self.threadID = threadID
        self.name = name
        self.count = count
    def run(self):
        print('开始线程'+self.name)
        print_name(self.name,self.count,1)
        print('结束线程'+self.name)

def print_name(threadName,count,delay):
    while count:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        count -= 1

if __name__ == "__main__":
    thread1 = mythread(1,'thread-1',6)
    thread2 = mythread(2,'thread-2',5)
    #主线程退出 kill thread1
    #thread1.setDaemon(True)
    thread1.start()
    thread2.start()
    #thread1.join()
    thread2.join()
    print('主线程')