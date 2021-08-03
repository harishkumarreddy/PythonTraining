import time

myList = ["Ricky","alex","David","gary"] #[3,5,4,2,1]

"""
Steps:
1. Pick each item from the list
2. compare the item with all items till the same position
3. if item is same or greater than compared position item, 
    swap the item with the compared position item.
4. repeat the same competition till position of the main item.
"""
s = time.perf_counter()
print(myList)
for i in range(len(myList)):
    for j in range(i):
        if myList[i] < myList[j]:
            # tmp = myList[i]
            # myList[i] = myList[j]
            # myList[j] = tmp
            myList[i], myList[j] = myList[j], myList[i]

e = time.perf_counter()
print(myList)
print(f"total time:{e-s:0.00f}")
