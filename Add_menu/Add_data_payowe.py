import pymysql
from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk, messagebox

gui = Tk()
gui.title("FASSS (Financial Accounting Smart Shops System)")
gui.geometry("1152x648")  # ขนาดหน้าต่าง
gui.configure(background='#232429')
my_font = ("Quark-Bold")


#=============== เพิ่มข้อมูลลูกต้า(การเงิน) ===============

def show2(): #กดดูรายชื่อลูกค้า
    db = pymysql.connect(host='localhost', db='fasss', user='root', passwd='yamayan0215')
    cursor = db.cursor()
    sqlString = "SELECT * FROM customer"
    cursor.execute(sqlString)
    customer = cursor.fetchall()

    cols = ('รหัสลูกค้า', 'ชื่อลูกค้า')
    listBox = ttk.Treeview(gui, columns=cols, show='headings',height=10)
    lbl = Label(gui, text="สามารถดับเบิ้ลคลิกที่ตารางเพื่อรับข้อมูลได้", bg="#232429", fg="#737988", font=(my_font, 17))
    lbl.place(x=680, y=360)

    for i, (cst_id, cst_name, cst_ad, cst_tell) in enumerate(customer, start=1):
        listBox.tag_configure('font', font=('Leelawadee', 11))
        listBox.insert("", "end", values=("CT-{:02d}".format(cst_id), cst_name), tags=('font',))
    db.close()

    for col in cols:
        listBox.heading(col, text=col)
        listBox.place(x=630, y=110)

    def GetValue(event):  #คลิกรับข้อมูล
        ct_id.delete(0, END)
        ct_name.delete(0, END)
        row_id = listBox.selection()[0]
        select = listBox.set(row_id)
        ct_id.insert(0, select['รหัสลูกค้า'])
        ct_name.insert(0, select['ชื่อลูกค้า'])

    listBox.bind('<Double-Button-1>', GetValue)

def add_fcst2(): #เพิ่มข้อมูล
    id_s = str(ct_id.get())
    name_s = str(ct_name.get())
    pay_s =int(ct_pd.get())
    owe_s =int(ct_owe.get())
    cal_s = str(cal_1.get_date())
    note_s = str(note.get())
    db = pymysql.connect(host='localhost', db='fasss', user='root', passwd='yamayan0215')
    cursor = db.cursor()

    try:
        sql ="INSERT INTO fin_customer(fcst_id,fcst_name,fcst_pd,fcst_owe,fcst_date,note) VALUES('%s','%s',%d,%d,'%s','%s')" % (id_s,name_s,pay_s,owe_s,cal_s,note_s)
        cursor.execute(sql)
        db.commit()
        messagebox.showinfo("Complete" , "บันทึกข้อมูลเสร็จสิ้น กรุณาปิดหน้าต่างเพื่อทำรายการอีกครั้ง")
        cal_1.delete(0, END)
        ct_id.delete(0, END)
        ct_name.delete(0, END)
        ct_pd.delete(0, END)
        ct_owe.delete(0, END)
        note.delete(0, END)

    except:
        messagebox.showerror("Error" ,"ไม่สามารถเพิ่มข้อมูลได้ คุณกรอกข้อมูลไปแล้ว")
        db.rollback()
        db.close()

cal_1 = DateEntry(gui,selectmode='day',font= (my_font,17),width=18)
cal_1.place(x=180, y=120)

lbl = Label(gui, text="เพิ่มข้อมูลการชำระหนี้-ติดหนี้ของลูกค้า",bg="#232429",fg="#737988",font= (my_font,37))
lbl.place(x=20, y=20)

lbl = Label(gui, text="วันที่(ด/ว/ป) : ",bg="#232429",fg="#737988",font= (my_font,17))
lbl.place(x=58, y=120)

lbl = Label(gui, text="รหัสลูกค้า : ",bg="#232429",fg="#737988",font= (my_font,17))
lbl.place(x=78, y=180)
ct_id = Entry(gui,fg="#737988",font= (my_font,17))
ct_id.place(x=180, y=180)

oct_id = Button(gui, text="ดูรายชื่อลูกค้า", command=show2,fg="#737988",font= (my_font,17))
oct_id.place(x=475, y=140)

lbl = Label(gui, text="ชื่อ : ",bg="#232429",fg="#737988",font= (my_font,17))
lbl.place(x=130, y=240)
ct_name = Entry(gui,fg="#737988",font= (my_font,17))
ct_name.place(x=180, y=240)

lbl = Label(gui, text="ชำระหนี้ : ",bg="#232429",fg="#737988",font= (my_font,17))
lbl.place(x=95, y=300)
ct_pd = Entry(gui,fg="#737988",font= (my_font,17))
ct_pd.place(x=180, y=300)

lbl = Label(gui, text=" ติดหนี้เพิ่ม : ",bg="#232429",fg="#737988",font= (my_font,17))
lbl.place(x=73, y=360)
ct_owe = Entry(gui,fg="#737988",font= (my_font,17))
ct_owe.place(x=180, y=360)

lbl = Label(gui, text=" หมายเหตุ : ",bg="#232429",fg="#737988",font= (my_font,17))
lbl.place(x=79, y=420)
note = Entry(gui,fg="#737988",font= (my_font,17))
note.place(x=180, y=420)

def on_enter_1(event):
    btn1.config(bg="#1d5ffe", fg="#ffffff")
def on_leave_2(event):
    btn1.config(bg="#ffffff", fg="#000000")

btn1 = Button(gui,text="เพิ่มข้อมูล", command=add_fcst2,fg="#737988",font= (my_font,17),width=21)
btn1.place(x=181, y=470)
btn1.bind("<Enter>", on_enter_1)
btn1.bind("<Leave>", on_leave_2)

gui.mainloop()
