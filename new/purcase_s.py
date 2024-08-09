import os
import re
import tempfile
import time
import random
from datetime import date
from tkinter import *
import qrcode
import pymysql
from PIL import  ImageTk
from tkinter import messagebox, ttk


def random_bill_number(stringLength):
    prefix = 'BB'
    strr = random.randint(10000, 99999)
    return prefix + str(strr)

def valid_phone(phn):
    if re.match(r"[789]\d{9}$", phn):
        return True
    return True

class Purchesh :
    def __init__(self,root):
        self.root = root
        self.root.title('Purchesh')
        self.root.geometry('1360x760+0+0')
        self.root.menuBar_line = Canvas(self.root, width=1330, height=0.9, bg="olive", highlightthickness=0)
        self.root.menuBar_line.place(x=10, y=70)
        self.root.config(bg="white")

        self.bg = ImageTk.PhotoImage(file="images/brand_logo.png")
        self.bg_img = Label(self.root, image=self.bg, bg='white').place(x=0, y=0)

        def home_p() :
            self.root.destroy()
            import dashboard

        home_btn = Button(self.root, text="Home", font=("Goudy old style", 20, "bold"), foreground="orange",
                          bd=0, cursor="hand2", bg="white", activebackground='#fd6a36', activeforeground='white')
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


        def search_bill():
            search_value = self.search_ent.get()
            con = pymysql.connect(host="localhost", user="root", password="Vedant@123", database="sin_up")
            mycursor = con.cursor()
            query = "select * from data3 where cash_name = %s"
            mycursor.execute(query, (search_value,))
            result = mycursor.fetchone()
            con.close()
            if result:
                self.ent_name.delete(0, END)
                self.ent_name.insert(END, result[0])
                self.textarea.config(state="normal")
                self.textarea.delete(1.0, END)
                self.textarea.insert(END, " ".join(map(str, result)))
                self.textarea.config(state="disabled")
            else:
                messagebox.showerror("Error!", "No record found for the given search criteria.")
                self.clr()

        self.search_ent = ttk.Combobox(self.root, font=("Goudy old style", 18, "bold"), cursor='hand2')
        self.search_ent.place(x=670, y=20, height=30, width=250)
        self.fetch_combo()
        self.search_nt = Button(self.root, text='Search', font=("Goudy old style", 23, "bold"), cursor='hand2',
                           foreground='white', bg='orange',bd=1,command=search_bill)
        self.search_nt.place(x=940, y=20, height=30, width=90)

        self.img = ImageTk.PhotoImage(file="images/admin.jpg")
        self.lbl = Label(self.root, image=self.img)
        self.lbl.place(x=1290, y=10, height=50, width=50)
        self.bll1 = Label(self.root, text="Admin", font=("Goudy old style", 30, "bold"), foreground="orange",
                          bg="white")
        self.bll1.place(x=1160, y=10, height=50, width=115)



        # self.img = ImageTk.PhotoImage(file="images/employ.png")
        # self.lbl = Label(self.root, image=self.img)
        # self.lbl.place(x=1290, y=10, height=50, width=50)
        # self.bll1 = Label(self.root, text="Employee", font=("Goudy old style", 30, "bold"), foreground="orange",bg="white")
        # self.bll1.place(x=1120, y=10, height=50, width=170)

        #===================ADD to CART===============

        class CoffeeItem:
            def __init__(self, coffee, price, qty):
                self.product_name = coffee
                self.price = price
                self.qty = qty

        class Cart:
            def __init__(self):
                self.items = []
                self.dictionary = {}

            def add_item(self, item):
                self.items.append(item)

            def remove_item(self):
                self.items.pop()

            def total(self):
                total = 0.0
                for i in self.items:
                    total += float(i.price) * i.qty
                return total

            def isEmpty(self):
                if len(self.items) == 0:
                    return True

            def allCart(self):
                for i in self.items:
                    if (i.product_name in self.dictionary):
                        self.dictionary[i.product_name] += i.qty
                    else:
                        self.dictionary.update({i.product_name:i.qty})

        frame1 = Frame(self.root, bg="light gray", highlightbackground="black", highlightcolor="black",
                       highlightthickness=1)
        frame1.place(x=10, y=80, height=645, width=1330)

        def times():
            current_time = time.strftime("%H:%M:%S")
            clock.config(text=current_time)
            clock.after(200, times)

        clock = Label(frame1, font=("Goudy old style", 20, "bold"), bg="white", foreground="#4286f5")
        clock.place(x=1170, y=20, height=30, width=100)
        times()

        frame_table = Frame(frame1, bg='#ffffff', bd=2.4, highlightbackground="black", highlightcolor="black",
                            highlightthickness=1)
        frame_table.place(x=30, y=60, height=560, width=390)

        self.lbl_name =Label(frame_table,text='Customer Name :',font=("Goudy old style", 18,"bold"),bg='white')
        self.lbl_name.place(x=30,y=35,height=20,width=170)
        self.ent_name = Entry(frame_table, font=("Modern No.20", 13),highlightthickness=1, relief=FLAT)
        self.ent_name.place(x=30,y=65,height=25,width=320)
        self.ent_name.config(highlightbackground="black", highlightcolor="#4286f5")
        self.ent_name.focus()

        self.lbl_num = Label(frame_table,text='Cafe No :',font=("Goudy old style", 18,"bold"),bg='white')
        self.lbl_num.place(x=30,y=110,height=28,width=90)
        self.ent_num = Entry(frame_table, font=("Modern No.20", 13),highlightthickness=1, relief=FLAT)
        self.ent_num.place(x=30,y=145,height=25,width=320)
        self.ent_num.config(highlightbackground="black", highlightcolor="#4286f5")
        self.companyNumber_txt = str(9373636857)
        self.ent_num.insert(0, self.companyNumber_txt)

        self.lbl_coffee = Label(frame_table,text='Coffee Name :',font=("Goudy old style", 18,"bold"),bg='white')
        self.lbl_coffee.place(x=30,y=190,height=28,width=140)
        self.combo1 = ttk.Combobox(frame_table,font=("Modern No.20", 13),state="readonly")
        self.combo1.place(x=30,y=225,height=25,width=320)
        self.fetch_coffee_names()
        self.combo1.bind("<<ComboboxSelected>>", self.fetch_discounts)
        # combo1.option_add("*TCombobox*Listbox.font", text_font)
        # combo1.option_add("*TCombobox*Listbox.selectBackground", "#fd6a3self.6")


        self.lbl_qun = Label(frame_table,text='Quantity :',font=("Goudy old style", 18,"bold"),bg='white')
        self.lbl_qun.place(x=30,y=265,height=28,width=100)
        self.ent_qun = Entry(frame_table,font=("Modern No.20", 13),highlightthickness=1, relief=FLAT)
        self.ent_qun.place(x=30,y=300,height=25,width=320)
        self.ent_qun.config(highlightbackground="black", highlightcolor="#4286f5")
        self.entr_stk = Label(frame_table,font=("Modern No.20", 10),bg='white')
        self.entr_stk.place(x=270, y=270, height=30, width=80)

        self.lbl_dis = Label(frame_table, text='Discount :', font=("Goudy old style", 18, "bold"),bg='white')
        self.lbl_dis.place(x=30, y=335, height=28, width=100)
        self.combo2 = ttk.Combobox(frame_table, font=("Modern No.20", 13), state="readonly")
        self.combo2.place(x=30, y=370, height=25, width=320)
        self.combo2.configure(state="disabled")


        self.lbl_pay = Label(frame_table, text='Payment Method :', font=("Goudy old style", 18, "bold"),bg='white')
        self.lbl_pay.place(x=30, y=410, height=28, width=180)
        self.combo3 = ttk.Combobox(frame_table, font=("Modern No.20", 13), values=["Cash", "Online", "Free"],state="readonly")
        self.combo3.place(x=30, y=445, height=25, width=320)

        self.cart = Cart()

        def add_to_cart():
            self.textarea.configure(state="normal")
            strr = self.textarea.get('1.0', END)
            if strr.find('Total') == -1:
                product_name = self.combo1.get()
                if (product_name != ""):
                    product_qty = self.ent_qun.get()
                    con = pymysql.connect(host="localhost", user="root", password="Vedant@123", database="sin_up")
                    mycursor = con.cursor()
                    find_mrp = "SELECT price, stock FROM data1 WHERE name = %s"
                    mycursor.execute(find_mrp, [product_name])
                    results = mycursor.fetchall()
                    stock = results[0][1]
                    mrp = results[0][0]
                    if product_qty.isdigit() == True:
                        stock = int(stock)
                        if (stock - int(product_qty)) >= 0:
                            sp = mrp * int(product_qty)
                            item = CoffeeItem(product_name, mrp, int(product_qty))
                            self.cart.add_item(item)
                            self.textarea.configure(state="normal")
                            divide = "\t" + ("-" * 70) + "\n"
                            self.textarea.insert('insert', divide)
                            # Display item with quantity and subtotal
                            bill_text = "\t{}  -----  \t{}\t  -----  {}\n".format(product_name, product_qty, sp)
                            self.textarea.insert('insert', bill_text)
                            self.textarea.configure(state="disabled")
                        else:
                            messagebox.showerror("error!", "Out of stock. Check quantity.")
                            self.ent_qun.focus()
                    else:
                        messagebox.showerror("error!", "Invalid quantity.")
                        self.ent_qun.focus()
                else:
                    messagebox.showerror("error!", "Choose a product.")
                    self.combo1.focus()
            else:
                self.textarea.delete('1.0', END)
                new_li = []
                li = strr.split("\n")
                for i in range(len(li)):
                    if len(li[i]) != 0:
                        if li[i].find('Total') == -1:
                            new_li.append(li[i])
                        else:
                            break
                for j in range(len(new_li) - 1):
                    self.textarea.insert('insert', new_li[j])
                    self.textarea.insert('insert', '\n')
                product_name = self.combo1.get()
                if (product_name != ""):
                    product_qty = self.ent_qun.get()
                    con = pymysql.connect(host="localhost", user="root", password="Vedant@123", database="sin_up")
                    mycursor = con.cursor()
                    find_mrp = "SELECT price, stock, id FROM data1 WHERE name =%s"
                    mycursor.execute(find_mrp, [product_name])
                    results = mycursor.fetchall()
                    stock = results[0][1]
                    mrp = results[0][0]
                    if product_qty.isdigit() == True:
                        stock = int(stock)
                        if (stock - int(product_qty)) >= 0:
                            sp = results[0][0] * int(product_qty)
                            item = CoffeeItem(product_name, mrp, int(product_qty))
                            self.cart.add_item(item)
                            self.textarea.configure(state="normal")
                            bill_text = "{}\t\t\t\t{}\t\t\t  {}\n".format(product_name, product_qty, sp)
                            self.textarea.insert('insert', bill_text)
                            self.textarea.configure(state="disabled")
                        else:
                            messagebox.showerror("error!", "Out of stock. Check quantity.")
                            self.ent_qun.focus()
                    else:
                        messagebox.showerror("error!", "Invalid quantity.")
                        self.ent_qun.focus()
                else:
                    messagebox.showerror("error!", "Choose a product.")
                    self.combo1.focus()

        btn_add = Button(frame_table,text='Add to Cart',font=("Goudy old style", 15, "bold"),
                     bg='#4286f5',bd=1,foreground='white',cursor='hand2',command=add_to_cart)
        btn_add.place(x=60,y=485,height=25, width=250)

        def clear():
            self.ent_name.delete(0, END)
            self.combo1.set("")
            self.ent_qun.delete(0,END)
            self.entr_stk.config(text="")
            self.combo2.set("")
            self.combo3.set("")
            self.ent_name.focus()

        btn_clear = Button(frame_table,text='Clear',font=("Goudy old style", 15, "bold"),
                     bg='#4286f5',foreground='white',bd=1,cursor='hand2',command=clear)
        btn_clear.place(x=60,y=520,height=25, width=250)

        #==================BUTTON=====================#

        frame_2 = Frame(frame1,bg='#ffffff', bd=2.4, highlightbackground="black", highlightcolor="black",
                            highlightthickness=1)
        frame_2.place(x=420, y=60, height=230, width=130)

        def total_bill():
            if self.cart.isEmpty():
                messagebox.showerror("error!", "Add a product.")
                self.combo1.focus()
            else:
                self.textarea.configure(state="normal")
                strr = self.textarea.get('1.0', END)
                if strr.find('Total') == -1:
                    self.textarea.configure(state="normal")
                    divider = "\n\n" + "\t" + ("-" * 70) + "\n"
                    self.textarea.insert('insert', divider)
                    total = "\tTotal\t\t₹. {}\n".format(self.cart.total())
                    self.textarea.insert('insert', total)
                    divider2 = "\t" + ("-" * 70) + "\n\n\tCashier : "
                    self.textarea.insert('insert', divider2)
                    self.textarea.configure(state="normal")
                else:
                    return

        btn_ttl1 = Button(frame_2,text='Total',font=("Goudy old style", 15, "bold"),bd=1,bg='#4286f5',foreground='white',cursor='hand2',command=total_bill)
        btn_ttl1.place(x=15,y=20,height=30,width=90)


        self.state = 1
        def gen_bill():

            if self.state == 1:
                strr = self.textarea.get('1.0', END)
                if (self.ent_name.get() == ""):
                    messagebox.showerror("error!", "Please enter a name.")
                    self.ent_name.focus()
                elif (self.ent_num.get() == ""):
                    messagebox.showerror("error!", "Please enter a number.")
                    self.ent_num.focus()
                elif valid_phone(self.ent_num.get()) == False:
                    messagebox.showerror("error!", "Please enter a valid number.")
                    self.ent_num.focus()
                elif (self.cart.isEmpty()):
                    messagebox.showerror("error!", "Cart is empty.")
                elif self.combo3 == "":
                    messagebox.showerror("error!", "Select the Payment Method.")
                    self.combo2.focus()
                else:
                    if strr.find('Total') == -1:
                        self.total_bill()
                        self.gen_bill()
                    else:
                        self.ent_cashname.insert(END, self.ent_name.get())
                        self.ent_cashname.configure(state="disabled")

                        self.ent_cafeno.insert(END, self.ent_num.get())
                        self.ent_cafeno.configure(state="disabled")
                        cust_new_bill = StringVar()
                        cust_new_bill.set(random_bill_number(8))

                        self.ent_billnum.insert(END, cust_new_bill.get())
                        self.ent_billnum.configure(state="disabled")
                        bill_date = StringVar()
                        bill_date.set(str(date.today()))

                        self.ent_billdate.insert(END, bill_date.get())
                        self.ent_billdate.configure(state="disabled")

                        self.textarea.insert(END, self.ent_name.get())
                        s1 = "\t     - RECEIPT # : "
                        self.textarea.insert('insert', s1)
                        self.textarea.insert(END, cust_new_bill.get())
                        s2 = "\n\n\tDATE : "
                        self.textarea.insert('insert', s2)
                        self.textarea.insert(END, bill_date.get())
                        s3 = "\n\t" + ("-" * 70) + "\n\t     FOR COMPLAINTS CALL : "
                        self.textarea.insert('insert', s3)
                        self.textarea.insert(END, self.ent_cafeno.get())
                        payment_method = self.combo3.get()
                        s4 = "\n\tPayment Method: {}\n".format(payment_method)
                        self.textarea.insert('insert', s4)

                        if self.combo3.get() == "Online":
                            # Generate QR code for online payment
                            payment_info = "https://forms.gle/4P6KRzgt2CVMRXSy9"  # Replace this with actual payment information
                            self.generate_qr_code(payment_info)

                            transaction_id = random.randint(100000, 999999)

                            self.textarea.configure(state="normal")
                            self.textarea.insert(END, f"\nTransaction ID: {transaction_id}\n")
                            self.textarea.configure(state="disabled")


                        con = pymysql.connect(host="localhost", user="root", password="Vedant@123", database="sin_up")
                        mycursor = con.cursor()
                        insert = "INSERT INTO data3(billno, date, cash_name, contact, method, bill_details) VALUES(%s,%s,%s,%s,%s,%s)"

                        mycursor.execute(insert, (cust_new_bill.get(), self.ent_billdate.get(), self.ent_cashname.get(), self.ent_cafeno.get(),
                                             self.combo3.get(),self.textarea.get('1.0', END)))
                        con.commit()

                        for item in self.cart.items:
                            update_stock_query = "UPDATE data1 SET stock = stock - %s WHERE name = %s"
                            mycursor.execute(update_stock_query, (item.qty, item.product_name))
                            con.commit()
                        con.close()

                        messagebox.showinfo("error", "Bill Generated Successfully.....!")
                        self.ent_name.configure(state="disabled", background="#ffffff", foreground="#000000")
                        self.ent_num.configure(state="disabled", background="#ffffff", foreground="#000000")
                        self.state = 0
                        self.ent_name.focus()
            else:
                return

        btn_ttl2 = Button(frame_2, text='Generate', font=("Goudy old style", 15, "bold"),bd=1,bg='#4286f5',foreground='white',cursor='hand2',command=gen_bill)
        btn_ttl2.place(x=15, y=70, height=30, width=90)

        def clr():
            self.ent_num.configure(state="normal")
            self.ent_name.configure(state="normal")
            self.ent_qun.configure(state="normal")
            self.ent_name.delete(0, END)
            self.ent_qun.delete(0, END)
            # self.entry3.delete(0, END)
            self.ent_cashname.configure(state="normal")
            self.ent_cafeno.configure(state="normal")
            self.ent_billnum.configure(state="normal")
            self.ent_billdate.configure(state="normal")
            self.textarea.configure(state="normal")
            self.ent_cashname.delete(0, END)
            self.ent_cafeno.delete(0, END)
            self.ent_billnum.delete(0, END)
            self.ent_billdate.delete(0, END)
            self.textarea.delete(1.0, END)
            self.ent_cashname.configure(state="disabled")
            self.ent_cafeno.configure(state="disabled")
            self.ent_billnum.configure(state="disabled")
            self.ent_billdate.configure(state="disabled")
            self.search_ent.set("")

            clear()
            self.textarea.configure(state="normal")
            self.state = 1
            head = "\n\n\t GLOBAL CAFE SHOP\n" \
                   "\t NEAR MAWAL \n\n\t THANK YOU FOR CHOOSING OUR COFFEE\n" \
                   "\t WE HOPE TO SEE YOU NEXT TIME\n\n\n" \
                   "\tCOFFEE ----- QUANTITY\t ----- PRICE( ₹ )\n"
            self.textarea.insert('insert', head)
            self.textarea.configure(state="disabled")
            self.ent_name.focus()

        btn_ttl3 = Button(frame_2, text='Clear', font=("Goudy old style", 15, "bold"),bd=1,bg='#4286f5',foreground='white',cursor='hand2',command=clr)
        btn_ttl3.place(x=15, y=120, height=30, width=90)


        btn_ttl4 = Button(frame_2, text='Print', font=("Goudy old style", 15, "bold"),bd=1, bg='#4286f5', foreground='white', cursor='hand2', command=lambda: self.print_area(self.textarea.get('1.0', END)))
        btn_ttl4.place(x=15, y=170, height=30, width=90)

        frame_3 = Frame(frame1,bg='#ffffff', bd=2.4, highlightbackground="black", highlightcolor="black",
                            highlightthickness=1)
        frame_3.place(x=585, y=60, height=560, width=450)

        #=============Bill Area================#
        lbl1 = Label(frame_3,text='Bill Area',font=("Goudy old style", 18, "bold"),bg='white',bd=4,relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(frame_3,orient=VERTICAL)
        self.textarea=Text(frame_3,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        head = "\n\n\t GLOBAL CAFE SHOP\n" \
               "\t NEAR MAWAL \n\n\t THANK YOU FOR CHOOSING OUR COFFEE\n" \
               "\t WE HOPE TO SEE YOU NEXT TIME\n\n\n" \
               "\tCOFFEE ----- QUANTITY\t ----- PRICE( ₹ )\n"
        self.textarea.insert('insert', head)

        self.textarea.config(state="disabled")

        frame_4 = Frame(frame1, bg='#ffffff', bd=2.4, highlightbackground="black", highlightcolor="black",
                        highlightthickness=1)
        frame_4.place(x=1100, y=60, height=560, width=200)

        self.lbl_bill = Label(frame_4, text='Bill Number :', font=("Goudy old style", 18, "bold"), bg='white')
        self.lbl_bill.place(x=20, y=40, height=28, width=140)
        self.ent_billnum = Entry(frame_4, font=("Modern No.20", 13), highlightthickness=1, relief=FLAT)
        self.ent_billnum.place(x=20, y=80, height=25, width=120)

        self.lbl_billdate = Label(frame_4, text='Bill Date :', font=("Goudy old style", 18, "bold"), bg='white')
        self.lbl_billdate.place(x=20, y=140, height=28, width=100)
        self.ent_billdate = Entry(frame_4, font=("Modern No.20", 13), highlightthickness=1, relief=FLAT)
        self.ent_billdate.place(x=20, y=180, height=25, width=120)

        self.lbl_cafeno = Label(frame_4, text='Cafe No :', font=("Goudy old style", 18, "bold"), bg='white')
        self.lbl_cafeno.place(x=20, y=240, height=28, width=100)
        self.ent_cafeno = Entry(frame_4, font=("Modern No.20", 13), highlightthickness=1, relief=FLAT)
        self.ent_cafeno.place(x=20, y=280, height=25, width=120)

        self.lbl_cashname = Label(frame_4, text='Customer Name :', font=("Goudy old style", 17, "bold"), bg='white')
        self.lbl_cashname.place(x=20, y=330, height=28, width=175)
        self.ent_cashname = Entry(frame_4, font=("Modern No.20", 13), highlightthickness=1, relief=FLAT)
        self.ent_cashname.place(x=20, y=370, height=25, width=120)


    def fetch_coffee_names(self):
        con = pymysql.connect(host="localhost", user="root", password="Vedant@123", database="sin_up")
        mycursor = con.cursor()
        mycursor.execute("SELECT name FROM data1")
        result = mycursor.fetchall()
        coffee_names = [row[0] for row in result]
        self.combo1['values'] = coffee_names
        mycursor.close()
        con.close()

    def fetch_discounts(self, event):
        self.combo2.set('')
        self.combo3.set('')
        selected_coffee = self.combo1.get()
        if selected_coffee:
            con = pymysql.connect(host="localhost", user="root", password="Vedant@123", database="sin_up")
            mycursor = con.cursor()
            mycursor.execute("SELECT discount,stock FROM data1 WHERE name=%s", (selected_coffee,))
            result = mycursor.fetchone()
            if result:
                discount, stock = result
                self.entr_stk.configure(text="In Stock: {}".format(stock))
                self.combo2['values'] = [discount]
                self.combo2.set(discount)
            mycursor.close()
            self.combo2.configure(state="readonly")
            con.close()
            self.insert_new_data_into_database()


    def insert_new_data_into_database(self):
       self.fetch_discounts()

    def generate_qr_code(self,payment_info):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(payment_info)
        qr.make(fit=True)

        qr_img = qr.make_image(fill_color="black", back_color="white")

        # Save or display the QR code image
        qr_img.save("qr1.png")
        qr_img.show()  # Display QR code (optional)

    def print_area(self, txt):

            temp_file = tempfile.mktemp('.txt')
            with open(temp_file, 'w', encoding='utf-8') as f:
                f.write(txt)
            os.startfile(temp_file, 'print')
            messagebox.showinfo("Success!", "Receipt printed successfully.")


    def fetch_combo(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='Vedant@123', database='sin_up')
            mycursor = con.cursor()
            query = "SELECT cash_name FROM data3"  # Fetch unique coffee names
            mycursor.execute(query)
            rows = mycursor.fetchall()
            if rows:
                name = [row[0] for row in rows]  # Extract coffee names from fetched rows
                self.search_ent['values'] = name  # Populate Combobox with unique coffee names
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {str(e)}")

    def clr(self):
        self.search_ent.set("")

root = Tk()
obj = Purchesh(root)
root.mainloop()