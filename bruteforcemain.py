import threading
import queue
from pwdproducer import PasswordProducer
from pwdconsumer import PasswordConsumer

queue = queue.Queue(maxsize=10)
condition = threading.Condition()

producer = PasswordProducer(queue, condition)

consumer = PasswordConsumer(queue, condition)

producer.start()
consumer.start()

producer.join()
consumer.join()
