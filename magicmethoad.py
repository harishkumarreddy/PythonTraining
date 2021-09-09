# print("Hello there")


def main(msg):
    """
    This is a main invocatier for direct cli executions.
    :param msg:(string): message as string.
    :return: void
    """
    print(msg)
    print(msg.__len__()) # -> len(msg)
    print(msg.__hash__())
    print(msg.__eq__("hey"))
    print(msg.__contains__("ll"))

# main()
if __name__ == "__main__":
    # print("hello")
    main("hello")
    abs(-1)
    print(main.__doc__)
    print(abs.__doc__)
    print(print.__doc__)



