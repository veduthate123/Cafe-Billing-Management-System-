import tkinter
from tkinter import *

import pymysql
from PIL import ImageTk
from tkinter import messagebox

class Login :
    def __init__(self,root) :
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1366x765+0+0")
        # self.root.resizable(False,False)
        #=====bg image=====#
        self.bg=ImageTk.PhotoImage(file="images/login.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        # =====Login_frame=====#
        Frame_lo=Frame(self.root,bg="white")
        Frame_lo.place(x=200,y=90,height=570,width=550)

        title=Label(Frame_lo,text="Login Here",bg="white",foreground="dark orange",font=("Impact", 35, "bold"))
        title.place(x=60,y=40,height=50,width=250)

        # sub_title=Label(Frame_lo,text="For Continue Please Login or Create New Account",foreground="dark orange",bg="white",font=("Time New Roman", 13, "italic"))
        # sub_title.place(x=80,y=90,height=30,width=380)

        lbl_1=Label(Frame_lo,text="User Name :",bg="white",font=("Goudy old style", 20))
        lbl_1.place(x=75,y=120,height=40,width=140)
        self.txt_1=Entry(Frame_lo,font=("Modern No.20", 13),highlightthickness=1,relief=FLAT)
        self.txt_1.place(x=80,y=150,height=35,width=380)
        self.txt_1.config(highlightbackground="black", highlightcolor="#4286f5")
        self.txt_1.focus()

        lbl_2 = Label(Frame_lo, text="Password :", bg="white",font=("Goudy old style", 20))
        lbl_2.place(x=75, y=200, height=40, width=120)
        self.txt_2 = Entry(Frame_lo, font=("Modern No.20", 13),show="*", highlightthickness=1,relief=FLAT)
        self.txt_2.place(x=80, y=230, height=35, width=380)
        self.txt_2.config(highlightbackground="black", highlightcolor="#4286f5")

        def password_command():
            if self.txt_2.cget('show') == "*":
                self.txt_2.config(show="")
            else:
                self.txt_2.config(show="*")

        # Check Button
        show_password = Checkbutton(Frame_lo, text="Show password",font=("Time New Roman", 10,"bold","underline"), bg='#ffffff', cursor="hand2",fg='#27221c',command=password_command)
        show_password.place(x=75, y=270,height=20, width=130)

        # =====foget password=====£
        def fog_pass() :
            win = Toplevel()
            win.geometry("450x450+600+180")
            win.title('Forgot Password')
            # win.iconbitmap('images\\aa.ico')
            win.config(bg="orange")
            win.resizable(0, 0)

            Frame_fo = Frame(win, bg="white")
            Frame_fo.place(x=30,y=30,height=390, width=390)


            title = Label(Frame_fo,text="Forget Password",foreground="orange",font=("Impact", 23),bg="white")
            title.place(x=90,y=20,height=30, width=220)

            conpas_l = Label(Frame_fo,text="UserName :",font=("Goudy old style", 16),bg="white")
            conpas_l.place(x=52,y=80,height=25, width=100)
            conpas_txt = Entry(Frame_fo,font=("Modern No.20", 12), highlightthickness=1,relief=FLAT)
            conpas_txt.place(x=55, y=105, height=35, width=280)
            conpas_txt.config(highlightbackground="black", highlightcolor="#4286f5")
            conpas_txt.focus()

            newpas_l = Label(Frame_fo,text="New Password :",font=("Goudy old style", 16),bg="white")
            newpas_l.place(x=55, y=165, height=25, width=130)
            newpas_txt = Entry(Frame_fo, font=("Modern No.20", 12), highlightthickness=1,relief=FLAT)
            newpas_txt.place(x=55, y=190, height=35, width=280)
            newpas_txt.config(highlightbackground="black", highlightcolor="#4286f5")

            cofpas_l = Label(Frame_fo, text="Confirm New Password :", font=("Goudy old style", 16), bg="white")
            cofpas_l.place(x=55, y=250, height=25, width=205)
            cofpas_txt = Entry(Frame_fo, font=("Modern No.20", 12), highlightthickness=1,relief=FLAT)
            cofpas_txt.place(x=55, y=275, height=35, width=280)
            cofpas_txt.config(highlightbackground="black", highlightcolor="#4286f5")

            #===========CONECTIVITY FOR FORGET PASSWORD============#

            def clear() :
                conpas_txt.delete(0, END)
                newpas_txt.delete(0, END)
                cofpas_txt.delete(0, END)

            def uppass() :
                if conpas_txt.get()=="" or newpas_txt.get()=="" or cofpas_txt.get()=="" :
                    messagebox.showerror("error" , "All fields are required...!",parent=win)
                    conpas_txt.focus()
                elif newpas_txt.get() != cofpas_txt.get() :
                    messagebox.showerror("error","New Password and Confirm password does not match...!",parent=win)
                    newpas_txt.focus()
                else :
                    try :

                        con = pymysql.connect(host="localhost", user="root", password="Vedant@123", database="sin_up")
                        mycursor = con.cursor()
                        query = "select * from data where uname=%s"
                        mycursor.execute(query,(conpas_txt.get()))
                        row = mycursor.fetchone()
                        if row==None :
                            messagebox.showerror("error","Incorrect username , username not match...!",parent=win)
                            conpas_txt.focus()
                        else:
                            query="update data set upass=%s where uname=%s"
                            mycursor.execute(query,(newpas_txt.get(),conpas_txt.get()))
                            con.commit()
                            con.close()
                            messagebox.showinfo("success","Password is reset , please login with new password...!",parent=win)
                            clear()
                            self.txt_1.focus()
                            win.destroy()

                    except:
                        messagebox.showerror("error","connection not establish...!",parent=win)



            newpass = Button(Frame_fo,text="Update Password",font=("Goudy old style", 16),bg="#4286f5",bd=1,foreground="white",cursor="hand2",command=uppass)
            newpass.place(x=100,y=330, height=35, width=180)

            win.mainloop()


        forget = Button(Frame_lo,text="Forget Password ?",bd=0,bg="white",font=("Time New Roman", 10,"bold","underline"),cursor="hand2",command=fog_pass)
        forget.place(x=340, y=265, height=25, width=120)

        def clear():
            self.txt_1.delete(0,END)
            self.txt_2.delete(0,END)

        def user_loin():
            username = self.txt_1.get()
            password = self.txt_2.get()
            if username== "" :
                messagebox.showerror("error","Please enter Username...!")
                self.txt_1.focus()
            elif password== "" :
                messagebox.showerror("error", "Please enter Password...!")
                self.txt_2.focus()
            else :
                try:
                    con = pymysql.connect(host="localhost", user="root", password="Vedant@123", database="sin_up")
                    mycursor = con.cursor()
                    query = "SELECT * FROM data WHERE uname=%s and upass=%s"
                    mycursor.execute(query, (username, password))
                    user_row = mycursor.fetchone()
                    if user_row:
                        messagebox.showinfo("Success", "Admin Login Successfully!")
                        self.root.destroy()
                        import admindas
                        con.close()
                    else:
                        messagebox.showerror("Error", "Invalid Username or Password!")
                        self.txt_1.focus()
                        clear()
                        con.close()
                except:
                    messagebox.showerror("error","not connect to database...!")

        logg_btn = Button(Frame_lo, text="Login", font=("Time New Roman", 20, "bold"), bg="#4286f5",bd=1, foreground="white",cursor="hand2",command=user_loin)
        logg_btn.place(x=175, y=330, height=50, width=200)


        #=====Canvas=====#
        line = Canvas(Frame_lo, width=162, height=1.3, bg="black", highlightthickness=0)
        line.place(x=80, y=410)
        label = Label(Frame_lo, text='OR', bg='#ffffff',font=("Time New Roman", 13,"bold"))
        label.place(x=255, y=400)
        line = Canvas(Frame_lo, width=162, height=1.3, bg="black", highlightthickness=0)
        line.place(x=300, y=410)

        # sin_up = Button(Frame_lo, text="Sign Up", font=("Time New Roman", 20, "bold"), bg="blue",foreground="white",textvariable="signup",cursor="hand2")
        # sin_up.place(x=200, y=460, height=50, width=150)

        # fb_im = PhotoImage(file="images/facebook.png")
        # fb_lbl = Label(Frame_lo,image=fb_im)
        # fb_lbl.place(x=120,y=360)

        lbl_3 = Label(Frame_lo,text="Don't have an Account ?",font=("Time New Roman", 10, "bold"),bg="white")
        lbl_3.place(x=125,y=500,height=30, width=170)

        def sign() :
            self.root.destroy()
            import sign_up

        creat_account = Button(Frame_lo,text="Create New One",font=("Time New Roman", 10,"bold","underline","italic"),bg="white",bd=0,foreground="orange",cursor="hand2",command=sign)
        creat_account.place(x=289,y=505,height=20, width=105)


root = Tk()
obj= Login(root)
root.mainloop()

