import random

dct = {}
while True:
    for i in range(0, 10000):
        broken_number = random.uniform(0, 1)
        dct[broken_number] = hash(broken_number)

    tempset = set(dct.values())
    if len(tempset) < len(dct.values()):
        break
    dct = {}

lst = list(dct.keys())


def findhashedcouple():
    """
    Function that finds hashed couples.

    """
    for hashed in dct:
        count = 0
        for n in range(0, 10000):
            if dct[hashed] == dct[lst[n]]:
                count += 1
            if count > 1 and hashed != lst[n]:
                print("hash(", (repr(hashed)), ") == hash(", lst[n], ") == ", dct[hashed])
                break
    print("Finished")


findhashedcouple()
