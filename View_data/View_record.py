import pymysql
from tkinter import *
from tkinter import ttk

#=============== ดูข้อมูลลูกค้า ===============
gui = Tk()
gui.title("FASSS (Financial Accounting Smart Shops System)")
gui.geometry("1152x648")  # ขนาดหน้าต่าง
gui.configure(background='#232429')
my_font = ("Quark-Bold")

db = pymysql.connect(host='localhost', db='fasss', user='root', passwd='yamayan0215')
cursor = db.cursor()
remain = "SELECT fcst_id,fcst_name, SUM(fcst_owe-fcst_pd) FROM fin_customer GROUP BY fcst_id;"
cursor.execute(remain)
remain = cursor.fetchall()

cols = ('รหัสลูกค้า', 'ชื่อลูกค้า','ยอดหนี้คงเหลือ')
listBox = ttk.Treeview(gui, columns=cols, show='headings')

for fcst_id,fcst_name, remain in remain:
    listBox.tag_configure('owe_tag', font=('Leelawadee', 11))
    listBox.insert("", "end", values=(fcst_id, fcst_name,remain),tags=('owe_tag',))
    listBox.column('รหัสลูกค้า',width=120,anchor=CENTER)
    listBox.column('ชื่อลูกค้า',anchor=CENTER)
    listBox.column('ยอดหนี้คงเหลือ',anchor=CENTER)

# ข้อมูลที่ถูกเรียกขึ้นมาแสดงผลบนลิสต์บ๊อค
for col in cols:
        listBox.heading(col, text=col)
        listBox.place(x=50, y=100)

def view_data():
    db = pymysql.connect(host='localhost', db='fasss', user='root', passwd='yamayan0215')
    cursor = db.cursor()
    sqlString = "SELECT * FROM customer"
    cursor.execute(sqlString)
    customer = cursor.fetchall()

    cols = ('รหัสลูกค้า', 'ชื่อลูกค้า','ที่อยู่','เบอร์โทร')
    listBox = ttk.Treeview(gui, columns=cols, show='headings')

    for i, (cst_id, cst_name, cst_ad, cst_tell) in enumerate(customer, start=1):
        listBox.tag_configure('owe_tag', font=('Leelawadee', 11))
        listBox.insert("", "end", values=("CT-{:02d}".format(cst_id), cst_name,cst_ad, cst_tell),tags=('owe_tag',))
    db.close()

    # ข้อมูลที่ถูกเรียกขึ้นมาแสดงผลบนลิสต์บ๊อค
    for col in cols:
        listBox.heading(col, text=col)
        listBox.place(x=50, y=350)
        listBox.column('รหัสลูกค้า', anchor=CENTER, width=100)
        listBox.column('ชื่อลูกค้า', anchor=CENTER, width=350)
        listBox.column('ที่อยู่', anchor=CENTER, width=350)
        listBox.column('เบอร์โทร', anchor=CENTER, width=250)

      
view_btn=Button(gui,text='ดูข้อมูลลูกค้าทั้งหมด',command=view_data,width=20,bg="#737988",fg="#ffffff",font= (my_font,14))
view_btn.place(x=600,y=285)

lbl = Label(gui, text="ข้อมูลรายชื่อลูกค้าและหนี้คงเหลือ ",bg="#232429",fg="#737988",font= (my_font,37))
lbl.place(x=40, y=15)
gui.mainloop()