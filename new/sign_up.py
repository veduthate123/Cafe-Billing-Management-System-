import tkinter
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import re


class Sign_Up:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up Page")
        self.root.geometry("1366x765+0+0")
        self.bg = ImageTk.PhotoImage(file="images/login.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # =====Login_frame=====#
        Frame_si = Frame(self.root, bg="white")
        Frame_si.place(x=200, y=90, height=570, width=550)

        title = Label(Frame_si, text="Login Here", bg="white", foreground="dark orange", font=("Impact", 35, "bold"))
        title.place(x=60, y=40, height=50, width=250)

        lbl_1 = Label(Frame_si, text="Full Name :", font=("Goudy old style", 20), bg="white")
        lbl_1.place(x=79, y=120, height=30, width=130)
        self.txt_1 = Entry(Frame_si, font=("Modern No.20", 13), highlightthickness=1, relief=FLAT)
        self.txt_1.place(x=80, y=150, height=35, width=380)
        self.txt_1.config(highlightbackground="black", highlightcolor="#4286f5")
        self.txt_1.focus()

        lbl_2 = Label(Frame_si, text="User Name :", font=("Goudy old style", 20), bg="white")
        lbl_2.place(x=79, y=210, height=30, width=130)
        self.txt_2 = Entry(Frame_si, font=("Modern No.20", 13), highlightthickness=1, relief=FLAT)
        self.txt_2.place(x=80, y=240, height=35, width=380)
        self.txt_2.config(highlightbackground="black", highlightcolor="#4286f5")

        lbl_3 = Label(Frame_si, text="Password :", font=("Goudy old style", 20), bg="white")
        lbl_3.place(x=75, y=300, height=30, width=120)
        self.txt_3 = Entry(Frame_si, font=("Modern No.20", 13), show="*", highlightthickness=1, relief=FLAT)
        self.txt_3.place(x=80, y=330, height=35, width=380)
        self.txt_3.config(highlightbackground="black", highlightcolor="#4286f5")

        def show_pass():
            if self.txt_3.cget('show') == "*":
                self.txt_3.config(show="")
            else:
                self.txt_3.config(show="*")

        show_pass = Checkbutton(Frame_si, text="Show password", font=("Time New Roman", 10, "bold", "underline"),
                                bg="white", cursor="hand2", fg='#27221c', command=show_pass)
        show_pass.place(x=335, y=365, height=25, width=130)

        # ========sign_up DATABASE CONNECTIVITY=======#
        def clear():
            self.txt_1.delete(0, END)
            self.txt_2.delete(0, END)
            self.txt_3.delete(0, END)
            check.set(0)

        def is_valid_username(username):
            if not re.search(r'[a-zA-Z0-9_@a-zA-Z]+$', username):
                return False

        def is_valid_password(password):
            if len(password) < 8:
                return False
            if not re.search(r'[A-Z]', password):
                return False
            if not re.search(r'[a-z]', password):
                return False
            if not re.search(r'[0-9]', password):
                return False
            return True

        def up():
            if self.txt_1.get() == "":
                messagebox.showerror("Error", "Enter your name!")
                self.txt_1.focus()
            elif self.txt_2.get() == "":
                messagebox.showerror("Error", "Please enter username!")
                self.txt_2.focus()
            elif not is_valid_username(self.txt_2.get()):
                messagebox.showerror("Error",
                                     "Username can only contain letters, numbers ans special Character")
                self.txt_2.focus()
            elif self.txt_3.get() == "":
                messagebox.showerror("Error", "Please enter password!")
                self.txt_3.focus()
            elif not is_valid_password(self.txt_3.get()):
                messagebox.showerror("Error",
                                     "Password must be at least 8 characters long, include an uppercase letter, a lowercase letter, a number")
                self.txt_3.focus()
            elif check.get() == 0:
                messagebox.showerror("Error", "Please accept Terms and Conditions!")
            else:
                try:
                    con = pymysql.connect(host="localhost", user="root", password="Vedant@123", database="sin_up")
                    mycursor = con.cursor()

                    query = "SELECT * FROM data WHERE uname=%s"
                    mycursor.execute(query, (self.txt_2.get(),))
                    row = mycursor.fetchone()
                    if row is not None:
                        messagebox.showerror("Error", "Username already exists!")
                        self.txt_2.focus()
                    else:
                        query = "INSERT INTO data(name, uname, upass) VALUES(%s, %s, %s)"
                        mycursor.execute(query, (self.txt_1.get(), self.txt_2.get(), self.txt_3.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success", "Registration Successful!")
                        clear()
                        self.root.destroy()
                        import loin
                except Exception as e:
                    messagebox.showerror("Error", f"Database connection error: {str(e)}")

        # ========END=========#
        check = IntVar()
        term_con = Checkbutton(Frame_si, text="I agree to the Terms & Conditions", font=("Time New Roman", 10, "bold"),
                               bg="white", cursor="hand2", fg='#27221c', variable=check)
        term_con.place(x=80, y=400, height=25, width=230)

        si_up = Button(Frame_si, text="Sign Up", font=("Time New Roman", 20, "bold"), bg="#4286f5", bd=1,
                       foreground="white", cursor="hand2", command=up)
        si_up.place(x=175, y=450, height=50, width=200)

        mg_lbl = Label(Frame_si, text="Already have an account?", font=("Time New Roman", 10, "bold"), bg="white")
        mg_lbl.place(x=140, y=515, height=25, width=155)

        def login():
            self.root.destroy()
            import loin

        login = Button(Frame_si, text="Login Here", font=("Time New Roman", 10, "bold", "underline", "italic"),
                       bg="white", bd=0, foreground="orange", cursor="hand2", command=login)
        login.place(x=295, y=515, height=20, width=75)


root = Tk()
obj = Sign_Up(root)
root.mainloop()
