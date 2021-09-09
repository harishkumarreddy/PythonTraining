import concurrent.futures
import time
# import threading
from concurrent.futures import ThreadPoolExecutor

def printTimesMsg(msg="Hello", times=10, iv=1):
    print("hello")
    if times is not int:
        times =int(times)

    for i in range(times):
        # print(f"{msg}: {i}")
        time.sleep(iv)

    return "i am done"

# printTimesMsg()
# printTimesMsg(msg="hey", iv=2)

# t1 = threading.Thread(target=printTimesMsg)
# t2 = threading.Thread(target=printTimesMsg, args=["hey", 10, 2])
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

with ThreadPoolExecutor(max_workers=4) as ex:
    res = [ex.submit(printTimesMsg, props) for props in [["hey", 10, 2], ["hey",5, 1], ["hey", 10, 2], ["hey",5, 1], ["hey", 10, 2], ["hey",5, 1]]]
    for trd in concurrent.futures.as_completed(res):
        print(trd.result())



print("Finished")
