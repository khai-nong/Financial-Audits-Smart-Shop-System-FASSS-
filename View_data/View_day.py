import pymysql
from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk, messagebox

#=============== ดูข้อมูล(รายวัน) ===============
gui = Tk()
gui.title("FASSS (Financial Accounting Smart Shops System)")
gui.geometry("1152x648")  # ขนาดหน้าต่าง
gui.configure(background='#232429')
my_font = ("Quark-Bold")

def search_data():
    enter_btn.place_forget()
    scr_day = cal_1.get_date()
    db = pymysql.connect(host='localhost', db='fasss', user='root', passwd='yamayan0215')
    cursor = db.cursor()
    sqlString = "Select * from finance where day ='%s'" % (scr_day)
    cursor.execute(sqlString)
    finance = cursor.fetchall()
    sql_payowe = "SELECT fcst_date, SUM(fcst_pd) AS total_pay ,SUM(fcst_owe) AS total_owe FROM fin_customer where fcst_date ='%s' GROUP BY fcst_date;" % (scr_day)
    cursor.execute(sql_payowe)
    pay_owe = cursor.fetchall()

    if finance ==() and pay_owe == ():
        enter_btn.place(x=400, y=81)
        messagebox.showerror("Error", "No data")

    elif pay_owe == ():
        for i, (day, income) in enumerate(finance, start=1):
            day_format = day.strftime("%d-%m-%Y")
            listBox.tag_configure('bold_tag', font=('Leelawadee', 14))
            listBox.insert("", "end", values=(day_format, income, "ไม่มีข้อมูล", "ไม่มีข้อมูล", income), tags=('bold_tag',))
        for col in cols:
            listBox.heading(col, text=col)
            listBox.place(x=80, y=170)
            listBox.column('วันที่(ว/ด/ป)', anchor=CENTER, width=200)
            listBox.column('รายได้ในวันนี้', anchor=CENTER)
            listBox.column('ยอดหนี้ที่ลูกค้าชำระ', anchor=CENTER)
            listBox.column('ยอดหนี้ที่ลูกค้าติดหนี้', anchor=CENTER)
            listBox.column('รายได้สุทธิ(รวมยอดหนี้ที่ลูกค้าจ่าย)', anchor=CENTER)
            again_btn.place(x=500, y=81)
            paydebt_btn.place(x=300, y=280)
            owe_btn.place(x=670, y=280)

    elif finance == ():
        for i, (fcst_date, total_pay, total_owe) in enumerate(pay_owe, start=1):
            day_format = fcst_date.strftime("%d-%m-%Y")
            listBox.tag_configure('bold_tag', font=('Leelawadee', 14))
            listBox.insert("", "end", values=(day_format, "ยังไม่ได้เพิ่มข้อมูล", total_pay, total_owe, total_pay),
                               tags=('bold_tag',))
            for col in cols:
                listBox.heading(col, text=col)
                listBox.place(x=80, y=170)
                listBox.column('วันที่(ว/ด/ป)', anchor=CENTER, width=200)
                listBox.column('รายได้ในวันนี้', anchor=CENTER)
                listBox.column('ยอดหนี้ที่ลูกค้าชำระ', anchor=CENTER)
                listBox.column('ยอดหนี้ที่ลูกค้าติดหนี้', anchor=CENTER)
                listBox.column('รายได้สุทธิ(รวมยอดหนี้ที่ลูกค้าจ่าย)', anchor=CENTER)
                again_btn.place(x=500, y=81)
                paydebt_btn.place(x=300, y=280)
                owe_btn.place(x=670, y=280)

    elif finance != ():
        for i, (day, income) in enumerate(finance, start=1):
            fcst_date, total_pay, total_owe = pay_owe[i - 1]
            total_2 = income + total_pay
            day_format = day.strftime("%d-%m-%Y")
            listBox.tag_configure('bold_tag', font=('Leelawadee', 14))
            listBox.insert("", "end", values=(day_format, income, total_pay, total_owe, total_2), tags=('bold_tag',))
        for col in cols:
            listBox.heading(col, text=col)
            listBox.place(x=80, y=170)
            listBox.column('วันที่(ว/ด/ป)',anchor=CENTER,width=200)
            listBox.column('รายได้ในวันนี้', anchor=CENTER)
            listBox.column('ยอดหนี้ที่ลูกค้าชำระ', anchor=CENTER)
            listBox.column('ยอดหนี้ที่ลูกค้าติดหนี้', anchor=CENTER)
            listBox.column('รายได้สุทธิ(รวมยอดหนี้ที่ลูกค้าจ่าย)', anchor=CENTER)
            again_btn.place(x=500, y=81)
            paydebt_btn.place(x=300, y=280)
            owe_btn.place(x=670, y=280)

def do_again():
    for i in listBox.get_children():
        listBox.delete(i)
        listBox.place_forget()
        listBox_pd.place_forget()
        listBox_owe.place_forget()
    for i in listBox_pd.get_children():
        listBox_pd.delete(i)
    for i in listBox_owe.get_children():
        listBox_owe.delete(i)
    lbl_1.place_forget()
    lbl_2.place_forget()
    paydebt_btn.place_forget()
    owe_btn.place_forget()
    enter_btn.place(x=400, y=81)

def paydebt_data(): #รายชื่อคนชำระหนี้
    paydebt_btn.place_forget()
    lbl_1.place(x=222, y=270)
    scr_day = cal_1.get_date()
    db = pymysql.connect(host='localhost', db='fasss', user='root', passwd='yamayan0215')
    cursor = db.cursor()
    sqlString = "Select * from fin_customer where fcst_date ='%s' AND fcst_pd != 0 ORDER BY `fcst_id` ASC" % (scr_day)
    cursor.execute(sqlString)
    view_pay = cursor.fetchall()

    for i, (fcst_NO,fcst_id, fcst_name, fcst_pd,fcst_owe,fcst_date,note) in enumerate(view_pay, start=1):
        listBox_pd.tag_configure('pay_tag', font=('Leelawadee', 11))
        listBox_pd.insert("", "end", values=(fcst_id, fcst_name,fcst_pd,note,),tags=('pay_tag',))
        for col in paydebt_cols:
            listBox_pd.heading(col, text=col)
            listBox_pd.place(x=80, y=320)
            listBox_pd.column('รหัสลูกค้า', anchor=CENTER, width=70)
            listBox_pd.column('ชื่อ', anchor=CENTER, width=150)
            listBox_pd.column('ยอดหนี้ที่ชำระ', anchor=CENTER, width=100)
            listBox_pd.column('หมายเหตุ', anchor=CENTER, width=150)

    if view_pay == ():
        messagebox.showerror("Error", "ไม่มีข้อมูลการชำระหนี้")

def owe_data(): #รายชื่อคนติดหนี้
    owe_btn.place_forget()
    lbl_2.place(x=752, y=270)
    scr_day = cal_1.get_date()
    db = pymysql.connect(host='localhost', db='fasss', user='root', passwd='yamayan0215')
    cursor = db.cursor()
    sqlString = "Select * from fin_customer where fcst_date ='%s' AND fcst_owe != 0 ORDER BY `fcst_id` ASC" % (scr_day)
    cursor.execute(sqlString)
    view_owe = cursor.fetchall()

    for i, (fcst_NO, fcst_id, fcst_name,fcst_pd, fcst_owe, fcst_date, note) in enumerate(view_owe, start=1):
        listBox_owe.tag_configure('owe_tag', font=('Leelawadee', 11))
        listBox_owe.insert("", "end", values=(fcst_id, fcst_name, fcst_owe, note),tags=('owe_tag',))
        for col in owe_cols:
            listBox_owe.heading(col, text=col)
            listBox_owe.place(x=610, y=320)
            listBox_owe.column('รหัสลูกค้า', anchor=CENTER, width=70)
            listBox_owe.column('ชื่อ', anchor=CENTER, width=150)
            listBox_owe.column('ยอดหนี้ที่ติดเพิ่ม', anchor=CENTER, width=100)
            listBox_owe.column('หมายเหตุ', anchor=CENTER, width=150)

    if view_owe == ():
        messagebox.showerror("Error", "ไม่มีข้อมูลการติดหนี้")

lbl = Label(gui, text="ข้อมูลรายได้ประจำวัน : ",bg="#232429",fg="#737988",font= (my_font,37))
lbl.place(x=20, y=15)
lbl = Label(gui, text="เลือกวันที่ต้องการค้นหา : \n (ด/ว/ป)",bg="#232429",fg="#737988",font= (my_font,20))
lbl.place(x=20, y=80)
cal_1=DateEntry(gui,selectmode='day',fg="#737988",font= (my_font,11))
cal_1.place(x=250, y=87)


cols = ('วันที่(ว/ด/ป)', 'รายได้ในวันนี้', 'ยอดหนี้ที่ลูกค้าชำระ', 'ยอดหนี้ที่ลูกค้าติดหนี้','รายได้สุทธิ(รวมยอดหนี้ที่ลูกค้าจ่าย)')
paydebt_cols = ('รหัสลูกค้า', 'ชื่อ', 'ยอดหนี้ที่ชำระ', 'หมายเหตุ')
owe_cols = ('รหัสลูกค้า', 'ชื่อ', 'ยอดหนี้ที่ติดเพิ่ม', 'หมายเหตุ')
listBox = ttk.Treeview(gui,columns=cols, show='headings', height=1)
listBox_pd = ttk.Treeview(gui, columns=paydebt_cols, show='headings', height=7)
listBox_owe = ttk.Treeview(gui, columns=owe_cols, show='headings', height=7)

lbl_1 = Label(gui, text="คนที่มาชำระหนี้ในวันนี้",fg="#ffffff",font= (my_font,20),bg="#232429")
lbl_2 = Label(gui, text="คนที่มาติดหนี้เพิ่มในวันนี้",fg="#ffffff",font= (my_font,20),bg="#232429")
enter_btn = Button(gui,text="Enter", command=search_data,width=7,bg="#737988",fg="#ffffff",font= (my_font,14))
enter_btn.place(x=400, y=81)

again_btn = Button(gui,text="ทำรายการอีกครั้ง", command=do_again,width=13,bg="#737988",fg="#ffffff",font= (my_font,14))
paydebt_btn = Button(gui, text="รายชื่อคนที่ชำระหนี้", command=paydebt_data,width=20,bg="#737988",fg="#ffffff",font= (my_font,14))
owe_btn = Button(gui, text="รายชื่อคนที่ติดหนี้", command=owe_data,width=20,bg="#737988",fg="#ffffff",font= (my_font,14))

gui.mainloop()