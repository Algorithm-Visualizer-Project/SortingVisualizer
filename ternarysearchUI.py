from tkinter import * 
from tkinter import ttk

from ternarysearch import ternary_search
import random

array = []
window = Tk()
window.title("Ternary Search Visulaizer")

def checkSpeed():
    if Speed_select.get() == 'Slow':
        speed=2.5
    
    elif Speed_select.get() == 'Medium':
        speed=1.5

    elif Speed_select.get() == 'Fast':
        speed=1

    else : speed=0.5
    return speed

def Start():
    strd=entry_select.get()
    if(len(strd) and strd.isnumeric()):
        ternary_search(0,len(array)-1,int(strd),array,display,checkSpeed())

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
        colours.append('indianred1')
    array.sort()
    display(array, colours)


canvas = Canvas(master=window, width=1000, height=500, bg='#f5f2c5')
canvas.pack()

Navigation_frame = Frame(master=window, width= 1000, height=200, bg='#6200ee')
Navigation_frame.pack(fill=X)

Label(master=Navigation_frame, text="Enter the value to search (integer only): ", bg='cyan',width=35, relief=RAISED, borderwidth=5).grid(row=0, column=0, padx=40, pady=5, sticky=W)
entry_select = ttk.Entry(master=Navigation_frame,width=23)
entry_select.grid(row=0, column=1, padx=5, pady=5)

Button(master=Navigation_frame, text="Start", command=Start, bg='coral', relief=RAISED, borderwidth=5,width=20).grid(row=0, column=4, padx=40, pady=5)

Label(master=Navigation_frame, text="Select Speed: ", bg='cyan',width=35, relief=RAISED, borderwidth=5).grid(row=1, column=0, padx=40, pady=5, sticky=W)
Speed_select = ttk.Combobox(master=Navigation_frame, values=['Slow', 'Medium', 'Fast'])
Speed_select.current(1)
Speed_select.grid(row=1, column=1, padx=5, pady=5)

Array_size = Scale(master=Navigation_frame, from_=3, to=50, resolution=1, orient=HORIZONTAL, label="Array Size",length=150)
Array_size.set(10)
Array_size.grid(row=0, column=3, padx=20, pady=5)

Button(master=Navigation_frame, text="Generate New Sorted Array", command=Create_Random_Array, bg='cyan', relief=RAISED, borderwidth=5,width=20).grid(row=1, column=4, padx=5, pady=5)

temp_size=10
temp_color=[]
for _ in range(temp_size):
        array.append(random.randrange(100, 1000))
        temp_color.append('indianred1')
array.sort()
display(array, temp_color)

window.mainloop()