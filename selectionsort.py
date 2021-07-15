import time

def selection_sort(array, display, speed):
    for iter in range(len(array)):
        min_index = iter
        for i in range(iter, len(array)):
            if array[i] < array[min_index]:
                min_index = i
                display(array, ['yellow' if x == min_index else "green" if x <= iter else  "red" for x in range(len(array))])
                time.sleep(speed)
        display(array, ['blue' if x == min_index or x == iter else "green" if x <= iter else "red" for x in range(len(array))])
        time.sleep(speed)
        array[min_index], array[iter] = array[iter], array[min_index]
    display(array, ['green' for x in range(len(array))])