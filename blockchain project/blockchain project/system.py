import getpass
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def define_layout(obj, cols=1, rows=1):
    
    def method(trg, col, row):
        
        for c in range(cols):    
            trg.columnconfigure(c, weight=1)
        for r in range(rows):
            trg.rowconfigure(r, weight=1)

    if type(obj)==list:        
        [ method(trg, cols, rows) for trg in obj ]
    else:
        trg = obj
        method(trg, cols, rows)

def scan():
    return

def scanmanu(username):
    window = Tk()
    window.title('Blockchain')
    window.geometry("300x200")
    align_mode = 'nswe'
    pad = 5

    div_size = 200
    def prescan():
        window.destroy
        scan()

    div1 = Frame(window,  width=div_size , height=div_size , bg='white')
    div2 = Frame(window,  width=div_size , height=div_size , bg='white')

    window.update()
    win_size = min( window.winfo_width(), window.winfo_height())

    div1.grid(row=0, padx=pad, pady=pad, sticky=align_mode)
    div2.grid(row=1, padx=pad, pady=pad, sticky=align_mode)

    define_layout(window, cols=1, rows=2)
    define_layout([div1, div2])

    l11 = Label(div1, text='Welcome ' + username , bg='orange', fg='white')
    l11.grid(row=0, sticky=align_mode)

    l21 = Label(div2, text='Please upload QR code: ', bg='white', fg='black')
    bt1 = Button(div2, text='Scan QR code', bg='green', fg='white',command=lambda: scan())
    bt2 = Button(div2, text='Return', bg='green', fg='white',command = window.quit())
    bt3 = Button(div2, text='Quit', bg='green', fg='white',command = window.destroy)
    l4 = Label(div2, text="Produced by Clarus & Ryan", bg='white', fg='black',anchor="e")

    l21.grid(column=0, row=0, sticky=W) 
    bt1.grid(column=0, row=1,sticky=align_mode)
    bt2.grid(column=1, row=1,sticky=align_mode)
    bt3.grid(columnspan=3, sticky=align_mode)
    l4.grid(columnspan=4, sticky=E)

    define_layout(window, cols=1, rows=2)
    define_layout(div1, rows=1)
    define_layout(div2, rows=4)

    window.mainloop()

def genQRcode(code):
    return

def option(username):
    window = Tk()
    window.title('Blockchain')
    window.geometry("300x200")
    align_mode = 'nswe'
    pad = 5

    div_size = 200

    div1 = Frame(window,  width=div_size , height=div_size , bg='white')
    div2 = Frame(window,  width=div_size , height=div_size , bg='white')

    window.update()
    win_size = min( window.winfo_width(), window.winfo_height())

    div1.grid(row=0, padx=pad, pady=pad, sticky=align_mode)
    div2.grid(row=1, padx=pad, pady=pad, sticky=align_mode)

    define_layout(window, cols=1, rows=2)
    define_layout([div1, div2])

    l11 = Label(div1, text='Welcome ' + username , bg='orange', fg='white')
    l11.grid(row=0, sticky=align_mode)

    l21 = Label(div2, text='Please choose a product: ', bg='white', fg='black')
    bt1 = Button(div2, text='Apple', bg='green', fg='white',command= lambda:genQRcode(1))
    bt2 = Button(div2, text='Melon', bg='green', fg='white',command =lambda: genQRcode(2))
    bt3 = Button(div2, text='Stawberry', bg='green', fg='white',command =lambda: genQRcode(3))
    bt4 = Button(div2, text='Quit', bg='green', fg='white',command = window.destroy)
    l4 = Label(div2, text="Produced by Clarus & Ryan", bg='white', fg='black',anchor="e")

    l21.grid(column=0, row=0, sticky=W) 
    bt1.grid(column=0, row=1,sticky=align_mode)
    bt2.grid(column=1, row=1,sticky=align_mode)
    bt3.grid(column=2, row=1,sticky=align_mode)
    bt4.grid(columnspan=3, sticky=align_mode)
    l4.grid(columnspan=4, sticky=E)

    define_layout(window, cols=1, rows=2)
    define_layout(div1, rows=1)
    define_layout(div2, rows=4)

    window.mainloop()

def mainmanu(username):
    window = Tk()
    window.title('Blockchain')
    window.geometry("300x200")
    align_mode = 'nswe'
    pad = 5

    div_size = 200

    div1 = Frame(window,  width=div_size , height=div_size , bg='white')
    div2 = Frame(window,  width=div_size , height=div_size , bg='white')

    window.update()
    win_size = min( window.winfo_width(), window.winfo_height())

    div1.grid(row=0, padx=pad, pady=pad, sticky=align_mode)
    div2.grid(row=1, padx=pad, pady=pad, sticky=align_mode)

    define_layout(window, cols=1, rows=2)
    define_layout([div1, div2])

    l11 = Label(div1, text='Welcome ' + username , bg='orange', fg='white')
    l11.grid(row=0, sticky=align_mode)

    l21 = Label(div2, text='Please Perform operation: ', bg='white', fg='black')
    bt1 = Button(div2, text='Scan QR code', bg='green', fg='white',command= lambda: scanmanu(username))
    bt2 = Button(div2, text='Generate QR code', bg='green', fg='white',command =lambda:option(username))
    bt3 = Button(div2, text='Quit', bg='green', fg='white',command = window.destroy)
    l4 = Label(div2, text="Produced by Clarus & Ryan", bg='white', fg='black',anchor="e")

    l21.grid(column=0, row=0, sticky=W) 
    bt1.grid(column=0, row=1,sticky=align_mode)
    bt2.grid(column=1, row=1,sticky=align_mode)
    bt3.grid(columnspan=3, sticky=align_mode)
    l4.grid(columnspan=4, sticky=E)

    define_layout(window, cols=1, rows=2)
    define_layout(div1, rows=1)
    define_layout(div2, rows=4)

    window.mainloop()

def validate(username,password):
    if (username == "" or password == ""):
        messagebox.showwarning("System","Invalid username or password")
        return
    fname = open("login/username.txt")
    fword = open("login/password.txt")
    for cnt,line in enumerate (fname.readlines()):
        if username in line:
            for i,line2 in enumerate(fword.readlines()):
                if (password in line2) & (i == cnt):
                    fname.close()
                    fword.close()
                    mainmanu(validate(e21,e22)) 
                    return 
            fname.close()
            fword.close()
            messagebox.showwarning("System","Invalid password")
            return 
    fname.close()
    fword.close()
    messagebox.showwarning("System","Invalid username or password")
    return 

def register(username,password):
    if (username == "" or password == ""):
        messagebox.showwarning("System","Invalid username or password")
        return
    fname = open("login/username.txt","+r")
    fword = open("login/password.txt","+r")
    for line in enumerate (fname.readlines()):
        if username in line:
            messagebox.showwarning("System","Username already exists")
            fname.close()
            return
    fname.write("\n" + str(username))
    for line in enumerate (fword.readlines()):
        line = line
    fword.write("\n" + str(password))
    fname.close()
    fword.close()
    messagebox.showwarning("System","Register success")
    mainmanu(username)
    return

def login():
    window = Tk()
    window.title('Blockchain')
    window.geometry("300x200")
    align_mode = 'nswe'
    pad = 5

    div_size = 200

    div1 = Frame(window,  width=div_size , height=div_size , bg='white')
    div2 = Frame(window,  width=div_size , height=div_size , bg='white')

    window.update()
    win_size = min( window.winfo_width(), window.winfo_height())

    div1.grid(row=0, padx=pad, pady=pad, sticky=align_mode)
    div2.grid(row=1, padx=pad, pady=pad, sticky=align_mode)

    define_layout(window, cols=1, rows=2)
    define_layout([div1, div2])

    l11 = Label(div1, text='Welcome to fake product identification system', bg='orange', fg='white')
    l12 = Label(div1, text="Please log in", bg='orange', fg='white')
    l11.grid(row=0, sticky=align_mode)
    l12.grid(row=1, sticky=align_mode)    

    l21 = Label(div2, text='Username: ', bg='white', fg='black')
    e21 = Entry(div2, bg='white', fg='black')
    l22 = Label(div2, text='Password: ', bg='white', fg='black')
    e22 = Entry(div2, bg='white', fg='black')
    bt1 = Button(div2, text='Login', bg='green', fg='white',command = lambda: validate(e21.get(),e22.get()))
    bt2 = Button(div2, text='Register', bg='green', fg='white',command = lambda: register(e21.get(),e22.get()))
    bt3 = Button(div2, text='Quit', bg='green', fg='white',command = window.destroy)
    l4 = Label(div2, text="Produced by Clarus & Ryan", bg='white', fg='black',anchor="e")

    l21.grid(column=0, row=0, sticky=E)
    e21.grid(column=1, row=0, sticky=W)
    l22.grid(column=0, row=1, sticky=E)
    e22.grid(column=1, row=1, sticky=W)
    bt1.grid(column=0, row=2,sticky=align_mode)
    bt2.grid(column=1, row=2,sticky=align_mode)
    bt3.grid(columnspan=3, sticky=align_mode)
    l4.grid(columnspan=4, sticky=E)

    define_layout(window, cols=1, rows=2)
    define_layout(div1, rows=1)
    define_layout(div2, rows=4)
    window.mainloop()

mainmanu("clarus")


