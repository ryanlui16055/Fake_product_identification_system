import getpass
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import qr_code as qrCode

# import blockchain as blk_chain

window = Tk()
window.title("Blockchain")
window.geometry("450x350")
align_mode = "nswe"
pad = 5

div_size = 200


def define_layout(obj, cols=1, rows=1):
    def method(trg, col, row):

        for c in range(cols):
            trg.columnconfigure(c, weight=1)
        for r in range(rows):
            trg.rowconfigure(r, weight=1)

    if type(obj) == list:
        [method(trg, cols, rows) for trg in obj]
    else:
        trg = obj
        method(trg, cols, rows)


def scan():
    window = Tk()
    window.geometry("500x200")  # Size of the window
    window.title("Scaning")
    div1 = Frame(window, width=div_size, height=div_size, bg="white")
    div2 = Frame(window, width=div_size, height=div_size, bg="white")

    window.update()
    win_size = min(window.winfo_width(), window.winfo_height())

    div1.grid(row=0, padx=pad, pady=pad, sticky=align_mode)
    div2.grid(row=1, padx=pad, pady=pad, sticky=align_mode)
    define_layout(window, cols=1, rows=2)
    define_layout([div1,div2])
    l1 = Label(div1, text="Scan QR code", bg="orange", fg="white")

    b1 = Button(div2, text="Choose file", bg="green", fg="white",command=lambda: upload_file())
    b2 = Button(div2, text="Return",bg="green", fg="white",command=lambda: window.withdraw())
    l4 = Label(div2, text="Produced by Clarus & Ryan", bg="white", fg="black", anchor="e")
    l1.grid(row=0, sticky=align_mode)
    b1.grid(row=0, sticky=align_mode)
    b2.grid(row=1, sticky=align_mode)
    l4.grid(row=2, sticky=align_mode)

    def upload_file():
        global img
        f_types = [("Jpg Files", "*.jpg")]
        filename = filedialog.askopenfilename(filetypes=f_types)
        img = ImageTk.PhotoImage(file=filename)
        messagebox.showinfo(title="Scan QR code", message= "File upload successful" + "\nFile path:" + filename + "\nThe product is " )
    
    define_layout(window, cols=1, rows=2)
    define_layout(div1, rows=1)
    define_layout(div2, rows=3)
    window.mainloop()

def option():
    window = Tk()
    window.title("Generate QR code")
    window.geometry("500x200")

    div1 = Frame(window, width=div_size, height=div_size, bg="white")
    div2 = Frame(window, width=div_size, height=div_size, bg="white")

    window.update()
    win_size = min(window.winfo_width(), window.winfo_height())

    div1.grid(row=0, padx=pad, pady=pad, sticky=align_mode)
    div2.grid(row=1, padx=pad, pady=pad, sticky=align_mode)

    define_layout(window, cols=1, rows=2)
    define_layout([div1, div2])

    l11 = Label(div1, text="Select product ", bg="orange", fg="white")
    l11.grid(row=0, sticky=align_mode)

    l21 = Label(div2, text="Please choose a product: ", bg="white", fg="black")
    bt1 = Button(
        div2,
        text="Apple",
        bg="green",
        fg="white",
        command=lambda: qrCode.generate_QRcode("abc"),
    )
    bt2 = Button(
        div2,
        text="Melon",
        bg="green",
        fg="white",
        command=lambda: qrCode.generate_QRcode("abc"),
    )
    bt3 = Button(
        div2,
        text="Stawberry",
        bg="green",
        fg="white",
        command=lambda: qrCode.generate_QRcode("abc"),
    )
    bt4 = Button(div2, text="Return", bg="green", fg="white", command=window.destroy)
    l4 = Label(
        div2, text="Produced by Clarus & Ryan", bg="white", fg="black", anchor="e"
    )

    l21.grid(column=0, row=0, sticky=W)
    bt1.grid(column=0, row=1, sticky=align_mode)
    bt2.grid(column=1, row=1, sticky=align_mode)
    bt3.grid(column=2, row=1, sticky=align_mode)
    bt4.grid(columnspan=3, sticky=align_mode)
    l4.grid(columnspan=4, sticky=E)

    define_layout(window, cols=1, rows=2)
    define_layout(div1, rows=1)
    define_layout(div2, rows=4)

    window.mainloop()

def addrecord(code):
    return

def add():
    window = Tk()
    window.title("Add transaction record")
    window.geometry("500x200")

    div1 = Frame(window, width=div_size, height=div_size, bg="white")
    div2 = Frame(window, width=div_size, height=div_size, bg="white")

    window.update()
    win_size = min(window.winfo_width(), window.winfo_height())

    div1.grid(row=0, padx=pad, pady=pad, sticky=align_mode)
    div2.grid(row=1, padx=pad, pady=pad, sticky=align_mode)

    define_layout(window, cols=1, rows=2)
    define_layout([div1, div2])

    l11 = Label(div1, text="Add transaction record", bg="orange", fg="white")
    l11.grid(row=0, sticky=align_mode)
    l21 = Label(div2, text="Username: ", bg="white", fg="black")
    e21 = Entry(div2, bg="white", fg="black")
    l22 = Label(div2, text="Password: ", bg="white", fg="black")
    e22 = Entry(div2, bg="white", fg="black")
    l23 = Label(div2, text="Please choose a product: ", bg="white", fg="black")
    bt1 = Button(
        div2,
        text="Apple",
        bg="green",
        fg="white",
        command=lambda: addrecord("abc"),
    )
    bt2 = Button(
        div2,
        text="Melon",
        bg="green",
        fg="white",
        command=lambda: addrecord("abc"),
    )
    bt3 = Button(
        div2,
        text="Stawberry",
        bg="green",
        fg="white",
        command=lambda: addrecord("abc"),
    )
    bt4 = Button(div2, text="Return", bg="green", fg="white", command=window.destroy)
    l4 = Label(
        div2, text="Produced by Clarus & Ryan", bg="white", fg="black", anchor="e"
    )

    l21.grid(column=0, row=0,padx=20,ipadx=20,sticky=W)
    e21.grid(column=0, row=0)
    l22.grid(column=0, row=1,padx=20,ipadx=20,sticky=W)
    e22.grid(column=0, row=1)
    l23.grid(columnspan=1, sticky=align_mode)
    bt1.grid(column=0, row=2, sticky=align_mode)
    bt2.grid(column=1, row=2, sticky=align_mode)
    bt3.grid(column=2, row=2, sticky=align_mode)
    bt4.grid(columnspan=3, sticky=align_mode)
    l4.grid(columnspan=4, sticky=E)

    define_layout(window, cols=1, rows=2)
    define_layout(div1, rows=1)
    define_layout(div2, rows=4)

    window.mainloop()


def usermanu(username):
    window.withdraw()
    manu = Tk()
    manu.title("Blockchain")
    manu.geometry("300x200")

    div1 = Frame(manu, width=div_size, height=div_size, bg="white")
    div2 = Frame(manu, width=div_size, height=div_size, bg="white")

    manu.update()
    win_size = min(manu.winfo_width(), manu.winfo_height())

    div1.grid(row=0, padx=pad, pady=pad, sticky=align_mode)
    div2.grid(row=1, padx=pad, pady=pad, sticky=align_mode)

    define_layout(manu, cols=1, rows=2)
    define_layout([div1, div2])

    l11 = Label(div1, text="Welcome " + username, bg="orange", fg="white")
    l11.grid(row=0, sticky=align_mode)

    l21 = Label(div2, text="Please Perform operation: ", bg="white", fg="black")
    bt1 = Button(
        div2, text="Scan QR code", bg="green", fg="white", command=lambda: scan()
    )
    bt2 = Button(
        div2,
        text="Generate QR code",
        bg="green",
        fg="white",
        command=lambda: option(username),
    )
    bt3 = Button(div2, text="Quit", bg="green", fg="white", command=manu.destroy)
    l4 = Label(
        div2, text="Produced by Clarus & Ryan", bg="white", fg="black", anchor="e"
    )

    l21.grid(column=0, row=0, sticky=W)
    bt1.grid(columnspan=1, sticky=align_mode)
    bt2.grid(columnspan=2, sticky=align_mode)
    bt3.grid(columnspan=3, sticky=align_mode)
    l4.grid(columnspan=4, sticky=E)

    define_layout(manu, cols=1, rows=2)
    define_layout(div1, rows=1)
    define_layout(div2, rows=4)

    manu.mainloop()


def adminmanu(username):
    window.withdraw()
    manu = Tk()
    manu.title("Blockchain")
    manu.geometry("500x200")

    div1 = Frame(manu, width=div_size, height=div_size, bg="white")
    div2 = Frame(manu, width=div_size, height=div_size, bg="white")

    manu.update()
    win_size = min(manu.winfo_width(), manu.winfo_height())

    div1.grid(row=0, padx=pad, pady=pad, sticky=align_mode)
    div2.grid(row=1, padx=pad, pady=pad, sticky=align_mode)

    define_layout(manu, cols=1, rows=2)
    define_layout([div1, div2])

    l11 = Label(div1, text="Welcome admin " + username, bg="orange", fg="white")
    l11.grid(row=0, sticky=align_mode)

    l21 = Label(div2, text="Please Perform operation: ", bg="white", fg="black")
    bt1 = Button(
        div2, text="Scan QR code", bg="green", fg="white", command=lambda: scan()
    )
    bt2 = Button(
        div2, text="Generate QR code", bg="green", fg="white", command=lambda: option()
    )
    bt3 = Button(
        div2,
        text="Add transaction record",
        bg="green",
        fg="white",
        command=lambda: add(),
    )
    bt4 = Button(div2, text="Quit", bg="green", fg="white", command=manu.destroy)
    l4 = Label(
        div2, text="Produced by Clarus & Ryan", bg="white", fg="black", anchor="e"
    )

    l21.grid(column=0, row=0, sticky=W)
    bt1.grid(column=0, row=1, sticky=align_mode)
    bt2.grid(column=1, row=1, sticky=align_mode)
    bt3.grid(column=2, row=1, sticky=align_mode)
    bt4.grid(columnspan=3, sticky=align_mode)
    l4.grid(columnspan=4, sticky=E)

    define_layout(manu, cols=1, rows=2)
    define_layout(div1, rows=1)
    define_layout(div2, rows=4)

    manu.mainloop()


def validate(username, password):
    if username == "" or password == "":
        messagebox.showwarning("System", "Invalid username or password")
        return
    fname = open(r".\blockchain_project\blockchain_project\login\username.txt")
    fword = open(r".\blockchain_project\blockchain_project\login\password.txt")
    for cnt, line in enumerate(fname.readlines()):
        if username in line:
            for i, line2 in enumerate(fword.readlines()):
                if (password in line2) & (i == cnt):
                    fname.close()
                    fword.close()
                    if username == "clarus" or username == "ryan":
                        adminmanu(username)
                    else:
                        usermanu(username)
            fname.close()
            fword.close()
            messagebox.showwarning("System", "Invalid password")
            return
    fname.close()
    fword.close()
    messagebox.showwarning("System", "Invalid username or password")
    return


def register(username, password):
    if username == "" or password == "":
        messagebox.showwarning("System", "Invalid username or password")
        return
    fname = open(r".\blockchain_project\blockchain_project\login\username.txt", "+r")
    fword = open(r".\blockchain_project\blockchain_project\login\password.txt", "+r")
    for line in enumerate(fname.readlines()):
        if username in line:
            messagebox.showwarning("System", "Username already exists")
            fname.close()
            return
    fname.write("\n" + str(username))
    for line in enumerate(fword.readlines()):
        line = line
    fword.write("\n" + str(password))
    fname.close()
    fword.close()
    messagebox.showwarning("System", "Register success")
    usermanu(username)
    return


# root
div1 = Frame(window, width=div_size, height=div_size, bg="white")
div2 = Frame(window, width=div_size, height=div_size, bg="white")

window.update()
win_size = min(window.winfo_width(), window.winfo_height())

div1.grid(row=0, padx=pad, pady=pad, sticky=align_mode)
div2.grid(row=1, padx=pad, pady=pad, sticky=align_mode)

define_layout(window, cols=1, rows=2)
define_layout([div1, div2])

l11 = Label(
    div1, text="Welcome to fake product identification system", bg="orange", fg="white"
)
l12 = Label(div1, text="Please log in", bg="orange", fg="white")
l11.grid(row=0, sticky=align_mode)
l12.grid(row=1, sticky=align_mode)

l21 = Label(div2, text="Username: ", bg="white", fg="black")
e21 = Entry(div2, bg="white", fg="black")
l22 = Label(div2, text="Password: ", bg="white", fg="black")
e22 = Entry(div2, bg="white", fg="black")
bt1 = Button(
    div2,
    text="Login",
    bg="green",
    fg="white",
    command=lambda: validate(e21.get(), e22.get()),
)
bt2 = Button(
    div2,
    text="Register",
    bg="green",
    fg="white",
    command=lambda: register(e21.get(), e22.get()),
)
bt3 = Button(div2, text="Quit", bg="green", fg="white", command=window.destroy)
l4 = Label(div2, text="Produced by Clarus & Ryan", bg="white", fg="black", anchor="e")

l21.grid(column=0, row=0,padx=20,ipadx=20,sticky=W)
e21.grid(column=0, row=0)
l22.grid(column=0, row=1,padx=20,ipadx=20,sticky=W)
e22.grid(column=0, row=1)
bt1.grid(columnspan=2, sticky=align_mode)
bt2.grid(columnspan=3, sticky=align_mode)
bt3.grid(columnspan=4, sticky=align_mode)
l4.grid(columnspan=5, sticky=E)

define_layout(window, cols=1, rows=2)
define_layout(div1, rows=1)
define_layout(div2, rows=5)
window.mainloop()
