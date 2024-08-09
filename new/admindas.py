from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time

class dashboard :
    def __init__(self,root):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("1360x760+0+0")
        self.root.resizable(False, False)

        self.root.menuBar_line = Canvas(self.root, width=1500, height=1.5, bg="#e6e6e6", highlightthickness=1)
        self.root.menuBar_line.place(x=0, y=60)
        self.root.config(bg="white")

        self.bg = ImageTk.PhotoImage(file="images/brand_logo.png")
        self.bg_img = Label(self.root, image=self.bg).place(x=0, y=0)

        #=======home_img=======#
        self.root.image_path = "images/home_bg.jpg"  # Replace with the actual path to your image file
        self.root.img = Image.open(self.root.image_path)
        self.root.img = ImageTk.PhotoImage(self.root.img)
        self.root.img_label = Label(self.root, image=self.root.img)
        self.root.img_label.place(x=0, y=60)
        self.root.labl = Label(self.root, text="Welcome to \n\tCafe Valentine", font=("Times New Roman", 30, "bold"),
                               bg="black", fg="olive")
        self.root.labl.place(x=50, y=90)

        self.root.labl.config(relief="flat", bd=0, padx=4, pady=4)
        self.root.labl.bind("<Enter>", self.on_enter)
        self.root.labl.bind("<Leave>", self.on_leave)


        self.root.lbl = Label(text="Trending", font=("Times New Roman", 20, "bold","underline"),
                               bg="black", fg="light green")
        self.root.lbl.place(x=100,y=230)

        self.root.coffeeImage = Image.open('images/menu-6.png')
        self.root.photo = ImageTk.PhotoImage(self.root.coffeeImage)
        self.root.coffeeImg = Label(self.root, image=self.root.photo, bg='black')
        self.root.coffeeImg.image = self.root.photo
        self.root.coffeeImg.place(x=40, y=290)
        #
        self.root.heading_1 = Label(self.root,text='Cappuccino',font=("Times New Roman", 14, "bold"),bg='black',foreground='white')
        self.root.heading_1.place(x=30,y=380)

        self.root.coffeeImage1 = Image.open('images/menu-5.png')
        self.root.photo = ImageTk.PhotoImage(self.root.coffeeImage1)
        self.root.coffeeImg = Label(self.root,image=self.root.photo,bg="black")
        self.root.coffeeImg.image = self.root.photo
        self.root.coffeeImg.place(x=190,y=290)
        #
        self.root.heading_2 = Label(self.root, text='Mocha', font=("Times New Roman", 14, "bold"), bg='black',
                                    foreground='white')
        self.root.heading_2.place(x=200, y=380)

        self.root.coffeeImage2 = Image.open('images/menu-4.png')
        self.root.photo = ImageTk.PhotoImage(self.root.coffeeImage2)
        self.root.coffeeImg = Label(self.root,image=self.root.photo,bg='black')
        self.root.coffeeImg.image = self.root.photo
        self.root.coffeeImg.place(x=40,y=450)

        self.root.heading_3 = Label(self.root,text='Piccolo Latte',font=("Times New Roman", 14, "bold"),bg='black',foreground='white')
        self.root.heading_3.place(x=30,y=540)

        # self.root.coffeeImage3 = Image.open('images/menu-3.png')
        # self.root.photo = ImageTk.PhotoImage(self.root.coffeeImage3)
        # self.root.coffeeImg = Label(self.root,image=self.root.photo,bg='black')
        # self.root.coffeeImg.image = self.root.photo
        # self.root.coffeeImg.place(x=50,y=250)
        #
        # self.root.heading_4 = Label(self.root,text="Cafe' Latte",font=("Times New Roman", 14, "bold"),bg='black',foreground='white')
        # self.root.heading_4.place(x=45,y=340)
        #
        # self.root.coffeeImage4 = Image.open('images/menu-2.png')
        # self.root.photo = ImageTk.PhotoImage(self.root.coffeeImage4)
        # self.root.coffeeImg = Label(self.root,image=self.root.photo,bg='black')
        # self.root.coffeeImg.image = self.root.photo
        # self.root.coffeeImg.place(x=1190,y=420)
        #
        # self.root.heading_5 = Label(self.root,text='Espresso',font=("Times New Roman", 14, "bold"),bg='black',foreground='white')
        # self.root.heading_5.place(x=1195,y=510)

        home_btn = Button(self.root, text="Home", font=("Goudy old style", 20, "bold"), foreground="orange",
                          bd=0, cursor="hand2", bg="white", activebackground='#fd6a36', activeforeground='white')
        home_btn.place(x=80, y=20, height=30, width=80)

        def mang():
            self.root.destroy()
            import adminmana

        manage_btn = Button(self.root, text="Manage", font=("Goudy old style", 20, "bold"), foreground="orange"
                            , bd=0, bg="white", cursor="hand2", activebackground='#fd6a36', activeforeground='white',command=mang)
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

        def times():
            current_time = time.strftime("%H:%M:%S")
            clock.config(text=current_time)
            clock.after(200, times)

        clock = Label(self.root, font=("Goudy old style", 20, "bold"), bg="black", foreground="#4286f5")
        clock.place(x=1165, y=80, height=30, width=100)
        times()


        self.img = ImageTk.PhotoImage(file="images/admin.jpg")
        self.lbl = Label(self.root,image=self.img)
        self.lbl.place(x=1290,y=10,height=50,width=50)
        self.bll1 = Label(self.root,text="Admin",font=("Goudy old style", 30,"bold"),foreground="orange",bg="white")
        self.bll1.place(x=1160,y=10,height=50,width=115)

    def on_enter(self, event):
        self.root.labl.config(fg="#558B2F")

    def on_leave(self, event):
        self.root.labl.config(fg="olive")

root = Tk()
obj = dashboard(root)
root.mainloop()