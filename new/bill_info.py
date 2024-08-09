import time
from tkinter import Tk, Canvas, messagebox, ttk
from tkinter import *

import pymysql
from PIL import ImageTk


class bill_info:
    def __init__(self,root):
        self.root = root
        self.root.title("Bill Info")
        self.root.geometry('1360x760+0+0')
        self.root.menuBar_line = Canvas(self.root, width=1330, height=0.9, bg="olive", highlightthickness=0)
        self.root.menuBar_line.place(x=10, y=70)
        self.root.config(bg="white")

        # =========all variables========#
        self.id_var = StringVar()
        self.billno_var = StringVar()
        self.date_var = StringVar()
        self.cashname_var = StringVar()
        self.contact_var = StringVar()
        self.method_var = StringVar()

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


        self.img = ImageTk.PhotoImage(file="images/admin.jpg")
        self.lbl = Label(self.root, image=self.img)
        self.lbl.place(x=1290, y=10, height=50, width=50)
        self.bll1 = Label(self.root, text="Admin", font=("Goudy old style", 30, "bold"), foreground="orange",
                          bg="white")
        self.bll1.place(x=1160, y=10, height=50, width=115)

        frame1 = Frame(self.root,bg="light gray",highlightbackground="black", highlightcolor="black",
                       highlightthickness=1)
        frame1.place(x=10,y=80,height=645,width=1330)

        def times():
            current_time = time.strftime("%H:%M:%S")
            clock.config(text=current_time)
            clock.after(200, times)

        clock = Label(frame1, font=("Goudy old style", 20, "bold"), bg="light gray", foreground="#4286f5")
        clock.place(x=1165, y=10, height=30, width=100)
        times()

        lbl_title = Label(frame1,text="Manage Bill Info",font=("Goudy old style", 23, "bold","underline"),bg="light gray")
        lbl_title.place(x=550,y=15)

        frem_1 = Frame(frame1, bg='#ffffff', bd=2.4, highlightbackground="black", highlightcolor="black",
                       highlightthickness=1)
        frem_1.place(x=220, y=75, height=540, width=410)

        self.lbl_id = Label(frem_1, text='ID :', font=("Goudy old style", 20, "bold"), bg='white')
        self.lbl_id.place(x=0, y=20, width=45, height=20)
        self.id_ent = ttk.Combobox(frem_1, font=("Modern No.20", 13),textvariable=self.id_var)
        self.id_ent.place(x=50, y=20, height=20, width=150)
        self.id_ent.bind("<<ComboboxSelected>>", self.show_details)
        self.fetch_combo()
        self.id_ent.focus()


        self.lbl_bill = Label(frem_1, text='Bill No :', font=("Goudy old style", 20, "bold"), bg='white')
        self.lbl_bill.place(x=20, y=60, height=30, width=100)
        self.bill_ent = Entry(frem_1, font=("Modern No.20", 13), highlightthickness=1, relief=FLAT,textvariable=self.billno_var)
        self.bill_ent.place(x=20, y=100, height=30, width=200)
        self.bill_ent.config(highlightbackground="black", highlightcolor="orange")
        self.bill_ent.configure(state="disabled")

        self.lbl_date = Label(frem_1, text='Date :', font=("Goudy old style", 20, "bold"), bg='white')
        self.lbl_date.place(x=20, y=150, height=30, width=70)
        self.date_ent = Entry(frem_1, font=("Modern No.20", 13), highlightthickness=1, relief=FLAT,textvariable=self.date_var)
        self.date_ent.place(x=20, y=190, height=30, width=200)
        self.date_ent.config(highlightbackground="black", highlightcolor="orange")
        self.date_ent.configure(state="disabled")

        self.lbl_cash = Label(frem_1, text='Casheir Name :', font=("Goudy old style", 20, "bold"), bg='white')
        self.lbl_cash.place(x=20, y=240, height=30, width=170)
        self.cash_ent = Entry(frem_1, font=("Modern No.20", 13), highlightthickness=1, relief=FLAT,textvariable=self.cashname_var)
        self.cash_ent.place(x=20, y=280, height=30, width=200)
        self.cash_ent.config(highlightbackground="black", highlightcolor="orange")
        self.cash_ent.configure(state="disabled")

        self.lbl_contact = Label(frem_1, text='Contact :', font=("Goudy old style", 20, "bold"), bg='white')
        self.lbl_contact.place(x=20, y=330, height=30, width=105)
        self.contact_ent = Entry(frem_1, font=("Modern No.20", 13), highlightthickness=1, relief=FLAT,textvariable=self.contact_var)
        self.contact_ent.place(x=20, y=370, height=30, width=200)
        self.contact_ent.config(highlightbackground="black", highlightcolor="orange")
        self.contact_ent.configure(state="disabled")

        self.lbl_method = Label(frem_1, text='Method :', font=("Goudy old style", 20, "bold"), bg='white')
        self.lbl_method.place(x=20, y=420, height=30, width=100)
        self.method_ent = Entry(frem_1, font=("Modern No.20", 13), highlightthickness=1, relief=FLAT,textvariable=self.method_var)
        self.method_ent.place(x=20, y=460, height=30, width=200)
        self.method_ent.config(highlightbackground="black", highlightcolor="orange")
        self.method_ent.configure(state="disabled")


        def dell():
            if self.id_ent.get()=="":
                messagebox.showerror("Error!","Please search Record...!")
            elif self.bill_ent.get()=="" or self.date_ent.get()=="":
                messagebox.showerror("Error!", "Please search Record...!")
            else :
                con = pymysql.connect(host='localhost', user='root', password='Vedant@123', database='sin_up')
                mycursor = con.cursor()
                query = "DELETE FROM data3 WHERE billno = %s"
                mycursor.execute(query, self.billno_var.get())
                con.commit()
                con.close()
                messagebox.showinfo("success", "Data Deleted Successfully.....!")
                clear()
                self.fetch_combo()
                self.id_ent.focus()

        self.btn_del = Button(frem_1,text="Delete",font=("Goudy old style", 18, "bold"),bd=1,bg="#4286f5",foreground="White",cursor="hand2",command=dell)
        self.btn_del.place(x=280,y=40,height=35,width=110)

        def clear():
            self.id_ent.set("")
            self.bill_ent.configure(state="normal")
            self.date_ent.configure(state="normal")
            self.cash_ent.configure(state="normal")
            self.contact_ent.configure(state="normal")
            self.method_ent.configure(state="normal")
            self.textarea.configure(state="normal")
            self.bill_ent.delete(0, END)
            self.date_ent.delete(0, END)
            self.cash_ent.delete(0, END)
            self.contact_ent.delete(0, END)
            self.method_ent.delete(0, END)
            self.textarea.delete(1.0, END)
            self.bill_ent.configure(state="disabled")
            self.date_ent.configure(state="disabled")
            self.cash_ent.configure(state="disabled")
            self.contact_ent.configure(state="disabled")
            self.method_ent.configure(state="disabled")
            self.id_ent.focus()

        self.btn_clr = Button(frem_1, text="Clear", font=("Goudy old style", 18, "bold"), bd=1, bg="#4286f5",foreground="White",cursor="hand2",command=clear)
        self.btn_clr.place(x=280, y=100, height=35, width=110)

        def show():
            self.root.destroy()
            import show_table

        self.btn_sow = Button(frem_1, text="Show Table", font=("Goudy old style", 17, "bold"), bd=1, bg="#4286f5",foreground="White", cursor="hand2", command=show)
        self.btn_sow.place(x=280, y=160, height=35, width=110)

        frame_3 = Frame(frame1, bg='#ffffff', bd=2.4, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        frame_3.place(x=680, y=75, height=540, width=500)

        # =============Bill Area================#
        lbl1 = Label(frame_3, text='Bill Area', font=("Goudy old style", 18, "bold"), bg='white', bd=4,
                     relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(frame_3, orient=VERTICAL)
        self.textarea = Text(frame_3, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)
        head = "\n\n\t GLOBAL CAFE SHOP\n" \
               "\t NEAR MAWAL \n\n\t THANK YOU FOR CHOOSING OUR COFFEE\n" \
               "\t WE HOPE TO SEE YOU NEXT TIME\n\n\n" \
               "\tCOFFEE ----- QUANTITY\t ----- PRICE( ₹ )\n"
        self.textarea.insert('insert', head)
        self.textarea.config(state="disabled")

    def fetch_combo(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='Vedant@123', database='sin_up')
            mycursor = con.cursor()
            query = "SELECT billno FROM data3"
            mycursor.execute(query)
            rows = mycursor.fetchall()
            if rows:
                billnum = [row[0] for row in rows]
                self.id_ent['values'] = billnum
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {str(e)}")

    def show_details(self, event):
        selected_bill = self.id_var.get()
        try:
            con = pymysql.connect(host='localhost', user='root', password='Vedant@123', database='sin_up')
            mycursor = con.cursor()
            query = "SELECT * FROM data3 WHERE billno = %s"
            mycursor.execute(query, (selected_bill,))
            row = mycursor.fetchone()
            if row:
                self.id_var.set(row[0])
                self.billno_var.set(row[1])
                self.date_var.set(row[2])
                self.cashname_var.set(row[3])
                self.contact_var.set(row[4])
                self.method_var.set(row[5])
                self.textarea.config(state="normal")
                self.textarea.delete(1.0, END)
                self.textarea.insert(END, row[6])
                self.textarea.config(state="disabled")
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching details: {str(e)}")

root = Tk()
obj= bill_info(root)
root.mainloop()