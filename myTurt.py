import tkinter

window = tkinter.Tk()
'''button = tkinter.Button(window, text="do not press", width=40)
button.pack(padx=10, pady=10)
clickCount = 0


def on_click(event):
    global clickCount
    clickCount = clickCount + 1
    if clickCount == 1:
        button.configure(text='seriously?')
    elif clickCount == 2:
        button.configure(text='twice?')
    else:
        button.pack_forget()


button.bind("<ButtonRelease-1>", on_click)'''
canvas = tkinter.Canvas(window, width=750, height=500, bg="white")
canvas.pack()
lastX, lastY = 0, 0
color = "black"


def store_position(event):
    global lastX, lastY
    lastX = event.x
    lastY = event.y


def on_click(event):
    store_position(event)


def on_drag(event):
    canvas.create_line(lastX, lastY, event.x, event.y, fill=color, width=3)
    store_position(event)


canvas.bind("<Button-1>", on_click)
canvas.bind("<B1-Motion>", on_drag)
window.mainloop()
