# TODO : learn tkinter and make a GUI
# TODO : brush up the program
# TODO : remove the blinking screen(maybe by using a horizontal array of line)(horizontal line covering the previous ones
# TODO : add notes so that you do not forget how your own program works
# TODO : Do not forget to delete the TODOs after completing them
import math
import random
import time
import pygame as pg
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Tk

skip_value = 0
length = 0
breadth = 0
screen = None
colour = True
running = False
brebutton = None
lenbutton = None
recommended_button = None
bredone = None
lendone = None
root = None
ldone = False
bdone = False
size = 0
x = -1
xincrement = -1
y2 = -1
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 128, 0)
PURPLE = (85, 26, 139)
elements = []
indx = -1
iter = -1
change_screen = None
y = -1
wait_time = -1


def Super_SelectionSort(inp, i):
    input = []
    for j in inp:
        input.append(j)
    min = input[i]
    max = input[i]
    pos = i
    posm = i
    uv = len(input) - 1 - i
    for j in range(i + 1, uv + 1):
        if min > input[j]:
            min = input[j]
            pos = j
        if max < input[j]:
            max = input[j]
            posm = j
    input[i], input[pos] = input[pos], input[i]
    if i == posm:
        input[uv], input[pos] = input[pos], input[uv]
        posm = pos
    elif uv != len(input) / 2:
        input[uv], input[posm] = input[posm], input[uv]
    return input, i, pos, uv, posm


def Bubble_Sort(input, i, j):
    if j >= len(input) - i - 1:
        i += 1
        j = 0
    if input[j + 1] < input[j]:
        input[j], input[j + 1] = input[j + 1], input[j]
    return input, j, j + 1, i


def Selection_Sort(input, i):
    unsorted = []
    for k in input:
        unsorted.append(k)
    length = len(unsorted)
    min = i
    for j in range(i + 1, length):
        if unsorted[j] <= unsorted[min]:
            min = j
    unsorted[i], unsorted[min] = unsorted[min], unsorted[i]

    return unsorted, min, i


def generate_list(list, size, breadth):
    for i in range(1, size):
        list.append(random.randint(0, breadth))
        # list.append(breadth - int(breadth / size * i))
    return list
    # for i in range(1000, 0, -1):
    #     list.append(i)
    # return list


def initialize():
    global screen, running, x, xincrement, y2, COLOUR, elements, indx, iter, change_screen, y, limit, Sort, BLACK, RED, BLUE, skip_value, wait_time, colour, lenbutton, bredone, brebutton, lendone, ldone, root, length, breadth, size, bdone, recommended_button
    skip_init = False
    wait_time = 0
    pg.init()
    if not skip_init:
        def next_window():
            if bdone and ldone:
                root.destroy()
                sort()
            else:
                messagebox.showinfo("ERROR!!!", "You have not entered the two values pls press the respective buttons",
                                    default='ok')

        def lengthdone():
            global x, root, brebutton, bredone, lenbutton, lendone, ldone, length, breadth, recommended_button

            length = x
            if length > 0:
                lendone.destroy()
                lenbutton.destroy()
                bredone.destroy()
                brebutton.destroy()
                recommended_button.destroy()

                lenbutton = Button(root, text="length of window : {}".format(x), bg='royal blue')
                lenbutton.place(relx='0.05', rely='0.1')

                lendone = Button(root, text="now enter the breadth")
                lendone.place(relx='0.05', rely='0.4')

                x = 100
                brebutton = Button(root, text="breadth of window : {}".format(x), fg='red', bg='royal blue')
                brebutton.place(relx='0.52', rely='0.1')

                bredone = Button(root, text="breadth entered", command=breadthdone, bg='light blue')
                bredone.place(relx='0.595', rely='0.4')

                ldone = True
            else:
                messagebox.showinfo("ERROR", "The length cannot be negative")

        def breadthdone():
            global breadth, root, brebutton, bredone, bdone
            breadth = x
            if breadth > 0:
                bredone.destroy()
                brebutton.destroy()
                bdone = True
                brebutton = Button(root, text="breadth of window : {}".format(x), fg='black', bg='royal blue')
                brebutton.place(relx='0.5', rely='0.1')

                bredone = Button(root, text="press next when ready")
                bredone.place(relx='0.5', rely='0.4')
            else:
                messagebox.showinfo("ERROR", "Breadth cannot be negative")

        def increase(event):
            global x, root, lenbutton, ldone, brebutton
            x += 1
            if not ldone:
                lenbutton.destroy()
                lenbutton = Button(root, text="length of window : {}".format(x), fg='red', bg='royal blue')
                lenbutton.place(relx='0.05', rely='0.1')
            else:
                brebutton.destroy()
                brebutton = Button(root, text="breadth of window : {}".format(x), fg='red', bg='royal blue')
                brebutton.place(relx='0.52', rely='0.1')

        def decrease(event):
            global x, root, lenbutton, ldone, brebutton
            x -= 1
            if not ldone:
                lenbutton.destroy()
                lenbutton = Button(root, text="length of window : {}".format(x), fg='red', bg='royal blue')
                lenbutton.place(relx='0.05', rely='0.1')
            else:
                brebutton.destroy()
                brebutton = Button(root, text="breadth of window : {}".format(x), fg='red', bg='royal blue')
                brebutton.place(relx='0.52', rely='0.1')

        def increase_100(event):
            global x, root, lenbutton, ldone, brebutton
            x += 100
            if not ldone:
                lenbutton.destroy()
                lenbutton = Button(root, text="length of window : {}".format(x), fg='red', bg='royal blue')
                lenbutton.place(relx='0.05', rely='0.1')
            else:
                brebutton.destroy()
                brebutton = Button(root, text="breadth of window : {}".format(x), fg='red', bg='royal blue')
                brebutton.place(relx='0.52', rely='0.1')

        def decrease_100(event):
            global x, root, lenbutton, ldone, brebutton
            x -= 100
            if not ldone:
                lenbutton.destroy()
                lenbutton = Button(root, text="length of window : {}".format(x), fg='red', bg='royal blue')
                lenbutton.place(relx='0.05', rely='0.1')
            else:
                brebutton.destroy()
                brebutton = Button(root, text="breadth of window : {}".format(x), fg='red', bg='royal blue')
                brebutton.place(relx='0.52', rely='0.1')

        def recommended():
            global x, root, brebutton, bredone, lenbutton, lendone, ldone, length, breadth, bdone
            length = 1000
            breadth = 500
            lendone.destroy()
            lenbutton.destroy()
            bredone.destroy()
            brebutton.destroy()

            lenbutton = Button(root, text="length of window : {}".format(x), bg='royal blue')
            lenbutton.place(relx='0.05', rely='0.1')
            brebutton = Button(root, text="breadth of window : {}".format(x), fg='red', bg='royal blue')
            brebutton.place(relx='0.52', rely='0.1')

            bredone = Button(root, text="breadth entered", command=breadthdone, bg='light blue')
            bredone.place(relx='0.595', rely='0.4')

            ldone = True
            bredone.destroy()
            brebutton.destroy()
            bdone = True
            brebutton = Button(root, text="breadth of window : {}".format(x), fg='black', bg='royal blue')
            brebutton.place(relx='0.5', rely='0.1')

        root = Tk()
        root.configure(bg='purple')
        root.geometry("300x100")
        root.title('Set Screen Size(recommended:1000x500)')
        x = 100

        lenbutton = Button(root, text="length of window : {}".format(x), fg='red', bg='royal blue')
        lenbutton.place(relx='0.05', rely='0.1')

        lendone = Button(root, text="length entered", command=lengthdone, bg='light blue')
        lendone.place(relx='0.09', rely='0.4')

        brebutton = Button(root, text="breadth of window : {}".format(x), fg='black', bg='royal blue')
        brebutton.place(relx='0.5', rely='0.1')

        bredone = Button(root, text="breadth entered", command=breadthdone)
        bredone.place(relx='0.595', rely='0.4')

        recommended_button = Button(root, text="1000x500", command=recommended)
        recommended_button.place(relx='0.392', rely='0.4')

        done_button = Button(root, text="Next -->", command=next_window, bg='green2', fg='dark green')
        done_button.place(relx='0.4', rely='0.75')

        root.bind("<Up>", increase)
        root.bind("<Down>", decrease)
        root.bind("<Shift-Up>", increase_100)
        root.bind("<Shift-Down>", decrease_100)

        # cmb = Combobox

        def checkcmbo():
            global Sort, cmb, root, sel

            if cmb.get() == "Bubble Sort":
                sel = messagebox.askyesno("Is This Your Choice ? ", "did you choose to see Bubble Sort", default='yes')
                Sort = "Bubble Sort"

            elif cmb.get() == "Selection Sort":
                sel = messagebox.askyesno("Is This Your Choice ? ", "Did you choose to see Selection Sort",
                                          default='yes')
                Sort = "Selection Sort"

            elif cmb.get() == "Super Selection Sort":
                sel = messagebox.askyesno("Is This Your Choice ? ", "Did you choose to see Super Selection Sort",
                                          default='yes')
                Sort = "Super Selection Sort"

            elif cmb.get() == "":
                sel = messagebox.showinfo("No choice detected", "You have to choose something!!!!", default='ok')
            if sel == True and cmb.get() != "":
                root.destroy()
                size_func()

        def sort():
            global cmb, root
            root = Tk()

            root.geometry("400x50")
            # ^ width - height window :D

            root.title("Choose The Sorting Technique")

            root.configure(bg='red')

            cmb = ttk.Combobox(root, width="20", values=("Bubble Sort", "Selection Sort", "Super Selection Sort"))
            cmb.place(relx="0.1", rely="0.2")
            cmb.set("Super Selection Sort")

            btn = ttk.Button(root, text="Confirm Selection", command=checkcmbo)
            btn.place(relx="0.5", rely="0.15")

        def size_func():
            def get_val(event=None):
                global size, length
                try:
                    size = int(size_entry.get())
                except Exception:
                    size = 0
                    messagebox.showinfo("ERROR!!!", "Pls enter a number")
                    size_entry.delete(0, END)
                    size_entry.insert(0, "")
                else:
                    if int(size) > length:
                        size = 0
                        messagebox.showinfo("ERROR!!!",
                                            "Pls enter a number that is less than or equal to the length({})".format(
                                                length))
                        size_entry.delete(0, END)
                        size_entry.insert(0, "")
                    else:
                        root.destroy()
                        direction()

            root = Tk()
            root.title("Number of elements for sorting")
            root.geometry('500x100')
            Label(root, text='Enter the size of the array(the bigger it is, slower the program is) : ').grid(row=0)
            size_button = Button(root, text="Confirm text", command=get_val).grid(row=1, column=1)
            size_entry = Entry(root)
            size_entry.grid(row=0, column=1)

            root.bind("<Return>", get_val)

        def reverse():
            global y
            y = 0
            print("reverse")

        def upright():
            global y
            y = breadth + 100
            print("upright")

        def go_next():
            global root
            root.destroy()
            skip()

        def direction():
            global root
            root = Tk()
            root.title("Direction of the graph")
            root.geometry('300x25')
            root.configure(bg='yellow2')

            d1 = Button(root, text="reverse", command=reverse, bg='cyan', fg='black').place(relx=0.84, rely=0)
            d2 = Button(root, text="upright", command=upright, bg='orange', fg='black').grid(row=1, column=1)
            next_button = Button(root, text="next", bg='green2', command=go_next).place(relx=0.42)

        def accept(event):
            global skip_entry, root, skip_value
            skip_value = int(skip_entry.get())
            print(skip_value)
            root.destroy()

        def yes_func():
            global yes, no, root, message, skip_entry
            yes.destroy()
            no.destroy()
            message.destroy()
            root.configure(bg='orange')
            message = Label(root, text='How many iterations do you want to skip?(press Enter when done) : ')
            message.grid(row=0, column=0)
            skip_entry = Entry(root)
            skip_entry.grid(row=0, column=1)
            root.bind('<Return>', accept)

        def no_func():
            global skip_value
            skip_value = 0
            root.destroy()

        def skip():
            global root, yes, no, message, skip_entry
            root = Tk()
            root.title("Iteration skip")
            root.configure(bg='light blue')

            message = Label(root,
                            text='Do you want to skip a few iterations?(recommended for array size greater than 500)(can be changed during visualisation)')
            message.grid(row=0, column=1)
            yes = Button(root, text='yes', command=yes_func)
            yes.grid(row=1, column=0)
            no = Button(root, text='no', command=no_func)
            no.grid(row=1, column=3)

        root.mainloop()

        running = True
        x = 0
        xincrement = 0
        y2 = 0
        elements = []
        generate_list(elements, size, breadth)
        if Sort == 'Bubble Sort' or Sort == 'Selection Sort':
            limit = len(elements)
        elif Sort == 'Super Selection Sort':
            limit = len(elements) / 2
        xincrement = length / len(elements)
        indx = 0
        iter = 0
        change_screen = True

        screen = pg.display.set_mode((length, breadth + 100))

        pg.display.set_caption("Sorting Visualizer ({})".format(Sort))
        # pg.display.set_icon(
            # pg.transform.scale(pg.image.load("C:/Users/Dell/Pictures/Saved Pictures/icon.png"), (32, 32)))
    else:
        length = 1000
        breadth = 500
        running = True
        x = 0
        xincrement = 0
        y2 = breadth
        colour = True
        elements = []
        size = 250
        generate_list(elements, size, breadth)
        Sort = "Selection Sort"
        if Sort == "Bubble Sort" or Sort == "Selection Sort":
            limit = len(elements)
        else:
            limit = len(elements) / 2
        xincrement = length / len(elements)
        indx = 0
        iter = 0
        change_screen = True
        y = 0
        wait_time = 0
        skip_value = 0
        screen = pg.display.set_mode((length, breadth + 100))
        pg.display.set_caption("Sorting Visualizer ({})".format(Sort))
        pg.display.set_icon(
            pg.transform.scale(pg.image.load("C:/Users/Dell/Pictures/Saved Pictures/icon.png"), (32, 32)))


def represent_data():
    initialize()
    global screen, running, x, xincrement, y2, BLACK, RED, BLUE, PURPLE, ORANGE, elements, indx, iter, change_screen, y, limit, l, b, wait_time, skip_value, colour
    fl = -1
    # Infinite while loop
    start_time = time.time()
    g1 = 0
    g2 = 0
    g3 = 0
    g4 = 0
    jval = 0
    iter = 0
    while running:
        # making the screen white
        # Drawing the data
        y2 = elements[indx]

        pg.draw.line(screen, BLACK, (x, y), (x, math.fabs(y - y2)), int(xincrement))

        if Sort == "Super Selection Sort":
            if colour:
                pg.draw.line(screen, PURPLE, (g1 * xincrement, y), (g1 * xincrement, math.fabs(y - elements[g2])),
                             int(xincrement))

            pg.draw.line(screen, RED, (g1 * xincrement, y), (g1 * xincrement, math.fabs(y - elements[g1])),
                         int(xincrement))

            pg.draw.line(screen, BLUE, (g2 * xincrement, y), (g2 * xincrement, math.fabs(y - elements[g2])),
                         int(xincrement))

            if colour:
                pg.draw.line(screen, ORANGE, (g2 * xincrement, y), (g2 * xincrement, math.fabs(y - elements[g1])),
                             int(xincrement))

            pg.draw.line(screen, RED, (g3 * xincrement, y), (g3 * xincrement, math.fabs(y - elements[g3])),
                         int(xincrement))

            if colour:
                pg.draw.line(screen, PURPLE, (g3 * xincrement, y), (g3 * xincrement, math.fabs(y - elements[g4])),
                             int(xincrement))

            if colour:
                pg.draw.line(screen, ORANGE, (g4 * xincrement, y), (g4 * xincrement, math.fabs(y - elements[g3])),
                             int(xincrement))

            pg.draw.line(screen, BLUE, (g4 * xincrement, y), (g4 * xincrement, math.fabs(y - elements[g4])),
                         int(xincrement))
        elif Sort == "Selection Sort":
            pg.draw.line(screen, RED, (g1 * xincrement, y), (g1 * xincrement, math.fabs(y - elements[g1])),
                         int(xincrement))

            if colour:
                pg.draw.line(screen, PURPLE, (g1 * xincrement, y), (g1 * xincrement, math.fabs(y - elements[g2])),
                             int(xincrement))

            if colour:
                pg.draw.line(screen, ORANGE, (g2 * xincrement, y), (g2 * xincrement, math.fabs(y - elements[g1])),
                             int(xincrement))

            pg.draw.line(screen, BLUE, (g2 * xincrement, y), (g2 * xincrement, math.fabs(y - elements[g2])),
                         int(xincrement))
        else:
            pg.draw.line(screen, BLUE, (g1 * xincrement, y), (g1 * xincrement, math.fabs(y - elements[g1])),
                         int(xincrement))

            pg.draw.line(screen, RED, (g2 * xincrement, y), (g2 * xincrement, math.fabs(y - elements[g2])),
                         int(xincrement))

        x += xincrement
        indx += 1
        # listening for events
        for event in pg.event.get():
            # checking whether the event is exit()
            if event.type == pg.QUIT:
                # exiting the loop by making the loop control variable false
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    if skip_value <= 0:
                        wait_time += 0.05
                        wait_time = round(wait_time, 2)
                    else:
                        skip_value -= 1
                        skip_value = round(skip_value)
                if event.key == pg.K_RIGHT:
                    if wait_time > 0:
                        wait_time -= 0.05
                        wait_time = round(wait_time)
                    else:
                        skip_value += 1
                        skip_value = round(skip_value)
                if event.key == pg.K_n:
                    wait_time = 0
                    skip_value = 0
        # updating the display
        if indx >= len(elements):
            if Sort == "Selection Sort":
                elements, g1, g2 = Selection_Sort(elements, iter)
            elif Sort == "Bubble Sort":
                elements, g1, g2, iter = Bubble_Sort(elements, iter, jval)
                jval = g1
            elif Sort == "Super Selection Sort":
                elements, g1, g2, g3, g4 = Super_SelectionSort(elements, iter)
            x = 0
            if Sort != "Bubble Sort":
                iter += 1
            jval += 1
            indx = 0
            if change_screen:
                time.sleep(math.fabs(wait_time))
                # noinspection PyUnresolvedReferences
                screen.fill((255, 255, 255))
        if skip_value > 0:
            if iter % (5 * skip_value) == 0:
                pg.display.flip()
        else:
            pg.display.flip()
        if iter >= limit:
            iter = 0
            jval = 0
            fl += 1
            change_screen = False
            screen.fill((255, 255, 255))
            colour = False
            if fl == 0:
                end_time = time.time()
                print(end_time - start_time)


# calling the function
represent_data()



