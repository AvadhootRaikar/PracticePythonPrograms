# ATM System Using Tkinter

from tkinter import *
import mysql.connector as msc

win = Tk()

win.title(" FRIENDS CO. OP. BANK ")
win.geometry("1366x768")
l = Frame(win, borderwidth = 150)
l.pack(side = "left", expand = "True")
con = msc.connect(host = 'slab-main', user = "SUSHANT", passwd = "009619", database = "sushant009619")
con.autocommit = True
cursor = con.cursor()
use = ""

def destroy(a):
    a.destroy() 

def opt():
    global win
    destroy(win)
    win = Tk()
    l = Frame(win, borderwidth = 150)
    l.pack(side = "left", expand = "True")
    win.geometry("1366x768")
    Label(l, text = "Logging in as:").pack()
    Button(l, text = "Admin", command = lambda: admlogin("")).pack()
    Button(l, text = "Client", command = lambda: cltlogin("")).pack()
    Label(l, text = "  ").pack()
    Button(l, text = "Quit", command = lambda: destroy(win)).pack()

def admlogin(x):
    global win
    global e
    destroy(win)
    win = Tk()
    l = Frame(win, borderwidth = 150)
    l.pack(side = "left", expand = "True")
    win.geometry("1366x768")
    Label(l, text = x).pack()
    Label(l, text = "Enter password: ").pack()
    e = Entry(l, show = "*")
    e.focus()
    e.bind("<Return>", check)
    e.pack()
    Button(l, text = "Submit", command = lambda: check()).pack()
    Button(l, text = "Go Back", command = lambda: opt()).pack()

def check(arg = None):
    global e
    if e.get() == "494949":
        admin()
    else:
        admlogin(" Wrong password ...")
       

def cltlogin(x):
    global win
    global pin
    destroy(win)
    win = Tk()
    l = Frame(win, borderwidth = 150)
    l.pack(side = "left", expand = "True")
    win.geometry("1366x768")
    Label(l, text = x).pack()
    Label(l, text = "Enter password").pack()
    pin = Entry(l, show = "*")
    pin.focus()
    pin.bind("<Return>", alsocheck)
    pin.pack()
    Button(l, text = "submit", command = lambda: alsocheck()).pack()
    Button(l, text = "Go back", command = lambda: opt()).pack()

def alsocheck(arg = None):
    global cursor
    global pin2
    pin2 = pin.get()
    cursor.execute("SELECT customerid FROM customer where customerid = %s;", (pin2,))
    cursor.fetchall()
    if cursor.rowcount > 0:
        client()
    else:
        cltlogin("Bhai kisko ullu bana raha hai")

def admin():
    global win
    destroy(win)
    win = Tk()
    l = Frame(win, borderwidth = 150)
    l.pack(side = "left", expand = "True")
    win.geometry("1366x768")
    Label(l, text = "Login successful").pack()
    Button(l, text = "Add user", command = lambda: adduser("")).pack()
    Button(l, text = "Delete user", command = lambda: deleteuser("")).pack()
    Button(l, text = "Update user", command = lambda: updateuser("")).pack()
    Button(l, text = "Search user", command = lambda: searchuser()).pack()
    Button(l, text = "Report", command = lambda: report()).pack()
    Label(l, text = " ").pack()
    Button(l, text = "Quit", command = lambda: destroy(win)).pack()

def client():
    global win
    global cursor
    global pin2
    cursor.execute("SELECT customername FROM customer WHERE customerid = %s;", (pin2,))
    welc = cursor.fetchall()
    destroy(win)
    win = Tk()
    l = Frame(win, borderwidth = 150)
    l.pack(side = "left", expand = "True")
    win.geometry("1366x768")
    Label(l, text = "Login successful").pack()
    Label(l, text = ("Welcome " + welc[0][0])).pack()
    Button(l, text = "Deposit money", command = lambda: payin()).pack()
    Button(l, text = "Withdraw", command = lambda: withdraw()).pack()
    Button(l, text = "Check balance", command = lambda: balancecheck()).pack()
    Button(l, text = "Transfer money to another account", command = lambda: transfer()).pack()
    Button(l, text = "Receipt", command = lambda: receipt()).pack()
    Label(l, text = " ").pack()
    Button(l, text = "Quit", command = lambda: destroy(win)).pack()
           
def adduser(x):
    global win
    global e1
    global e2
    global e3
    destroy(win)
    win = Tk()
    l = Frame(win, borderwidth = 150)
    l.pack(side = "left", expand = "True")
    win.geometry("1366x768")
    Label(l, text = x).grid(row = 0, column = 1)
    Label(l, text = "Enter the 5- Digit ID of the user to be added : ").grid(row = 1, column = 1)
    e1 = Entry(l)
    e1.grid(row = 1, column = 2)
    Label(l, text = "Enter the name of the user to be added : ").grid(row = 2, column = 1)
    e2 = Entry(l)
    e2.grid(row = 2, column = 2)
    Label(l, text = " Enter Balance to be added in user's account :").grid(row = 3, column = 1)
    e3 = Entry(l)
    e3.bind("<Return>", summit)
    e3.grid(row = 3, column = 2)
    Button(l, text = "Submit", command = lambda: summit()).grid(row = 4, column = 2)
    Button(l, text = "Go Back", command = lambda: admin()).grid(row = 5, column = 2)

def summit(arg = None):
    global e1
    global e2
    global e3
    global con
    userid = e1.get()
    username = e2.get()
    balance = e3.get()
    insert = "insert into customer(customerid, customername, balance) values(%s, %s, %s);"
    val = (userid, username, balance)
    omy = cursor.execute(insert, val)
    con.commit()
    adduser("Done!")

def deleteuser(x):
    global win
    global userid
    destroy(win)
    win = Tk()
    l = Frame(win, borderwidth = 150)
    l.pack(side = "left", expand = "True")
    win.geometry("1366x768")
    Label(l, text = x).pack()
    Label(l, text = "Enter the 5- Digit ID of the user to be deleted : ").pack()
    userid = Entry(l)
    userid.focus()
    userid.bind("<Return>", delete)
    userid.pack()
    Button(l, text = "Submit", command = lambda: delete()).pack()
    Button(l, text = "Go Back", command = lambda: admin()).pack()

def delete(arg = None):
    global cursor
    global userid
    global con
    dele = userid.get()
    cursor.execute("delete from customer where customerid = %s ;" ,( dele,))
    con.commit()
    deleteuser("Done!")

def updateuser(x):
    global win
    global updateid
    global whatupdate
    destroy(win)
    win = Tk()
    l = Frame(win, borderwidth = 150)
    l.pack(side = "left", expand = "True")
    win.geometry("1366x768")
    Label(l, text = x).grid(row = 0, column = 1)
    Label(l, text = "Enter the 5- Digit ID of the user to be updated : ").grid(row = 1, column = 1)
    updateid = Entry(l)
    updateid.focus()
    updateid.grid(row = 1, column = 2)
    Label(l, text = "What are you updating?(username/balance)").grid(row = 2, column = 1)
    whatupdate = Entry(l)
    whatupdate.grid(row = 2, column = 2)
    Button(l, text = "Submit", command = lambda: updog()).grid(row = 3, column = 2) # Ask Apoorva "what's updog"
    Button(l, text = "Go Back", command = lambda: admin()).grid(row = 4, column = 2)

def updog():
    global win
    global con
    global whatupdate
    global updateid
    global updatename
    global updatebal
    global blah
    global blehid
    blah = whatupdate.get()
    blehid = updateid.get()
    destroy(win)
    win = Tk()
    l = Frame(win, borderwidth = 150)
    l.pack(side = "left", expand = "True")
    win.geometry("1366x768")
    if blah.lower() == "username":
        Label(l, text = "Enter the name of the user to be updated: ").pack()
        updatename = Entry(l)
        updatename.focus()
        updatename.bind("<Return>", thirddef)
        updatename.pack()
        Button(l, text = "Change", command = lambda: thirddef()).pack()
    elif blah.lower() == "balance":
        Label(l, text = "Enter the balance of the user to be updated: ").pack()
        updatebal = Entry(l)
        updatebal.focus()
        updatebal.bind("<Return>", thirddef)
        updatebal.pack()
        Button(l, text = "Change", command = lambda: thirddef()).pack()
        Button(l, text = " changed", command = lambda: updateuser()).pack()
       
def thirddef(arg = None):
    global blah
    global blehid
    global updatename
    global updatebal
    global cursor
    global con
    if blah.lower() == "username":
        upname = updatename.get()
        cursor.execute("update customer set customername = %s where customerid = %s ;",(upname,blehid))
        con.commit()
        updateuser("Done!")
    elif blah.lower() == "balance":
        upbal = updatebal.get()
        update2 = cursor.execute("update customer set balance = %s where customerid = %s ;",(upbal,blehid))
        con.commit()
        updateuser("Done!")

def searchuser():
    global win
    global searchid
    destroy(win)
    win = Tk()
    l = Frame(win, borderwidth = 150)
    l.pack(side = "left", expand = "True")
    win.geometry("1366x768")
    Label(l, text = "Enter the 5- Digit ID of the user you are searching : ").pack()
    searchid = Entry(l)
    searchid.focus()
    searchid.bind("<Return>", search)
    searchid.pack()
    Button(l, text = "Submit", command = lambda: search()).pack()
    Button(l, text = "Go Back", command = lambda: admin()).pack()

def search(arg = None):
    global win
    global cursor
    global searchid
    global con
    lel = searchid.get()
    cursor.execute("select * from customer where customerid = %s;", (lel,))
    data = cursor.fetchall()
    destroy(win)
    win = Tk()
    l = Frame(win, borderwidth = 150)
    l.pack(side = "left", expand = "True")
    win.geometry("1366x768")
    Label(l, text = "The details of the user are : ").pack()
    for row in data:
        Label(l, text = row).pack()
    Button(l, text = "Go back", command = lambda: admin()).pack()


def report():
    global win
    global reportid
    destroy(win)
    win = Tk()
    l = Frame(win, borderwidth = 150)
    l.pack(side = "left", expand = "True")
    win.geometry("1366x768")
    Label(l, text = "Enter the 5- Digit ID for the report: ").pack()
    reportid = Entry(l)
    reportid.focus()
    reportid.bind("<Return>", pura)
    reportid.pack()
    Button(l, text = "Submit", command = lambda: pura()).pack()
    Button(l, text = "Go Back", command = lambda: admin()).pack()

def pura(arg = None):
    global win
    global reportid
    lele = reportid.get()
    cursor.execute("select * from customer where customerid = %s;",(lele,))
    data = cursor.fetchall()
    destroy(win)
    win = Tk()
    l = Frame(win, borderwidth = 150)
    l.pack(side = "left", expand = "True")
    win.geometry("1366x768")
    for i in data[0]:
        Label(l, text = i).pack()
    Button(l, text = "Go back", command = lambda: admin()).pack() 

def payin():
    global win
    global entry1
    global use
    use += "\n Added amount"
    destroy(win)
    win = Tk()
    l = Frame(win, borderwidth = 150)
    l.pack(side = "left", expand = "True")
    win.geometry("1366x768")
    Label(l, text = "Enter amount to be added here").pack()
    entry1 = Entry(l)
    entry1.focus()
    entry1.bind("<Return>", hogaya)
    entry1.pack()
    Button(l, text = "Submit", command = lambda: hogaya()).pack()
    Button(l, text = "Go back", command = lambda: client()).pack()

def hogaya(arg = None):
    global win
    global cursor
    global entry1
    global pin2
    global con
    ans = entry1.get()
    cursor.execute("UPDATE customer SET balance = balance + %s WHERE customerid = %s;", (ans, pin2))
    con.commit()
    cursor.execute("SELECT balance FROM customer WHERE customerid = %s", (pin2,))
    data = cursor.fetchall()
    destroy(win)
    win = Tk()
    l = Frame(win, borderwidth = 150)
    l.pack(side = "left", expand = "True")
    win.geometry("1366x768")
    Label(l, text = "Balance:").pack()
    Label(l, text = str(data[0][0])).pack()
    Button(l, text = "Go Back", command = lambda: client()).pack()

def withdraw():
    global use
    global win
    global cursor
    global pin
    global e1
    destroy(win)
    win = Tk()
    l = Frame(win, borderwidth = 150)
    l.pack(side = "left", expand = "True")
    win.geometry("1366x768")
    use += "\n Withdrew money"
    Label(l, text = "How much Would you like to withdraw? ").pack()
    e1 = Entry(l)
    e1.focus()
    e1.bind("<Return>", dede)
    e1.pack()
    Button(l, text = "Submit", command = lambda: dede()).pack()
    Button(l, text = "Go back", command = lambda: client()).pack()
   
def dede(arg = None):
    global win
    global e1
    global pin2
    global cursor
    global con
    ans = e1.get()
    cursor.execute("UPDATE customer SET balance = balance - %s WHERE customerid = %s;", (ans, pin2))
    con.commit()
    cursor.execute("SELECT balance FROM customer WHERE customerid = %s;", (pin2,))
    ishanbal = cursor.fetchall()
    destroy(win)
    win = Tk()
    l = Frame(win, borderwidth = 150)
    l.pack(side = "left", expand = "True")
    win.geometry("1366x768")
    Label(l, text = "New Balance:").pack()
    Label(l, text = ishanbal).pack()
    Button(l, text = "Go back", command = lambda: client()).pack()

def balancecheck():
    global use
    global win
    global cursor
    global pin2
    global n
    use += "\n Checked Balance"
    cursor.execute("SELECT balance FROM customer WHERE customerid = %s;", (pin2,))
    data = cursor.fetchall()
    destroy(win)
    win = Tk()
    l = Frame(win, borderwidth = 150)
    l.pack(side = "left", expand = "True")
    win.geometry("1366x768")
    Label(l, text = " Your balance is ").pack()
    Label(l, text = data).pack()
    Button(l, text = " Go Back", command = lambda: client()).pack()
       
def transfer():
    global use
    global win
    global cursor
    global pin
    global en1
    global en2
    use += "\n Transferred money"
    destroy(win)
    win = Tk()
    l = Frame(win, borderwidth = 150)
    l.pack(side = "left", expand = "True")
    win.geometry("1366x768")
    Label(l, text = "To which account you want to transfer money").pack()
    en1 = Entry(l)
    en1.focus()
    en1.pack()
    Label(l, text = "please enter the amount you wanted to transfer ").pack()
    en2 = Entry(l)
    en2.bind("<Return>", teranahimeranahi)
    en2.pack()
    Button(l, text = " TRANSFER", command = lambda: teranahimeranahi()).pack()
    Button(l, text = " Go back", command = lambda: client()).pack()
   
def teranahimeranahi(arg = None):
    global win
    global en1
    global en2
    global cursor
    global con
    global pin2
    pintya = en1.get() 
    amt = en2.get() 
    cursor.execute("UPDATE customer SET balance = balance - %s WHERE customerid = %s;", (amt, pin2))
    con.commit()
    cursor.execute("UPDATE customer SET balance = balance + %s WHERE customerid = %s;", (amt, pintya))
    con.commit()
    cursor.execute("SELECT balance FROM customer WHERE customerid = %s;", (pin2,))
    data = cursor.fetchall()
    destroy(win)
    win = Tk()
    l = Frame(win, borderwidth = 150)
    l.pack(side = "left", expand = "True")
    win.geometry("1366x768")
    Label(l, text = "Your balance:").pack()
    Label(l, text = data).pack()
    Button(l, text = "Click here to check status", command = lambda: client()).pack()

def receipt():
    global win
    global use
    global cursor
    destroy(win)
    win = Tk()
    l = Frame(win, borderwidth = 150)
    l.pack(side = "left", expand = "True")
    win.geometry("1366x768")
    win.title("Receipt")
    Label(l, text = "Receipt ").pack()
    Label(l, text = " ").pack()
    Label(l, text = ("You: %s" % use)).pack()
    Button(l, text = "Quit", command = lambda: destroy(win)).pack()

Button(l, text = "Start", command = lambda: opt()).pack()
Label(l, text = " ").pack()
Button(l, text = "Exit", command = lambda: destroy(win)).pack()
win.mainloop()
