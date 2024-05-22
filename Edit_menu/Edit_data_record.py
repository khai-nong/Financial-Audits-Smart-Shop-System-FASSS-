import pymysql
from tkinter import *
from tkinter import ttk, messagebox

#=============== แก้ไขข้อมูล(ประวัติ) ===============
gui = Tk()
gui.title("FASSS (Financial Accounting Smart Shops System)")
gui.geometry("1152x648")  # ขนาดหน้าต่าง
gui.configure(background='#232429')
my_font = ("Quark-Bold")

def show():
    window = Tk()
    window.geometry("420x350")
    window.title("รายชื่อลูกค้า")
    db = pymysql.connect(host='localhost', db='fasss', user='root', passwd='yamayan0215')
    cursor = db.cursor()
    sqlString = "SELECT * FROM customer"
    cursor.execute(sqlString)
    customer = cursor.fetchall()

    cols = ('รหัสลูกค้า', 'ชื่อลูกค้า')
    listBox = ttk.Treeview(window, columns=cols, show='headings')

    for i, (cst_id, cst_name, cst_ad, cst_tell) in enumerate(customer, start=1):
        listBox.tag_configure('font', font=('Leelawadee', 11))
        listBox.insert("", "end", values=("CT-{:02d}".format(cst_id), cst_name),tags=('font',))
    db.close()

    for col in cols:
        listBox.heading(col, text=col)
        listBox1.column('รหัสลูกค้า', anchor=CENTER)
        listBox1.column('ชื่อลูกค้า', anchor=CENTER)
        listBox.place(x=7, y=0)
    window.mainloop()

def search_data():
    enter_btn.place_forget()
    scr_id = str(ct_id.get())
    db = pymysql.connect(host='localhost', db='fasss', user='root', passwd='yamayan0215')
    cursor = db.cursor()
    sqlString = "Select * from customer where cst_id ='%s'" % (scr_id)
    cursor.execute(sqlString)
    customer = cursor.fetchall()

    for i, (cst_id, cst_name, cst_ad, cst_tell) in enumerate(customer, start=1):
        listBox.tag_configure('font', font=('Quark-Bold', 13))
        listBox.insert("", "end", values=("CT-{:02d}".format(cst_id), cst_name,cst_ad,cst_tell),tags=('font',))
        for col in cols:
            listBox.heading(col, text=col)
            listBox.place(x=110, y=210)
            listBox.column('รหัสลูกค้า',anchor=CENTER, width=150)
            listBox.column('ชื่อลูกค้า', anchor=CENTER, width=260)
            listBox.column('ที่อยู่', anchor=CENTER,width=300)

        again_btn.place(width=140,x=500, y=147)
        edit_btn.place(width=100,x=920, y=280)

    if scr_id == "":
        enter_btn.place(x=410, y=147)
        messagebox.showwarning("Error", "กรุณากรอกรหัสลูกค้า")
        db.rollback()
    elif customer == ():
        enter_btn.place(x=410, y=147)
        messagebox.showerror("Error", "คุณกรอกรหัสลูกค้าผิด/ไม่มีข้อมูล")
        db.rollback()

def edit_data():
    edit_btn.place_forget()
    lbl.place(x=30, y=150)
    lbl_1.place(x=400, y=280)
    lbl_2.place(x=150, y=350)
    lbl_3.place(x=440, y=350)
    lbl_4.place(x=730, y=350)
    ct_name.place(x=150, y=385)
    ct_add.place(x=440, y=385)
    ct_tell.place(x=730, y=385)
    save_btn.place(width=244,x=440, y=430)
    listBox.bind('<Double-Button-1>', GetValue)

def GetValue(event):  #กดรับข้อมูล
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    ct_name.delete(0, END)
    ct_add.delete(0, END)
    ct_tell.delete(0, END)
    ct_name.insert(0, select['ชื่อลูกค้า'])
    ct_add.insert(0, select['ที่อยู่'])
    ct_tell.insert(0, select['เบอร์โทร'])

def save_data():
    sct_id = ct_id.get()
    name_ed = ct_name.get()
    add_ed = ct_add.get()
    tell_ed = ct_tell.get()
    db = pymysql.connect(host='localhost', db='fasss', user='root', passwd='yamayan0215')
    cursor = db.cursor()
    sqlString = "Select * from customer where cst_id ='%s'" % (sct_id)
    cursor.execute(sqlString)
    customer = cursor.fetchall()
    if sct_id =="" or customer == ():
        messagebox.showwarning("Error", "กรุณากรอกรหัสลูกค้าให้ถูกต้อง")
    elif name_ed == "" or add_ed =="" or tell_ed =="":
        messagebox.showwarning("Error", "กรุณากรอกข้อมูลให้ครบ")
    else:
        try:
            sqlString = "Update customer set cst_name ='%s' , cst_ad='%s', cst_tell='%s' where cst_id ='%s'" % (name_ed, add_ed, tell_ed, sct_id)
            cursor.execute(sqlString)
            db.commit()
            messagebox.showinfo("Complete", "บันทึกข้อมูลเสร็จสิ้น กรุณาปิดหน้าต่างเพื่อทำรายการอีกครั้ง")
            scr_id = str(ct_id.get())
            sqlString = "Select * from customer where cst_id ='%s'" % (scr_id)
            cursor.execute(sqlString)
            customer = cursor.fetchall()

            lbl_5.place(x=495, y=510)
            for i, (cst_id, cst_name, cst_ad, cst_tell) in enumerate(customer, start=1):
                listBox1.tag_configure('font', font=('Quark-Bold', 13))
                listBox1.insert("", "end", values=("CT-{:02d}".format(cst_id), cst_name, cst_ad, cst_tell),tag='font')
                for col in cols:
                    listBox1.heading(col, text=col)
                    listBox1.place(x=110, y=550)
                    listBox1.column('รหัสลูกค้า', anchor=CENTER, width=150)
                    listBox1.column('ชื่อลูกค้า', anchor=CENTER, width=260)
                    listBox1.column('ที่อยู่', anchor=CENTER, width=300)

        except:
            messagebox.showerror("Error", "ไม่สามารถเพิ่มข้อมูลได้")

def do_again():
    enter_btn.place(x=410, y=147)
    edit_btn.place(width=100, x=920, y=280)
    for i in listBox.get_children():
        listBox.delete(i)
        listBox.place_forget()
    for i in listBox1.get_children():
        listBox1.delete(i)
        listBox1.place_forget()
    ct_id.delete(0, END)
    ct_name.delete(0, END)
    ct_add.delete(0, END)
    ct_tell.delete(0, END)
    edit_btn.place_forget()
    save_btn.place_forget()
    lbl_1.place_forget()
    lbl_2.place_forget()
    lbl_3.place_forget()
    lbl_4.place_forget()
    lbl_5.place_forget()
    ct_name.place_forget()
    ct_add.place_forget()
    ct_tell.place_forget()

lbl = Label(gui, text="แก้ไขข้อมูลลูกค้า ",bg="#232429",fg="#737988",font= (my_font,37))
lbl.place(x=30, y=15)
lbl = Label(gui, text="เเสดงรายชื่อลูกค้าทั้งหมด : ",bg="#232429",fg="#737988",font= (my_font,16))
lbl.place(x=30, y=90)
lbl = Label(gui, text="รหัสลูกค้าที่ต้องการค้นหา : CT-0",bg="#232429",fg="#737988",font= (my_font,16))
lbl.place(x=30, y=150)
ct_id = Entry(gui,font= (my_font,16),width=9)
ct_id.place(x=265, y=150)
ct_name = Entry(gui,font= (my_font,16))
ct_add = Entry(gui,font= (my_font,16))
ct_tell = Entry(gui,font= (my_font,16))

cols = ('รหัสลูกค้า', 'ชื่อลูกค้า', 'ที่อยู่', 'เบอร์โทร')
listBox = ttk.Treeview(gui, columns=cols, show='headings', height=1)
listBox1 = ttk.Treeview(gui, columns=cols, show='headings', height=1)

lbl_1 = Label(gui, text="กรุณากรอกข้อมูลใหม่ \n(สามารถคลิกข้อมูลในตารางเพื่อนำข้อมูลเข้าได้)",bg="#232429",fg="#737988",font= (my_font,16))
lbl_2 = Label(gui, text="ชื่อ : ",bg="#232429",fg="#737988",font= (my_font,16))
lbl_3 = Label(gui, text="ที่อยู่ : ",bg="#232429",fg="#737988",font= (my_font,16))
lbl_4 = Label(gui, text="เบอร์โทร : ",bg="#232429",fg="#737988",font= (my_font,16))
lbl_5 = Label(gui, text="ข้อมูลหลังแก้ไข",bg="#232429",fg="#737988",font= (my_font,16))
enter_btn = Button(gui,text="ตกลง", command=search_data,font= (my_font,15))
enter_btn.place(x=410, y=147)
edit_btn = Button(gui, text="แก้ไขข้อมูล", command=edit_data,font= (my_font,14))

def on_enter(event):
    save_btn.config(bg="#1d5ffe", fg="#ffffff")
def on_leave(event):
    save_btn.config(bg="#ffffff", fg="#000000")

save_btn = Button(gui, text="บันทึก", command=save_data,font= (my_font,15))
save_btn.bind("<Enter>", on_enter)
save_btn.bind("<Leave>", on_leave)
view_btn = Button(gui, text="ดูรายชื่อลูกค้า", command=show,fg="#737988",font= (my_font,13),width=15)
view_btn.place(x=230, y=90)
again_btn = Button(gui,text="ทำรายการอีกครั้ง", command=do_again,font= (my_font,16))

gui.mainloop()