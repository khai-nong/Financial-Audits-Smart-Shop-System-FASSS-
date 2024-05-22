import pymysql
import sys
sys.path.append('/database/fasss')
import fasss as db

from tkinter import *
from tkinter import ttk, messagebox

#=============== เพิ่มข้อมูลลูกต้า ===============
gui = Tk()
gui.title("FASSS (Financial Accounting Smart Shops System)")
gui.geometry("1152x648")  # ขนาดหน้าต่าง
gui.configure(background='#232429')
my_font = ("Quark-Bold")

def show(): #กดดูรายชื่อลูกค้า
    db = pymysql.connect(host='localhost', db='fasss', user='root', passwd='yamayan0215')
    cursor = db.cursor()
    sqlString = "SELECT * FROM customer"
    cursor.execute(sqlString)
    customer = cursor.fetchall()

    for i, (cst_id, cst_name, cst_ad, cst_tell) in enumerate(customer, start=1):
        listBox.tag_configure('font', font=('Leelawadee', 11))
        listBox.insert("", "end", values=("CT-{:02d}".format(cst_id), cst_name),tags=('font',))
    db.close()

    for col in cols:
        listBox.heading(col, text=col)
        listBox.column('รหัสลูกค้า',anchor=CENTER, width=130)
        listBox.column('ชื่อลูกค้า', anchor=CENTER, width=250)
        listBox.place(x=670, y=120)

def save_cstdata(): #บันทึก
    name_s = str(ct_name.get())
    add_s = str(ct_add.get())
    tell_s = str(ct_tell.get())
    db = pymysql.connect(host='localhost', db='fasss', user='root', passwd='yamayan0215')
    cursor = db.cursor()
    try:
        sql = "INSERT INTO customer(cst_name,cst_ad,cst_tell) VALUES('%s','%s','%s')" % (name_s,add_s,tell_s)
        cursor.execute(sql)
        db.commit()
        messagebox.showinfo("Complete", "บันทึกข้อมูลเสร็จสิ้น กรุณาปิดหน้าต่างเพื่อทำรายการอีกครั้ง")
        update_id.place(x=490, y=200)
        ct_name.delete(0, END)
        ct_add.delete(0, END)
        ct_tell.delete(0, END)
    except:
        messagebox.showerror("Error", "ไม่สามารถเพิ่มข้อมูลได้")
        db.rollback()
        db.close()

def update_data(): #ปุ่มอัพเดทข้อมูล
    for i in listBox.get_children():
        listBox.delete(i)
    db = pymysql.connect(host='localhost', db='fasss', user='root', passwd='yamayan0215')
    cursor = db.cursor()
    sqlString = "SELECT * FROM customer"
    cursor.execute(sqlString)
    customer = cursor.fetchall()

    for i, (cst_id, cst_name, cst_ad, cst_tell) in enumerate(customer, start=1):
        listBox.tag_configure('font', font=('Leelawadee', 11))
        listBox.insert("", "end", values=("CT-{:02d}".format(cst_id), cst_name), tags=('font',))
    db.close()


lbl = Label(gui, text="เพิ่มข้อมูลลูกค้า ",bg="#232429",fg="#737988",font= (my_font,37))
lbl.place(x=20, y=15)

lbl = Label(gui, text="ชื่อ : ",bg="#232429",fg="#737988",font= (my_font,17))
lbl.place(x=120, y=120)
ct_name = Entry(gui,fg="#737988",font= (my_font,17))
ct_name.place(x=170, y=120)

oct_id = Button(gui, text="รายชื่อลูกค้าที่มีอยู่", command=show,fg="#737988",font= (my_font,17))
oct_id.place(x=490, y=120)

update_id = Button(gui, text="อัพเดท", command=update_data,fg="#737988",font= (my_font,17),width=12)

lbl = Label(gui, text="ที่อยู่ : ",bg="#232429",fg="#737988",font= (my_font,17))
lbl.place(x=108, y=180)
ct_add = Entry(gui,fg="#737988",font= (my_font,17))
ct_add.place(x=170, y=180)

lbl = Label(gui, text=" เบอร์โทร : ",bg="#232429",fg="#737988",font= (my_font,17))
lbl.place(x=70, y=240)
ct_tell = Entry(gui,fg="#737988",font= (my_font,17))
ct_tell.place(x=170, y=240)

def on_enter_1(event):
    btn1.config(bg="#1d5ffe", fg="#ffffff")
def on_leave_2(event):
    btn1.config(bg="#ffffff", fg="#000000")

btn1 = Button(gui,text="บันทึกข้อมูล", command=save_cstdata, width=25,font= (my_font,14))
btn1.place(x=172, y=300)
btn1.bind("<Enter>", on_enter_1)
btn1.bind("<Leave>", on_leave_2)

cols = ('รหัสลูกค้า', 'ชื่อลูกค้า')
listBox = ttk.Treeview(gui, columns=cols, show='headings',height=10)

gui.mainloop()