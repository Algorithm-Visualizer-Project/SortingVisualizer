import time
sorted=[]
def partition(array, head, tail, display, speed):
    border = head
    pivot = array[tail]

    display(array, colorize(len(array), head, tail, border, border))
    time.sleep(speed)

    for j in range(head, tail):
        if array[j] < pivot:
            display(array, colorize(len(array), head, tail, border, j))
            time.sleep(speed)

            array[border], array[j] = array[j], array[border]
            border += 1

        display(array, colorize(len(array), head, tail, border, j))
        time.sleep(speed)


    #swap pivot with border value
    array[border], array[tail] = array[tail], array[border]
    display(array, colorize(len(array), head, tail, border, tail))
    time.sleep(speed)
    sorted.append(border)

    
    return border

def quick_sort(array, head, tail, display, speed):
    if(head==0 and tail==len(array)-1):
        sorted.clear()
    if head<=tail:
        partitionIdx = partition(array, head, tail, display, speed)

        #LEFT PARTITION
        quick_sort(array, head, partitionIdx-1, display, speed)

        #RIGHT PARTITION
        quick_sort(array, partitionIdx+1, tail, display, speed)
    if head == 0 and tail == len(array) - 1:
        display(array, ['green' for x in range(len(array))])


def colorize(length, head, tail, border, currIdx):
    colours = []
    for i in range(length):
        #base coloring
        if i >= head and i <= tail:
            colours.append('gray')
        else:
            colours.append('indianred1')

        if i == tail:
            colours[i] = 'blue'
        elif i == border:
            colours[i] = 'blue'
        elif i == currIdx:
            colours[i] = 'yellow'
        if(i in sorted):
            colours[i]='green'

    return colours