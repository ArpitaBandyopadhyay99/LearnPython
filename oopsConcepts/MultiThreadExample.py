from threading import Thread
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(3):
            print("hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(3):
            print("hi")
            sleep(0.5)


t1 = Hello()
sleep(1)
t2 = Hi()

t1.start()
t2.start()

t1.join()
t2.join()

print("Bye by main thread")

