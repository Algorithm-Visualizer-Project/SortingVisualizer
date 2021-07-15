from tkinter import * 
from tkinter import ttk
from heapsort import heap_sort
from selectionsort import selection_sort
from quicksort import quick_sort
from bubblesort import bubble_sort
from mergesort import merge_sort
import random

array = []

window = Tk()
window.title("Sorting Visualizer")

def checkSpeed():
    if Speed_select.get() == 'Slow':
        speed=0.5
    
    elif Speed_select.get() == 'Medium':
        speed=0.2

    elif Speed_select.get() == 'Fast':
        speed=0.05

    else : speed=0.5
    return speed

def Bubble():
    bubble_sort(array, display, checkSpeed())

def Selection():
    selection_sort(array, display, checkSpeed())

def Quick():
    quick_sort(array, 0, len(array)-1, display, checkSpeed())

def Heap():
    heap_sort(array, display, checkSpeed())

def Merge():
    merge_sort(array, 0, len(array)-1, display, checkSpeed())


def display(array, colours):
    canvas.delete("all")
    hor_width = 1000 / (len(array) + 1)
    offset = hor_width//2
    spacing = hor_width//4
    for i, height in enumerate(array):
        #top left corner of rectangle
        x0 = i * hor_width + offset + spacing
        y0 = 500 - height * 450/1000
        #bottom right corner of rectangle
        x1 = (i + 1) * hor_width + offset
        y1 = 500

        canvas.create_rectangle(x0, y0, x1, y1, fill=colours[i])
        if(len(array)<=20): x_align=(x0+x0+x1)/3
        else : x_align=x0
        canvas.create_text(x_align, y0, anchor=SW, text=str(array[i]))
    
    window.update_idletasks()


def Create_Random_Array():
    global array
    size = int(Array_size.get())

    array = []
    colours=[]
    for _ in range(size):
        array.append(random.randrange(100, 1000))
        colours.append('red')
    display(array, colours)



canvas = Canvas(master=window, width=1000, height=500, bg='#f5f2c5')
canvas.pack()

Navigation_frame = Frame(master=window, width= 1000, height=200, bg='#6200ee')
Navigation_frame.pack(fill=X)

Button(master=Navigation_frame, text="Bubble Sort", command=Bubble, bg='coral', relief=RAISED, borderwidth=5,width=20).grid(row=0, column=0, padx=20, pady=5)
Button(master=Navigation_frame, text="Selection Sort", command=Selection, bg='coral', relief=RAISED, borderwidth=5,width=20).grid(row=0, column=1, padx=20, pady=5)
Button(master=Navigation_frame, text="Quick Sort", command=Quick, bg='coral', relief=RAISED, borderwidth=5,width=20).grid(row=0, column=2, padx=20, pady=5)
Button(master=Navigation_frame, text="Heap Sort", command=Heap, bg='coral', relief=RAISED, borderwidth=5,width=20).grid(row=0, column=3, padx=20, pady=5)
Button(master=Navigation_frame, text="Merge Sort", command=Merge, bg='coral', relief=RAISED, borderwidth=5,width=20).grid(row=0, column=4, padx=20, pady=5)

Label(master=Navigation_frame, text="Select Speed: ", bg='cyan',width=20, relief=RAISED, borderwidth=5).grid(row=1, column=0, padx=40, pady=5, sticky=W)
Speed_select = ttk.Combobox(master=Navigation_frame, values=['Slow', 'Medium', 'Fast'])
Speed_select.current(1)
Speed_select.grid(row=1, column=1, padx=5, pady=5)

Array_size = Scale(master=Navigation_frame, from_=3, to=30, resolution=1, orient=HORIZONTAL, label="Array Size",length=150)
Array_size.set(10)
Array_size.grid(row=1, column=2, padx=5, pady=5)

Button(master=Navigation_frame, text="Generate New Array", command=Create_Random_Array, bg='cyan', relief=RAISED, borderwidth=5,width=20).grid(row=1, column=3, padx=5, pady=5)

temp_size=10
temp_color=[]
for _ in range(temp_size):
        array.append(random.randrange(100, 1000))
        temp_color.append('red')
display(array, temp_color)

window.mainloop()
