import concurrent
import time
# import multiprocessing
from concurrent.futures import ProcessPoolExecutor

def printTimesMsg(msg="Hello", times=10, iv=1):
    if times is not int:
        times = int(times)

    for i in range(times):
        print(f"{msg}: {i}")
        time.sleep(iv)


# printTimesMsg()
# printTimesMsg(msg="hey", iv=2)

# t1 = multiprocessing.Process(target=printTimesMsg) #multiprocessing.process(target=printTimesMsg)
# t2 = multiprocessing.Process(target=printTimesMsg, args=["hey", 10, 2])
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()


with ProcessPoolExecutor(max_workers=4) as ex:
    res = [ex.submit(printTimesMsg, props) for props in [["hey", 10, 2], ["hey",5, 1]]]
    for trd in concurrent.futures.as_completed(res):
        print(trd.result())
print("Finished")
