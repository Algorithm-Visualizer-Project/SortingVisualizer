import time

def bubble_sort(array, display, speed):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                time.sleep(speed)
            display(array, ['green' if x >= len(array) - i else 'blue' if x == j or x == j+1 else 'red' for x in range(len(array))] )
    display(array, ['green' for x in range(len(array))])