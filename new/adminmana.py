from tkinter import *
import pymysql
from PIL import ImageTk,Image
from tkinter import messagebox, ttk
import time

class manage_p :
    def __init__(self,root):
        self.root = root
        self.root.title('Manage')
        self.root.geometry("1360x760+0+0")
        self.root.menuBar_line = Canvas(self.root, width=1330, height=0.9, bg="olive", highlightthickness=0)
        self.root.menuBar_line.place(x=10, y=70)
        self.root.config(bg="white")

        self.bg = ImageTk.PhotoImage(file="images/brand_logo.png")
        self.bg_img = Label(self.root, image=self.bg,bg='white').place(x=0, y=0)

        #=========all variables========#
        self.id_var=StringVar()
        self.name_var = StringVar()
        self.type_var = StringVar()
        self.discount_var = StringVar()
        self.stock_var = StringVar()
        self.price_var = StringVar()

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

        frame1 = Frame(self.root, bg="light gray", highlightbackground="black", highlightcolor="black",
                       highlightthickness=1)
        frame1.place(x=10, y=80, height=645, width=1330)

        def times():
            current_time = time.strftime("%H:%M:%S")
            clock.config(text=current_time)
            clock.after(200, times)

        clock = Label(frame1, font=("Goudy old style", 20, "bold"), bg="light gray", foreground="#4286f5")
        clock.place(x=1165, y=20, height=30, width=100)
        times()

        lbl_title = Label(frame1,text='Manage Coffee Details' , font=('Times New Roman', 18,'bold',"underline"),bg='light gray')
        lbl_title.place(x=130,y=50,height=28, width=230)

        self.root.image_path = "images/menu-6.png"
        self.root.img = Image.open(self.root.image_path)
        self.root.img = ImageTk.PhotoImage(file="images/menu-6.png")
        self.root.img_label = Label(frame1, image=self.root.img,bg="light gray")
        self.root.img_label.place(x=30, y=20)

        frem_1 = Frame(frame1, bg='#ffffff', bd=2.4, highlightbackground="black", highlightcolor="black",highlightthickness=1)
        frem_1.place(x=40, y=120, height=510, width=400)

        self.lbl_id = Label(frem_1,text='ID :',font=("Goudy old style", 20, "bold"), bg='white')
        self.lbl_id.place(x=0,y=20,width=45, height=20)
        self.id_ent = ttk.Combobox(frem_1,font=("Modern No.20", 13),state="readonly",textvariable=self.id_var)
        self.id_ent.place(x=50,y=20,height=20,width=150)
        self.id_ent.config(state="normal")
        self.id_ent.bind("<<ComboboxSelected>>", self.show_details)
        self.fetch_combo()
        self.id_ent.focus()

        self.lbl_name = Label(frem_1,text='Coffee Name :',font=("Goudy old style", 20, "bold"), bg='white')
        self.lbl_name.place(x=20,y=60,height=30,width=160)
        self.name_ent = Entry(frem_1, font=("Modern No.20", 13), highlightthickness=1,relief=FLAT,textvariable=self.name_var)
        self.name_ent.place(x=20, y=100, height=30, width=200)
        self.name_ent.config(highlightbackground="black", highlightcolor="#4286f5")

        self.lbl_type = Label(frem_1, text='Type :', font=("Goudy old style", 20, "bold"), bg='white')
        self.lbl_type.place(x=20, y=150, height=30, width=70)
        self.type_ent = Entry(frem_1, font=("Modern No.20", 13), highlightthickness=1, relief=FLAT,textvariable=self.type_var)
        self.type_ent.place(x=20, y=190, height=30, width=200)
        self.type_ent.config(highlightbackground="black", highlightcolor="#4286f5")

        self.lbl_discount = Label(frem_1, text='Discount :', font=("Goudy old style", 20, "bold"), bg='white')
        self.lbl_discount.place(x=20, y=240, height=30, width=115)
        self.discount_ent = Entry(frem_1, font=("Modern No.20", 13), highlightthickness=1, relief=FLAT,textvariable=self.discount_var)
        self.discount_ent.place(x=20, y=280, height=30, width=200)
        self.discount_ent.config(highlightbackground="black", highlightcolor="#4286f5")

        self.lbl_instock = Label(frem_1, text='In stock :', font=("Goudy old style", 20, "bold"), bg='white')
        self.lbl_instock.place(x=20, y=330, height=30, width=105)
        self.instock_ent = Entry(frem_1, font=("Modern No.20", 13), highlightthickness=1, relief=FLAT,textvariable=self.stock_var)
        self.instock_ent.place(x=20, y=370, height=30, width=200)
        self.instock_ent.config(highlightbackground="black", highlightcolor="#4286f5")

        self.lbl_price = Label(frem_1, text='Price :', font=("Goudy old style", 20, "bold"), bg='white')
        self.lbl_price.place(x=20, y=420, height=30, width=70)
        self.price_ent = Entry(frem_1, font=("Modern No.20", 13), highlightthickness=1, relief=FLAT,textvariable=self.price_var)
        self.price_ent.place(x=20, y=460, height=30, width=200)
        self.price_ent.config(highlightbackground="black", highlightcolor="#4286f5")

        def insert() :
            if self.name_ent.get()=="" :
                messagebox.showerror('error','Enter Coffee name , type and price to insert data...!')
                self.name_ent.focus()
            elif self.type_ent.get()=="" :
                messagebox.showerror('error', 'type and price to insert data...!')
                self.type_ent.focus()
            elif self.discount_ent.get() == "" :
                messagebox.showerror('error', 'Enter Discount,stock and price to insert data...!')
                self.discount_ent.focus()
            elif self.instock_ent.get()=="" :
                messagebox.showerror('error', 'Enter stock and price to insert data...!')
                self.instock_ent.focus()
            elif self.price_ent.get()=="" :
                messagebox.showerror('error', 'Enter price to insert data...!')
                self.price_ent.focus()
            else :
                try :
                    con = pymysql.connect(host="localhost", user="root", password="Vedant@123", database="sin_up")
                    mycursor = con.cursor()
                    query = "select * from data1 where name=%s"
                    mycursor.execute(query, (self.name_ent.get()))
                    row = mycursor.fetchone()
                    if row != None:
                        messagebox.showerror("error", "Coffee data already exit...!")
                        self.name_ent.focus()
                    else:
                        query = "insert into data1(name,type,discount,stock,price) values(%s,%s,%s,%s,%s)"
                        mycursor.execute(query,(self.name_var.get(),self.type_var.get(),self.discount_var.get(),self.stock_var.get(),self.price_var.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("success","Data inserted Succesfully...!")
                        clear()
                        self.fetch_data()
                        self.fetch_combo()
                except Exception as e:
                    messagebox.showerror("Error", f"Error updating data: {str(e)}")


        add_btn = Button(frem_1,text='Add',font=("Goudy old style", 20, "bold"),bg='#4286f5',bd=1,foreground='white',cursor='hand2',command=insert)
        add_btn.place(x=280,y=40,height=30, width=100)

        def upd():
            if self.id_var.get() == "":
                messagebox.showerror('Error', 'Select a record to update.')
            else:
                try:
                    con = pymysql.connect(host='localhost', user='root', password='Vedant@123', database='sin_up')
                    mycursor = con.cursor()
                    query = "UPDATE data1 SET name=%s, type=%s, discount=%s, stock=%s, price=%s WHERE id=%s"
                    mycursor.execute(query, (
                    self.name_var.get(), self.type_var.get(), self.discount_var.get(), self.stock_var.get(),
                    self.price_var.get(), self.id_var.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Data updated successfully...!")
                    clear()
                    self.fetch_data()
                    self.fetch_combo()
                except Exception as e:
                    messagebox.showerror("Error", f"Error updating data: {str(e)}")

        update_btn = Button(frem_1,text='Update',font=("Goudy old style", 20, "bold"),bg='#4286f5',bd=1,foreground='white',cursor='hand2',command=upd)
        update_btn.place(x=280,y=100,height=30, width=100)

        def delete():
            if self.name_ent.get() == "":
                messagebox.showerror('error', 'Enter Coffee name , type and price to insert data...!')
                self.name_ent.focus()
            elif self.type_ent.get() == "":
                messagebox.showerror('error', 'type and price to insert data...!')
                self.type_ent.focus()
            elif self.discount_ent.get() == "":
                messagebox.showerror('error', 'Enter Discount,stock and price to insert data...!')
                self.discount_ent.focus()
            elif self.instock_ent.get() == "":
                messagebox.showerror('error', 'Enter stock and price to insert data...!')
                self.instock_ent.focus()
            elif self.price_ent.get() == "":
                messagebox.showerror('error', 'Enter price to insert data...!')
                self.price_ent.focus()
            else:
                con = pymysql.connect(host='localhost', user='root', password='Vedant@123', database='sin_up')
                mycursor = con.cursor()
                query = "delete from data1 where name=%s"
                mycursor.execute(query,self.name_var.get())
                con.commit()
                con.close()
                messagebox.showinfo("success","Data Deleted Successfully.....!")
                clear()
                self.fetch_data()
                self.fetch_combo()

        delete_btn = Button(frem_1, text='Delete', font=("Goudy old style", 20, "bold"), bg='#4286f5',bd=1,foreground='white', cursor='hand2',command=delete)
        delete_btn.place(x=280, y=160, height=30, width=100)

        def clear():
            self.id_var.set("")
            self.name_var.set("")
            self.type_var.set("")
            self.discount_var.set("")
            self.stock_var.set("")
            self.price_var.set("")
            self.id_ent.focus()


        clear_btn = Button(frem_1, text='clear', font=("Goudy old style", 20, "bold"), bg='#4286f5',bd=1,foreground='white', cursor='hand2',command=clear)
        clear_btn.place(x=280, y=220, height=30, width=100)


        frame_table = Frame(frame1, bg='#ffffff', bd=2.4, highlightbackground="black", highlightcolor="black",highlightthickness=1)
        frame_table.place(x=460, y=120, height=510, width=835)

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview.Heading", font=("Goudy old style", 15, "bold"), background="light blue",
                             foreground="black")

        scroll_x = Scrollbar(frame_table, orient=HORIZONTAL)
        scroll_y = Scrollbar(frame_table, orient=VERTICAL)
        self.tbl = ttk.Treeview(frame_table, columns=("id", "coffee name", "type", "discount", "inStock", "price"),cursor='hand2')
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.tbl.xview)
        scroll_y.config(command=self.tbl.yview)
        self.tbl.heading("id", text="ID", anchor=CENTER)
        self.tbl.heading("coffee name", text="Coffee Name", anchor=CENTER)
        self.tbl.heading("type", text="Type", anchor=CENTER)
        self.tbl.heading("discount", text="Discount", anchor=CENTER)
        self.tbl.heading("inStock", text="InStock", anchor=CENTER)
        self.tbl.heading("price", text="Price(₹)", anchor=CENTER)

        self.tbl['show'] = 'headings'

        self.tbl.column("id",width=30,anchor=CENTER)
        self.tbl.column("coffee name", width=220,anchor=CENTER)
        self.tbl.column("type", width=60,anchor=CENTER)
        self.tbl.column("discount", width=60,anchor=CENTER)
        self.tbl.column("inStock", width=60,anchor=CENTER)
        self.tbl.column("price", width=60,anchor=CENTER)
        self.tbl.bind("<ButtonRelease-1>",self.get_cursor)
        self.tbl.pack(fill=BOTH, expand=1)
        self.fetch_data()

        self.tbl.config(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

    def fetch_data(self):
        con = pymysql.connect(host='localhost', user='root', password='Vedant@123', database='sin_up')
        mycursor = con.cursor()
        query = "SELECT * FROM data1"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        if len(rows)!=0:
            self.tbl.delete(*self.tbl.get_children())
            for row in rows:
                self.tbl.insert('',END,values=row)
            con.commit()
        con.close()

    def get_cursor(self,event):
        cursor_row=self.tbl.focus()
        contains=self.tbl.item(cursor_row)
        row=contains['values']
        self.id_var.set(row[0])
        self.name_var.set(row[1])
        self.type_var.set(row[2])
        self.discount_var.set(row[3])
        self.stock_var.set(row[4])
        self.price_var.set(row[5])


    def fetch_combo(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='Vedant@123', database='sin_up')
            mycursor = con.cursor()
            query = "SELECT name FROM data1"
            mycursor.execute(query)
            rows = mycursor.fetchall()
            if rows:
                coffee_names = [row[0] for row in rows]
                self.id_ent['values'] = coffee_names
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {str(e)}")


    def show_details(self, event):
        selected_name = self.id_var.get()
        try:
            con = pymysql.connect(host='localhost', user='root', password='Vedant@123', database='sin_up')
            mycursor = con.cursor()
            query = "SELECT * FROM data1 WHERE name = %s"
            mycursor.execute(query, (selected_name,))
            row = mycursor.fetchone()
            if row:
                self.id_var.set(row[0])
                self.name_var.set(row[1])
                self.type_var.set(row[2])
                self.discount_var.set(row[3])
                self.stock_var.set(row[4])
                self.price_var.set(row[5])
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching details: {str(e)}")


root = Tk()
obj = manage_p(root)
root.mainloop()