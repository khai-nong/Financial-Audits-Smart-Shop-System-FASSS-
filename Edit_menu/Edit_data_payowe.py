import pymysql
from tkinter import *
from tkinter import ttk, messagebox

#=============== แก้ไขข้อมูล(การจ่ายหนี้ลูกค้า) ===============
gui = Tk()
gui.title("FASSS (Financial Accounting Smart Shops System)")
gui.geometry("1152x648")  # ขนาดหน้าต่าง
gui.configure(background='#232429')
my_font = ("Quark-Bold")

db = pymysql.connect(host='localhost', db='fasss', user='root', passwd='yamayan0215')
cursor = db.cursor()
sqlString = "SELECT * FROM fin_customer ORDER BY `fcst_NO`ASC"
cursor.execute(sqlString)
payowe = cursor.fetchall()

cols = ('ลำดับ','วันที่','รหัสลูกค้า','ชื่อลูกค้า','ติดหนี้เพิ่ม','ชำระหนี้','หมายเหตุ')
listBox = ttk.Treeview(gui, columns=cols, show='headings')

for i, (fcst_NO,fcst_id, fcst_name, fcst_owe,fcst_pd ,fcst_date,note) in enumerate(payowe, start=1):
        listBox.tag_configure('font', font=('Leelawadee', 13))
        day_format = fcst_date.strftime("%d-%m-%Y")
        listBox.insert("", "end", values=(fcst_NO,day_format,fcst_id,fcst_name,fcst_owe,fcst_pd,note),tags=('font',))
db.close()

for col in cols: #ตารางหลัก
        listBox.heading(col, text=col)
        listBox.place(x=30, y=90)
        listBox.column('ลำดับ', anchor=CENTER, width=100)
        listBox.column('วันที่', anchor=CENTER, width=200)
        listBox.column('รหัสลูกค้า', anchor=CENTER, width=130)
        listBox.column('ชื่อลูกค้า', anchor=CENTER, width=200)
        listBox.column('ชำระหนี้', anchor=CENTER, width=130)
        listBox.column('ติดหนี้เพิ่ม', anchor=CENTER, width=130)
        listBox.column('หมายเหตุ', anchor=CENTER, width=200)

def edit_data():
    edit_btn.destroy()
    lbl = Label(gui, text="กรุณากรอกข้อมูลใหม่ \n(สามารถคลิกข้อมูลในตารางเพื่อนำข้อมูลเข้าได้)",bg="#232429",fg="#737988",font= (my_font,16))
    lbl.place(x=420, y=330)
    lbl = Label(gui, text="ลำดับ : ",bg="#232429",fg="#737988",font= (my_font,15))
    lbl.place(x=30, y=395)
    in_no.place(x=30, y=430)
    lbl = Label(gui, text="วันที่ : ",bg="#232429",fg="#737988",font= (my_font,16))
    lbl.place(x=270, y=395)
    in_date.place(x=270, y=430)
    lbl = Label(gui, text="ติดหนี้เพิ่ม : ",bg="#232429",fg="#737988",font= (my_font,16))
    lbl.place(x=500, y=395)
    in_pd.place(x=500, y=430)
    lbl = Label(gui, text="ชำระหนี้ : ",bg="#232429",fg="#737988",font= (my_font,16))
    lbl.place(x=720, y=395)
    in_owe.place(x=720, y=430)
    lbl = Label(gui, text="หมายเหตุ : ",bg="#232429",fg="#737988",font= (my_font,16))
    lbl.place(x=940, y=395)
    in_note.place(x=940, y=430)
    save_btn.place(x=500, y=500)
    again_btn.place(x=940, y=500)
    listBox.bind('<Double-Button-1>', GetValue)

def GetValue(event):  #กดรับข้อมูล
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    in_date.delete(0, END)
    in_no.delete(0, END)
    in_pd.delete(0, END)
    in_owe.delete(0, END)
    in_note.delete(0, END)
    in_no.insert(0,select['ลำดับ'])
    in_date.insert(0, select['วันที่'])
    in_pd.insert(0, select['ชำระหนี้'])
    in_owe.insert(0, select['ติดหนี้เพิ่ม'])
    in_note.insert(0, select['หมายเหตุ'])

def save_data():
    sct_no = int(in_no.get())
    pd_ed = int(in_pd.get())
    owe_ed = int(in_owe.get())
    date_ed = str(in_date.get())
    note_ed = str(in_note.get())
    db = pymysql.connect(host='localhost', db='fasss', user='root', passwd='yamayan0215')
    cursor = db.cursor()
    query = "SELECT * FROM fin_customer WHERE fcst_NO = %s"
    cursor.execute(query, (sct_no,))
    if sct_no =='':
        messagebox.showinfo("Re", "กรุณากรอกลำดับให้ถูกต้อง")
    elif date_ed == '' or pd_ed == '' or owe_ed =='':
        messagebox.showinfo("Re", "กรุณากรอกข้อมูลให้ครบ")
    else:
        try:
            query = "UPDATE fin_customer SET fcst_owe = %s, fcst_pd = %s, fcst_date = %s, note = %s WHERE fcst_NO = %s"
            cursor.execute(query, (owe_ed,pd_ed, date_ed, note_ed, sct_no))
            db.commit()
            messagebox.showinfo("Complete", "บันทึกข้อมูลเสร็จสิ้น กรุณาปิดหน้าต่างเพื่อทำรายการอีกครั้ง")
        except:
            messagebox.showinfo("Error", "ไม่สามารถเพิ่มข้อมูลได้")

def do_again():
    in_date.delete(0, END)
    in_no.delete(0, END)
    in_pd.delete(0, END)
    in_owe.delete(0, END)
    in_note.delete(0, END)

in_no = Entry(gui,fg="#737988",font= (my_font,15),width=16)
in_date = Entry(gui,fg="#737988",font= (my_font,15),width=15)
in_pd = Entry(gui,fg="#737988",font= (my_font,15),width=15)
in_owe = Entry(gui,fg="#737988",font= (my_font,15),width=15)
in_note = Entry(gui,fg="#737988",font= (my_font,15),width=15)

lbl = Label(gui, text="แก้ไขการชำระหนี้ของลูกค้า ",bg="#232429",fg="#737988",font= (my_font,37))
lbl.place(x=30, y=15)
edit_btn = Button(gui, text="แก้ไขข้อมูล", command=edit_data,fg="#737988",font= (my_font,16))
edit_btn.place(x=1030,y=330)

def on_enter_1(event):
    save_btn.config(bg="#1d5ffe", fg="#ffffff")
def on_leave_2(event):
    save_btn.config(bg="#ffffff", fg="#000000")
save_btn = Button(gui, text="บันทึก", command=save_data,width=18,fg="#737988",font= (my_font,15))
save_btn.bind("<Enter>", on_enter_1)
save_btn.bind("<Leave>", on_leave_2)
again_btn = Button(gui,text="ทำรายการอีกครั้ง", command=do_again,width=18,fg="#737988",font= (my_font,15))

gui.mainloop()