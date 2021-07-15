import time

def merge_sort(array, left, right, display, speed):
    if left < right:
        middle = (left + right) // 2
        merge_sort(array, left, middle, display, speed)
        merge_sort(array, middle+1, right, display, speed)
        merge(array, left, middle, right, display, speed)
        if left == 0 and right == len(array) - 1:
            display(array, ['green' for x in range(len(array))])

def merge(array, left, middle, right, display, speed):
    display(array, Colorize(len(array), left, middle, right))
    time.sleep(speed)

    leftPart = array[left:middle+1]
    rightPart = array[middle+1: right+1]

    leftIdx = rightIdx = 0

    for arrayIdx in range(left, right+1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                array[arrayIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                array[arrayIdx] = rightPart[rightIdx]
                rightIdx += 1
        
        elif leftIdx < len(leftPart):
            array[arrayIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            array[arrayIdx] = rightPart[rightIdx]
            rightIdx += 1
    
    display(array, ["green" if x >= left and x <= right else "white" for x in range(len(array))])
    time.sleep(speed)

def Colorize(size, left, middle, right):
    colours = []

    for i in range(size):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colours.append("yellow")
            else:
                colours.append("pink")
        else:
            colours.append("white")

    return colours