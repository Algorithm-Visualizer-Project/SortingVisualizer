import time

def to_heap(array, chosen_root, n, display, speed):
    time.sleep(speed)
    index = chosen_root
    l = 2 * chosen_root + 1
    r = 2 * chosen_root + 2
    
    if l < n and array[index] < array[l]:
        index = l
    if r < n and array[index] < array[r]:
        index = r
    if index != chosen_root:
        display(array, ['blue' if x == chosen_root or x == index else 'green' if x >= n else 'red' for x in range(len(array))])
        array[index], array[chosen_root] = array[chosen_root], array[index]
        to_heap(array, index, n, display, speed)


def heap_sort(array, display, speed):
    for index in range(len(array)//2-1, -1, -1):
        to_heap(array, index, len(array), display, speed)
    for i in range(len(array)-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        to_heap(array, 0, i, display, speed)
        display(array, ['green' if x >= i else 'red' for x in range(len(array))])
        time.sleep(speed)
    display(array, ['green' for x in range(len(array))])