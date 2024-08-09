import time
from tkinter import *
from tkinter import ttk, messagebox

import pymysql
from PIL import ImageTk


class show_table:
    def __init__(self,root):
        self.root = root
        self.root.title("Bill Info")
        self.root.geometry('1360x760+0+0')
        self.root.menuBar_line = Canvas(self.root, width=1330, height=0.9, bg="olive", highlightthickness=0)
        self.root.menuBar_line.place(x=10, y=70)
        self.root.config(bg="white")

        self.bg = ImageTk.PhotoImage(file="images/brand_logo.png")
        self.bg_img = Label(self.root, image=self.bg, bg='white').place(x=0, y=0)

        def home_p():
            self.root.destroy()
            import admindas

        home_btn = Button(self.root, text="Home", font=("Goudy old style", 20, "bold"), foreground="orange",
                          bd=0, cursor="hand2", bg="white", activebackground='#fd6a36', activeforeground='white',command=home_p)
        home_btn.place(x=80, y=20, height=30, width=80)

        def mang():
            self.root.destroy()
            import adminmana

        manage_btn = Button(self.root, text="Manage", font=("Goudy old style", 20, "bold"), foreground="orange"
                            , bd=0, bg="white", cursor="hand2", activebackground='#fd6a36', activeforeground='white',
                            command=mang)
        manage_btn.place(x=170, y=20, height=30, width=85)

        def pur():
            self.root.destroy()
            import purcase_s

        acc_btn = Button(self.root, text="Purchase", font=("Goudy old style", 20, "bold"), foreground="orange"
                         , bd=0, bg="white", cursor="hand2", activebackground='#fd6a36', activeforeground='white',
                         command=pur)
        acc_btn.place(x=270, y=20, height=30, width=100)

        def bill():
            self.root.destroy()
            import bill_info

        bill_btn = Button(self.root, text="Bill Info", font=("Goudy old style", 20, "bold"), foreground="orange"
                          , bd=0, bg="white", cursor="hand2", activebackground='#fd6a36', activeforeground='white',
                          command=bill)
        bill_btn.place(x=380, y=20, height=30, width=105)

        def help():
            win = Toplevel()
            win.geometry("1360x760+0+0")
            win.title('help')
            # win.iconbitmap('images\\aa.ico')
            win.resizable(0, 0)

            win.bg = ImageTk.PhotoImage(file="images/project_help.jpg")
            win.bg_image = Label(win, image=win.bg).place(x=0, y=0, relwidth=1, relheight=1)

            win.mainloop()

        help_btn = Button(self.root, text="Help", font=("Goudy old style", 20, "bold"), foreground="orange",
                          bd=0, bg="white", cursor="hand2", activebackground='#fd6a36', activeforeground='white',
                          command=help)
        help_btn.place(x=490, y=20, height=30, width=55)

        def logout():
            logout = messagebox.askyesno("Exit", "Are you sure want to logout")
            if logout > 0:
                self.root.destroy()
                import loin

        logout_btn = Button(self.root, text="Logout", font=("Goudy old style", 20, "bold"), foreground="orange",
                            bg="white"
                            , bd=0, cursor="hand2", activebackground='#fd6a36', activeforeground='white',
                            command=logout)
        logout_btn.place(x=560, y=20, height=30, width=85)


        self.imae = ImageTk.PhotoImage(file="images/admin.jpg")
        self.lbl = Label(self.root,image=self.imae)
        self.lbl.place(x=1290, y=10, height=50, width=50)
        self.bll1 = Label(self.root, text="Admin", font=("Goudy old style", 30, "bold"), foreground="orange",
                          bg="white")
        self.bll1.place(x=1160, y=10, height=50, width=115)

        frame1 = Frame(self.root, bg="light gray", highlightbackground="black", highlightcolor="black",
                       highlightthickness=1)
        frame1.place(x=10, y=80, height=645, width=1330)


        frame_table = Frame(frame1, bg='#ffffff', bd=2.4, highlightbackground="black", highlightcolor="black",
                            highlightthickness=1)
        frame_table.place(x=250, y=90, height=520, width=870)

        def bck():
            self.root.destroy()
            import bill_info

        btntitle = Button(frame1,text="Back",font=("Goudy old style", 18, "bold"),foreground="White", bg="#4286f5", bd=1, cursor="hand2",
                            command=bck)
        btntitle.place(x=50,y=10)


        def times():
            current_time = time.strftime("%H:%M:%S")
            clock.config(text=current_time)
            clock.after(200, times)

        clock = Label(frame1, font=("Goudy old style", 20, "bold"), bg="light gray", foreground="#4286f5")
        clock.place(x=1165, y=10, height=30, width=100)
        times()

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview.Heading", font=("Goudy old style", 15, "bold"), background="light blue",
                             foreground="black")

        scroll_x = Scrollbar(frame_table, orient=HORIZONTAL)
        scroll_y = Scrollbar(frame_table, orient=VERTICAL)
        self.tbl = ttk.Treeview(frame_table, columns=("id", "billno", "date", "cash_name", "contact", "method"), cursor='hand2')
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.tbl.xview)
        scroll_y.config(command=self.tbl.yview)
        self.tbl.heading("id", text="ID", anchor=CENTER)
        self.tbl.heading("billno", text="Bill No", anchor=CENTER)
        self.tbl.heading("date", text="Date", anchor=CENTER)
        self.tbl.heading("cash_name", text="Casheir Name", anchor=CENTER)
        self.tbl.heading("contact", text="Contact", anchor=CENTER)
        self.tbl.heading("method", text="Method", anchor=CENTER)

        self.tbl['show'] = 'headings'

        self.tbl.column("id", width=30, anchor=CENTER)
        self.tbl.column("billno", width=50, anchor=CENTER)
        self.tbl.column("date", width=50, anchor=CENTER)
        self.tbl.column("cash_name", width=120, anchor=CENTER)
        self.tbl.column("contact", width=50, anchor=CENTER)
        self.tbl.column("method", width=40, anchor=CENTER)
        self.tbl.pack(fill=BOTH, expand=1)
        self.fetch_data()

    def fetch_data(self):
        con = pymysql.connect(host='localhost', user='root', password='Vedant@123', database='sin_up')
        mycursor = con.cursor()
        query = "SELECT * FROM data3"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        if len(rows)!=0:
            self.tbl.delete(*self.tbl.get_children())
            for row in rows:
                self.tbl.insert('',END,values=row)
            con.commit()
        con.close()


root = Tk()
obj = show_table(root)
root.mainloop()
