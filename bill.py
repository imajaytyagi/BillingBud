from tkinter import *
import math,random,os
from tkinter import messagebox

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#b0e0e6"
        title = Label(self.root, text="Billing Software", bd=10, relief=GROOVE, bg=bg_color, fg="black", font=("arial narrow", 30, "bold"), pady=2).pack(fill=X)

        # Variables
        # Cosmetics
        self.bath_soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.hair_spray=IntVar()
        self.hair_gell=IntVar()
        self.body_lotion=IntVar()
        # Grocery
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.beans=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        # Cold Drinks
        self.sprite=IntVar()
        self.pepsi=IntVar()
        self.thumbs_up=IntVar()
        self.coca_cola=IntVar()
        self.limca=IntVar()
        self.frooti=IntVar()
        # Total Product Price & Tax Variable
        self.cosmetics_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetics_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()
        # Customer
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()


        # Customer Detail Frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("arial narrow",15,"bold"),fg="#003366",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="black", font=("arial narrow",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1, width=15,textvariable=self.c_name,font=("arial narrow",15),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphn_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="black", font=("arial narrow", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone,font=("arial narrow", 15), bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10,pady=5)

        c_bill = Label(F1, text="Bill Number", bg=bg_color, fg="black", font=("arial narrow", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15,textvariable=self.search_bill,font=("arial narrow", 15), bd=7, relief=SUNKEN).grid(row=0, column=5, padx=10, pady=5)

        bill_btn=Button(F1,text="Search",width=10,command=self.find_bill,bd=4,font=("arial narrow", 12, "bold")).grid(row=0,column=6, padx=10, pady=10)

        # Cosmetics Frame
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("arial narrow",15,"bold"),fg="#003366",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)


        c1_lbl = Label(F2,text="Bath Soap",font=("arial narrow",15,"bold"),bg=bg_color,fg="#ff4040").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt = Entry(F2,width=10,textvariable=self.bath_soap,font=("arial narrow",15),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c2_lbl = Label(F2,text="Face Cream",font=("arial narrow",15,"bold"),bg=bg_color,fg="#ff4040").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt = Entry(F2, width=10,textvariable=self.face_cream,font=("arial narrow", 15), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10,pady=10)

        c3_lbl = Label(F2, text="Face Wash", font=("arial narrow", 15, "bold"), bg=bg_color, fg="#ff4040").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt = Entry(F2, width=10,textvariable=self.face_wash,font=("arial narrow", 15), bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_lbl = Label(F2, text="Hair Spray", font=("arial narrow", 15, "bold"), bg=bg_color, fg="#ff4040").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt = Entry(F2, width=10,textvariable=self.hair_spray,font=("arial narrow", 15), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_lbl = Label(F2, text="Hair Gell", font=("arial narrow", 15, "bold"), bg=bg_color, fg="#ff4040").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt = Entry(F2, width=10,textvariable=self.hair_gell,font=("arial narrow", 15), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_lbl = Label(F2, text="Body Lotion", font=("arial narrow", 15,"bold"), bg=bg_color, fg="#ff4040").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt = Entry(F2, width=10,textvariable=self.body_lotion, font=("arial narrow", 15), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        # Grocery Frame
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("arial narrow", 15, "bold"),fg="#003366", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        g1_lbl = Label(F3, text="Rice", font=("arial narrow", 15, "bold"), bg=bg_color, fg="#ff4040").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt = Entry(F3, width=10,textvariable=self.rice,font=("arial narrow", 15), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10,pady=10)

        g2_lbl = Label(F3, text="Food Oil", font=("arial narrow", 15, "bold"), bg=bg_color, fg="#ff4040").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10,textvariable=self.food_oil,font=("arial narrow", 15), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        g3_lbl = Label(F3, text="Beans", font=("arial narrow", 15, "bold"), bg=bg_color, fg="#ff4040").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10,textvariable=self.beans, font=("arial narrow", 15), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        g4_lbl = Label(F3, text="Wheat", font=("arial narrow", 15, "bold"), bg=bg_color, fg="#ff4040").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=10,textvariable=self.wheat,font=("arial narrow", 15), bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

        g5_lbl = Label(F3, text="Sugar", font=("arial narrow", 15, "bold"), bg=bg_color, fg="#ff4040").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10,textvariable=self.sugar,font=("arial narrow", 15), bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)

        g6_lbl = Label(F3, text="Tea", font=("arial narrow", 15, "bold"), bg=bg_color,fg="#ff4040").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10, textvariable=self.tea,font=("arial narrow", 15), bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)

        # Cold Drink Frame
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drinks", font=("arial narrow", 15, "bold"),fg="#003366", bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        cd1_lbl = Label(F4, text="Sprite", font=("arial narrow", 15, "bold"), bg=bg_color, fg="#ff4040").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        cd1_txt = Entry(F4, width=10,textvariable=self.sprite, font=("arial narrow", 15), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10,pady=10)

        cd2_lbl = Label(F4, text="Pepsi", font=("arial narrow", 15, "bold"), bg=bg_color, fg="#ff4040").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        cd2_txt = Entry(F4, width=10,textvariable=self.pepsi, font=("arial narrow", 15), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10,pady=10)

        cd3_lbl = Label(F4, text="Thumbs-Up", font=("arial narrow", 15, "bold"), bg=bg_color, fg="#ff4040").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        cd3_txt = Entry(F4, width=10, textvariable=self.thumbs_up,font=("arial narrow", 15), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10,pady=10)

        cd4_lbl = Label(F4, text="CocaCola", font=("arial narrow", 15, "bold"), bg=bg_color, fg="#ff4040").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        cd4_txt = Entry(F4, width=10, textvariable=self.coca_cola,font=("arial narrow", 15), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10,pady=10)

        cd5_lbl = Label(F4, text="Limca", font=("arial narrow", 15, "bold"), bg=bg_color, fg="#ff4040").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        cd5_txt = Entry(F4, width=10, textvariable=self.limca,font=("arial narrow", 15), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10,pady=10)

        cd6_lbl = Label(F4, text="Frooti", font=("arial narrow", 15, "bold"), bg=bg_color, fg="#ff4040").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        cd6_txt = Entry(F4, width=10, textvariable=self.frooti,font=("arial narrow", 15), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10,pady=10)

        # Bill Area
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=340, height=380)

        bill_title = Label(F5,text="Bill Area",font=("arial narrow",15,"bold"),bd=7,relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F5,orient=VERTICAL)
        self.txtarea = Text(F5,yscrollcommand = scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        # Button Frame
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("arial narrow", 15, "bold"),fg="#003366", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        tp1_lbl = Label(F6,text="Total Cosmetics Price",bg=bg_color,fg="black",font=("arial narrow",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        tp1_txt = Entry(F6,textvariable=self.cosmetics_price,width=18,font=("arial narrow",10),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        tp2_lbl = Label(F6, text="Total Grocery Price", bg=bg_color, fg="black",font=("arial narrow", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        tp2_txt = Entry(F6, width=18, textvariable=self.grocery_price,font=("arial narrow", 10), bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10,pady=1)

        tp3_lbl = Label(F6, text="Total Cold Drink Price", bg=bg_color, fg="black",font=("arial narrow", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        tp3_txt = Entry(F6, width=18,textvariable=self.cold_drink_price, font=("arial narrow", 10), bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10,pady=1)

        t1_lbl = Label(F6, text="Cosmetics Tax", bg=bg_color, fg="black",font=("arial narrow", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        t1_txt = Entry(F6, width=18, textvariable=self.cosmetics_tax,font=("arial narrow", 10), bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10,pady=1)

        t2_lbl = Label(F6, text="Grocery Tax", bg=bg_color, fg="black",font=("arial narrow", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        t2_txt = Entry(F6, width=18, textvariable=self.grocery_tax,font=("arial narrow", 10), bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10,pady=1)

        t3_lbl = Label(F6, text="Cold Drink Tax", bg=bg_color, fg="black",font=("arial narrow", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        t3_txt = Entry(F6, width=18, textvariable=self.cold_drink_tax,font=("arial narrow", 10), bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10,pady=1)


        btn_F = Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)

        total_btn = Button(btn_F,text="Total",command=self.total,bg="cadetblue",fg="white",pady=15,width=12,bd=2,font=("arial narrow",14,"bold")).grid(row=0,column=0,padx=5,pady=5)
        generatebill_btn = Button(btn_F, text="Generate Bill",command=self.bill_area, bg="cadetblue", fg="white", pady=15, width=12, bd=2,font=("arial narrow", 14, "bold")).grid(row=0, column=1, padx=5, pady=5)
        clear_btn = Button(btn_F, text="Clear",command=self.clear_data, bg="cadetblue", fg="white", pady=15, width=12, bd=2,font=("arial narrow", 14, "bold")).grid(row=0, column=2, padx=5, pady=5)
        exit_btn = Button(btn_F, text="Exit", command=self.exit_app,bg="cadetblue", fg="white", pady=15, width=12, bd=2,font=("arial narrow", 14, "bold")).grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

    def total(self):
        self.c_bs_p=self.bath_soap.get() * 40
        self.c_fc_p=self.face_cream.get() * 120
        self.c_fw_p=self.face_wash.get() * 60
        self.c_hs_p=self.hair_spray.get() * 180
        self.c_hg_p=self.hair_gell.get() * 140
        self.c_bl_p=self.body_lotion.get() * 180

        self.total_cosmetic_price= float(
            self.c_bs_p +
            self.c_fc_p +
            self.c_fw_p +
            self.c_hs_p +
            self.c_hg_p +
            self.c_bl_p
        )
        self.cosmetics_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax = round(self.total_cosmetic_price*0.05,2)
        self.cosmetics_tax.set("Rs. "+str(self.c_tax))


        self.g_r_p=self.rice.get() * 180
        self.g_fo_p=self.food_oil.get() * 180
        self.g_b_p=self.beans.get() * 60
        self.g_w_p=self.wheat.get() * 240
        self.g_s_p=self.sugar.get() * 45
        self.g_t_p=self.tea.get() * 150

        self.total_grocery_price= float(
            self.g_r_p +
            self.g_fo_p +
            self.g_b_p +
            self.g_w_p +
            self.g_s_p +
            self.g_t_p
        )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round(self.total_grocery_price * 0.1,2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        self.cd_s_p=self.sprite.get() * 60
        self.cd_p_p=self.pepsi.get() * 60
        self.cd_tu_p=self.thumbs_up.get() * 50
        self.cd_cc_p=self.coca_cola.get() * 40
        self.cd_l_p=self.limca.get() * 40
        self.cd_f_p=self.frooti.get() * 45

        self.total_cold_drinks_price = float(
            self.cd_s_p +
            self.cd_p_p +
            self.cd_tu_p +
            self.cd_cc_p +
            self.cd_l_p +
            self.cd_f_p
        )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drinks_price))
        self.cd_tax=round(self.total_cold_drinks_price * 0.05,2)
        self.cold_drink_tax.set("Rs. "+str(self.cd_tax))


        self.total_bill=float(self.total_cosmetic_price+
                              self.total_grocery_price +
                              self.total_cold_drinks_price +
                              self.c_tax +
                              self.g_tax +
                              self.cd_tax
                              )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome BVICAM Retail")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number : {self.c_phone.get()}")
        self.txtarea.insert(END,"\n=====================================")
        self.txtarea.insert(END, "\n Product\t\tQTY\t\tPrice")
        self.txtarea.insert(END, "\n=====================================")


    def bill_area(self):
        if self.c_name.get() =="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmetics_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No product purchased")
        else:
            self.welcome_bill()

            # Cosmetics
            if self.bath_soap.get() != 0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.bath_soap.get()}\t\t{self.c_bs_p}")
            if self.face_cream.get() != 0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get() != 0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.hair_spray.get() != 0:
                self.txtarea.insert(END,f"\n Hair Spray\t\t{self.hair_spray.get()}\t\t{self.c_hs_p}")
            if self.hair_gell.get() != 0:
                self.txtarea.insert(END,f"\n Hair Gell\t\t{self.hair_gell.get()}\t\t{self.c_hg_p}")
            if self.body_lotion.get() != 0:
                self.txtarea.insert(END,f"\n Body Lotion\t\t{self.body_lotion.get()}\t\t{self.c_bl_p}")

            # Grocery
            if self.rice.get() != 0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get() != 0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_fo_p}")
            if self.beans.get() != 0:
                self.txtarea.insert(END,f"\n Bean\t\t{self.beans.get()}\t\t{self.g_b_p}")
            if self.wheat.get() != 0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get() != 0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_t_p}")
            if self.tea.get() != 0:
                self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")

            # Cold Drinks
            if self.sprite.get() != 0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.cd_s_p}")
            if self.pepsi.get() != 0:
                self.txtarea.insert(END,f"\n Pepsi\t\t{self.pepsi.get()}\t\t{self.cd_p_p}")
            if self.thumbs_up.get() != 0:
                self.txtarea.insert(END,f"\n Thumbs-Up\t\t{self.thumbs_up.get()}\t\t{self.cd_tu_p}")
            if self.coca_cola.get() != 0:
                self.txtarea.insert(END,f"\n CocaCola\t\t{self.coca_cola.get()}\t\t{self.cd_cc_p}")
            if self.limca.get() != 0:
                self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t\t{self.cd_l_p}")
            if self.frooti.get() != 0:
                self.txtarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.cd_f_p}")

            self.txtarea.insert(END, "\n-------------------------------------")
            if self.cosmetics_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Cosmetic Tax\t\t\t{self.cosmetics_tax.get()}")
            if self.grocery_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Cold Drinks Tax\t\t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(END, f"\n Total Bill : \t\t\tRs. {self.total_bill}")
            self.txtarea.insert(END, "\n-------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} has been saved successfully!")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            # Splitting the bill file name and taking only 0 element data not the extension part of it
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
                messagebox.showerror("Error","Invalid Bill Number.")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really ant to clear?")
        if op>0:
            # Variables
            # Cosmetics
            self.bath_soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.hair_spray.set(0)
            self.hair_gell.set(0)
            self.body_lotion.set(0)
            # Grocery
            self.rice.set(0)
            self.food_oil.set(0)
            self.beans.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            # Cold Drinks
            self.sprite.set(0)
            self.pepsi.set(0)
            self.thumbs_up.set(0)
            self.coca_cola.set(0)
            self.limca.set(0)
            self.frooti.set(0)
            # Total Product Price & Tax Variable
            self.cosmetics_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetics_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
            # Customer
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you really ant to exit?")
        if op>0:
            self.root.destroy()
# tkinter object
root = Tk()
# calling Bill_App class
obj = Bill_App(root)
# calling class
root.mainloop()
