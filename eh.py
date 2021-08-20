# import logging
#
# """
# error
# warning
# critical
# info
# debug
# """
#
#
# logging.basicConfig(
#     filename="./logs/errors.log",
#     filemode="a",
#     format="%(levelname)s - [%(asctime)s] - %(name)s : %(message)s"
# )
#
# logging.error("this is test error.")
# logging.warning("this is my test warning")
# logging.critical("This is my test critical")
# logging.info("This is my test info")
# logging.debug("This is my test debug")

from common.logger import log, ERROR, WARNING
import magicmethoad

a = 5
b = 2
c = 0
d= None
# n =10
try:
    d = n
    c = a / b
    d = c
except TypeError as te:
    log(f"Error: Tha values(a={a}, b={b}) are not same data types")
    # logging.error(f"Error: Tha values(a={a}, b={b}) are not same data types")
    # print(f"Error: Tha values(a={a}, b={b}) are not same data types")
except ZeroDivisionError as ze:
    log(
        level=ERROR,
        message="Error: Tha values(a=%d, b=%d) are containing `0` in it." % (a, b)
    )
    #logging.error("Error: Tha values(a=%d, b=%d) are containing `0` in it." % (a, b))
    # print("Error: Tha values(a=%d, b=%d) are containing `0` in it." % (a, b))
except Exception as e:
    log(
        level=ERROR,
        message=e,
        traceback=True
    )
    # logging.error(e, exc_info=True)
    # print("Error: ", e)
finally:
    if not d:
        d = "from finally"


print("Final value: ", c)
print("d value: ", d)

