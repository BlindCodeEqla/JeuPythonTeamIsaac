
import winsound
import threading



def process1():
    winsound.PlaySound("CLOCK", winsound.SND_FILENAME)
def process2():
    input("hello: ")
    th1.__delattr__()


th1 = threading.Thread(target=process1)
th2 = threading.Thread(target=process2)

th1.start()
th2.start()

# th2.join()
# th1.join()
print("hello")