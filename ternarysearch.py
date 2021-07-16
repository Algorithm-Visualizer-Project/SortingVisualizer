import time

def ternary_search(l, r, to_find, array, display, speed):
    if (r >= l):
        mid1 = l + (r - l) //3
        mid2 = r - (r - l) //3
        display(array, ["orange" if x == mid1 or x == mid2 else "yellow" if x == l or x == r else "#FFDCD1" for x in range(len(array))])
        time.sleep(speed)
        if (array[mid1] == to_find):
            display(array,['green' if x==mid1 else "#FFDCD1" for x in range(len(array))])
            time.sleep(speed)
            return
        if (array[mid2] == to_find):
            display(array,['green' if x==mid2 else "#FFDCD1" for x in range(len(array))])
            time.sleep(speed)
            return
        if (to_find < array[mid1]):
            ternary_search(l, mid1 - 1, to_find, array, display, speed)
        elif (to_find > array[mid2]):
            ternary_search(mid2 + 1, r, to_find, array, display, speed)
        else:
            ternary_search(mid1 + 1, mid2 - 1, to_find, array, display, speed)
    else:
        display(array, ["black" for x in range(len(array))])
        time.sleep(speed)
        return        
    