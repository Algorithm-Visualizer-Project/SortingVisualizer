import time

def binary_search(array, to_find, display, speed):
    l = 0
    r = len(array)-1
    code_binarysearch(array,to_find, display, speed, l, r)

def code_binarysearch(array, to_find, display, speed, l, r):    
    if(l > r):
        display(array, ["black" for x in range(len(array))])
        time.sleep(speed)
        return
    mid = (l + r)//2
    if(array[mid] == to_find):
        display(array,['green' if x==mid else "#FFDCD1" for x in range(len(array))])
        time.sleep(speed)
        return
    elif(array[mid] < to_find):
        new_l = mid + 1
        display(array, ['yellow' if x == l else "orange" if x == r else  "#FFDCD1" for x in range(len(array))])
        time.sleep(speed)
        code_binarysearch(array, to_find, display, speed, new_l, r)
    else:
        new_r = mid - 1
        display(array, ['yellow' if x == l else "orange" if x == r else  "#FFDCD1" for x in range(len(array))])
        time.sleep(speed)
        code_binarysearch(array, to_find, display, speed, l, new_r)