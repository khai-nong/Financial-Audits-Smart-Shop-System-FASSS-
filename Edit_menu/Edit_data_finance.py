import pymysql
from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk, messagebox

#=============== แก้ไขข้อมูล(รายรับ) ===============
gui = Tk()
gui.title("FASSS (Financial Accounting Smart Shops System)")
gui.geometry("1152x648")  # ขนาดหน้าต่าง
gui.configure(background='#232429')
my_font = ("Quark-Bold")

def search_data(): #ค้นหาวัน
    enter_btn.place_forget()
    scr_day = cal_1.get_date()
    db = pymysql.connect(host='localhost', db='fasss', user='root', passwd='yamayan0215')
    cursor = db.cursor()
    sqlString = "Select * from finance where day ='%s'" % (scr_day)
    cursor.execute(sqlString)
    finance = cursor.fetchall()

    for i, (day, income) in enumerate(finance, start=1):
        listBox.tag_configure('font', font=('Leelawadee', 13))
        day_format = day.strftime("%d-%m-%Y")
        listBox.insert("", "end", values=(day_format, income),tags=('font',))
        for col in cols:
            listBox.heading(col, text=col)
            listBox.place(x=250, y=160)
            listBox.column('วันที่(ว/ด/ป)', anchor=CENTER,width=300)
            listBox.column('รายได้ในวันนี้', anchor=CENTER,width=300)

        again_btn.place(width=140,x=500, y=85)
        edit_btn.place(width=140,x=922, y=240)

    if finance == ():
        enter_btn.place(x=420, y=85)
        messagebox.showerror("Error", "ไม่มีข้อมูล")
        db.rollback()

def edit_data():
    edit_btn.place_forget()
    lbl_1.place(x=400, y=250)
    lbl_2.place(x=440, y=320)
    in_income.place(x=440, y=360)
    save_btn.place(width=244,x=440, y=410)
    listBox.bind('<Double-Button-1>', GetValue)

def GetValue(event):  #กดรับข้อมูล
    row_day = listBox.selection()[0]
    select = listBox.set(row_day)
    in_income.delete(0, END)
    in_income.insert(0, select['รายได้ในวันนี้'])

def save_data():
    scr_day = cal_1.get_date()
    income_ed = int(in_income.get())
    db = pymysql.connect(host='localhost', db='fasss', user='root', passwd='yamayan0215')
    cursor = db.cursor()
    try:
        sqlString = "Update finance set income =%d where day ='%s'" % (income_ed,scr_day)
        cursor.execute(sqlString)
        db.commit()
        messagebox.showinfo("Complete", "บันทึกข้อมูลเสร็จสิ้น กรุณาปิดหน้าต่างเพื่อทำรายการอีกครั้ง")
        scr_day = cal_1.get_date()
        sqlString = "Select * from finance where day ='%s'" % (scr_day)
        cursor.execute(sqlString)
        finance = cursor.fetchall()

        lbl.place(x=490, y=480)
        for i, (day, income) in enumerate(finance, start=1):
            listBox1.tag_configure('font', font=('Leelawadee', 13))
            day_format = day.strftime("%d-%m-%Y")
            listBox1.insert("", "end", values=(day_format, income),tags=('font',))
            for col in cols:
                listBox1.heading(col, text=col)
                listBox1.place(x=250, y=520)
                listBox1.column('วันที่(ว/ด/ป)', anchor=CENTER,width=300)
                listBox1.column('รายได้ในวันนี้', anchor=CENTER,width=300)
    except:
        messagebox.showerror("Error", "ไม่สามารถเพิ่มข้อมูลได้")

def do_again():
    enter_btn.place(x=420, y=85)
    edit_btn.place(width=140, x=922, y=240)
    for i in listBox.get_children():
        listBox.delete(i)
        listBox.place_forget()
    for i in listBox1.get_children():
        listBox1.delete(i)
        listBox1.place_forget()
    in_income.delete(0, END)
    in_pay_debt.delete(0, END)
    in_owe.delete(0, END)
    edit_btn.place_forget()
    save_btn.place_forget()
    lbl.place_forget()
    lbl_1.place_forget()
    lbl_2.place_forget()
    in_income.place_forget()
    in_pay_debt.place_forget()
    in_owe.place_forget()


lbl = Label(gui, text="แก้ไขข้อมูลการเงิน/รายได้ ",bg="#232429",fg="#737988",font= (my_font,37))
lbl.place(x=30, y=15)

lbl = Label(gui, text="เลือกวันที่ต้องการค้นหา : \n (ด/ว/ป)",bg="#232429",fg="#737988",font= (my_font,16))
lbl.place(x=30, y=90)
cal_1=DateEntry(gui,selectmode='day',fg="#737988",font= (my_font,16))
cal_1.place(x=230, y=90)

in_income = Entry(gui,fg="#737988",font= (my_font,16))
in_pay_debt = Entry(gui,fg="#737988",font= (my_font,16))
in_owe = Entry(gui,fg="#737988",font= (my_font,16))

cols = ('วันที่(ว/ด/ป)', 'รายได้ในวันนี้')
listBox = ttk.Treeview(gui, columns=cols, show='headings', height=1)
listBox1 = ttk.Treeview(gui, columns=cols, show='headings', height=1)

def on_enter(event):
    save_btn.config(bg="#1d5ffe", fg="#ffffff")
def on_leave(event):
    save_btn.config(bg="#ffffff", fg="#000000")

enter_btn = Button(gui,text="ตกลง", command=search_data,font= (my_font,15))
enter_btn.place(x=420, y=85)

edit_btn = Button(gui, text="แก้ไขข้อมูล", command=edit_data,font= (my_font,15))
save_btn = Button(gui, text="บันทึก", command=save_data,font= (my_font,13))
save_btn.bind("<Enter>", on_enter)
save_btn.bind("<Leave>", on_leave)

lbl_1 = Label(gui, text="กรุณากรอกข้อมูลใหม่ \n(สามารถคลิกข้อมูลในตารางเพื่อนำข้อมูลเข้าได้)",bg="#232429",fg="#737988",font= (my_font,16))
lbl_2 = Label(gui, text="รายได้ในวันนี้ : ",bg="#232429",fg="#737988",font= (my_font,16))
lbl = Label(gui, text="ข้อมูลหลังแก้ไข",bg="#232429",fg="#737988",font= (my_font,17))
again_btn = Button(gui,text="ทำรายการอีกครั้ง", command=do_again,font= (my_font,15))

gui.mainloop()