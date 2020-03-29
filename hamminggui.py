import tkinter

# Dimensions of the window generated
HEIGHT = 600
WIDTH = 700
root = tkinter.Tk()

canvas = tkinter.Canvas(root, heigh=HEIGHT, width=WIDTH, bg='#ccffff')
canvas.pack()

frame = tkinter.Frame(root, bg='#b3b3ff', bd=5)
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

encodeButton = tkinter.Button(frame, text='Encode', bg='cyan', fg='red', font=40, command=test_function(entry.get()))
encodeButton.place(relx=0.0, rely=0.4, relwidth=0.5, relheight=0.2)

decodeButton = tkinter.Button(frame, text='Decode', bg='cyan', fg='red', font=40)
decodeButton.place(relx=0.5, rely=0.4, relwidth=0.5, relheight=0.2)

label = tkinter.Label(frame, text='bla bla bla', font=40)
label.place(relx=0.0, rely=0.6, relwidth=1.0, relheight=0.4)

entry = tkinter.Entry(frame, font=40)
entry.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.4)

root.mainloop()

def test_function(s):
    print(s)