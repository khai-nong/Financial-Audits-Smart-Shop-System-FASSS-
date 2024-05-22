import pymysql
from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox

#=============== เพิ่มข้อมูลการเงิน ===============

def show_finance():  #แสดงผล
    cal = cal_1.get_date()
    db = pymysql.connect(host='localhost', db='fasss', user='root', passwd='yamayan0215')
    cursor = db.cursor()
    sqlString = "SELECT fcst_date, SUM(fcst_pd) AS total_pay ,SUM(fcst_owe) AS total_owe FROM fin_customer where fcst_date ='%s' GROUP BY fcst_date;" % (cal)
    cursor.execute(sqlString)
    finance = cursor.fetchall()
    for t, total_pay, total_owe in finance:
        i = int(income.get())
        p = int(total_pay)
        o = int(total_owe)
        total = i + p
        lbl = Label(gui, text="วันที่(ว/ด/ป) : ", bg="#232429", fg="#737988", font=(my_font))
        lbl.place(x=235, y=360)
        day_format = cal.strftime("%d - %m - %Y")
        cal = Label(gui, text=day_format, font=(my_font), fg="#ffffff", bg="#232429")
        cal.place(x=350, y=360)

        lbl = Label(gui, text="รายได้ทั้งหมดที่ได้ในวันนี้ : ", bg="#232429", fg="#737988", font=(my_font))
        lbl.place(x=165, y=400)
        lbl = Label(gui, text=i, bg="#232429", font=(my_font), fg="#ffffff", width=15)
        lbl.place(x=350, y=400)

        lbl = Label(gui, text="จำนวนเงินที่ลูกค้าชำระหนี้ : ", bg="#232429", fg="#737988", font=(my_font))
        lbl.place(x=157, y=440)
        pay_debt = Label(gui, text=p, bg="#232429", font=(my_font, 15), fg="#ffffff", width=15)
        pay_debt.place(x=350, y=440)

        lbl = Label(gui, text="จำนวนเงินที่ลูกค้าติดหนี้เพิ่ม : ", bg="#232429", fg="#737988", font=(my_font))
        lbl.place(x=143, y=480)
        owe = Label(gui, text=o, bg="#232429", font=(my_font), fg="#ffffff", width=15)
        owe.place(x=350, y=480)

        lbl = Label(gui, text="รายได้สุทธิ (คำนวณยอดหนี้ลูกค้า) : ", bg="#232429", fg="#737988", font=(my_font))
        lbl.place(x=102, y=520)
        lbl = Label(gui, text=total, bg="#232429", font=(my_font), fg="#ffffff", width=15)
        lbl.place(x=350, y=520)

        lbl = Label(gui, text="รายได้สุทธิ (ไม่คำนวณยอดหนี้ลูกค้า) : ", bg="#232429", fg="#737988", font=(my_font))
        lbl.place(x=83, y=560)
        lbl = Label(gui, text=i, bg="#232429", font=(my_font), fg="#ffffff", width=15)
        lbl.place(x=350, y=560)

    if finance == ():
        i = int(income.get())
        p = 0
        o = 0
        total = i + p
        lbl = Label(gui, text="วันที่(ว/ด/ป) : ",bg="#232429",fg="#737988",font= (my_font))
        lbl.place(x=235, y=360)
        day_format = cal.strftime("%d - %m - %Y")
        cal = Label(gui,text=day_format ,font= (my_font),fg="#ffffff",bg="#232429")
        cal.place(x=350, y=360)

        lbl = Label(gui, text="รายได้ทั้งหมดที่ได้ในวันนี้ : ",bg="#232429",fg="#737988",font= (my_font))
        lbl.place(x=165, y=400)
        lbl = Label(gui,text=i,bg="#232429",font= (my_font),fg="#ffffff",width=15)
        lbl.place(x=350, y=400)

        lbl = Label(gui, text="จำนวนเงินที่ลูกค้าชำระหนี้ : ",bg="#232429",fg="#737988",font= (my_font))
        lbl.place(x=157, y=440)
        pay_debt = Label(gui,text=p,bg="#232429",font= (my_font,15),fg="#ffffff",width=15)
        pay_debt.place(x=350, y=440)

        lbl = Label(gui, text="จำนวนเงินที่ลูกค้าติดหนี้เพิ่ม : ",bg="#232429",fg="#737988",font= (my_font))
        lbl.place(x=143, y=480)
        owe = Label(gui,text=o,bg="#232429",font= (my_font),fg="#ffffff",width=15)
        owe.place(x=350, y=480)

        lbl = Label(gui, text="รายได้สุทธิ (คำนวณยอดหนี้ลูกค้า) : ",bg="#232429",fg="#737988",font= (my_font))
        lbl.place(x=102, y=520)
        lbl = Label(gui, text=total,bg="#232429",font= (my_font),fg="#ffffff",width=15)
        lbl.place(x=350, y=520)

        lbl = Label(gui, text="รายได้สุทธิ (ไม่คำนวณยอดหนี้ลูกค้า) : ",bg="#232429",fg="#737988",font= (my_font))
        lbl.place(x=83, y=560)
        lbl = Label(gui, text=i,bg="#232429",font= (my_font),fg="#ffffff",width=15)
        lbl.place(x=350, y=560)

    btn2.place(x=580, y=580)

def save_data(): #บันทึก
    cal_s = cal_1.get_date()
    db = pymysql.connect(host='localhost', db='fasss', user='root', passwd='yamayan0215')
    cursor = db.cursor()
    sqlString = "SELECT fcst_date, SUM(fcst_pd) AS total_pay ,SUM(fcst_owe) AS total_owe FROM fin_customer where fcst_date ='%s' GROUP BY fcst_date;" % (cal_s)
    cursor.execute(sqlString)
    finance = cursor.fetchall()
    for t in finance:
        i_s = int(income.get())
        try:
            sql = "INSERT INTO finance(day,income) VALUES('%s',%d)" % (cal_s, i_s)
            cursor.execute(sql)
            db.commit()
            messagebox.showinfo("Complete" , "บันทึกข้อมูลเสร็จสิ้น กรุณาปิดหน้าต่างเพื่อทำรายการอีกครั้ง")
            cal_1.delete(0, END)
            income.delete(0, END)
            cal_1.focus_set()
        except:
            messagebox.showerror("Error" ,"ไม่สามารถเพิ่มข้อมูลได้ คุณกรอกข้อมูลของวันนี้ไปแล้ว")
            db.rollback()
            db.close()
    if finance == ():
        i_s = int(income.get())
        try:
            sql = "INSERT INTO finance(day,income) VALUES('%s',%d)" % (cal_s, i_s)
            cursor.execute(sql)
            db.commit()
            messagebox.showinfo("Complete" , "บันทึกข้อมูลเสร็จสิ้น กรุณาปิดหน้าต่างเพื่อทำรายการอีกครั้ง")
            cal_1.delete(0, END)
            income.delete(0, END)
            cal_1.focus_set()
        except:
            messagebox.showerror("Error" ,"ไม่สามารถเพิ่มข้อมูลได้ คุณกรอกข้อมูลของวันนี้ไปแล้ว")
            db.rollback()
            db.close()

gui = Tk()
gui.title("FASSS (Financial Accounting Smart Shops System)")
gui.geometry("1152x648")  # ขนาดหน้าต่าง
gui.configure(background='#232429')
my_font = ("Quark-Bold")

lbl = Label(gui, text="เพิ่มข้อมูลการเงินประจำวัน",bg="#232429",fg="#737988",font= (my_font,37))
lbl.place(x=30, y=20)

cal_1=DateEntry(gui,selectmode='day',font= (my_font),width=16)
cal_1.place(x=350, y=140)

lbl = Label(gui, text="กรอกข้อมูล ",fg="#737988",font= (my_font),width=20)
lbl.place(x=350, y=95)

lbl = Label(gui, text="วันที่ (ด/ว/ป) : ",bg="#232429",fg="#737988",font= (my_font))
lbl.place(x=227, y=140)


def search_data():
    scr_day = cal_1.get_date()
    db = pymysql.connect(host='localhost', db='fasss', user='root', passwd='yamayan0215')
    cursor = db.cursor()
    sqlString = "SELECT fcst_date, SUM(fcst_pd) AS total_pay ,SUM(fcst_owe) AS total_owe FROM fin_customer where fcst_date ='%s' GROUP BY fcst_date;" % (scr_day)
    cursor.execute(sqlString)
    finance = cursor.fetchall()
    for t,total_pay,total_owe in finance:
        pay_debt = Label(gui,text=total_pay,font=(my_font),bg="#232429",fg="#ffffff",width=20)
        pay_debt.place(x=350, y=220)
        owe = Label(gui, text=total_owe, font=(my_font),bg="#232429",fg="#ffffff",width=20)
        owe.place(x=350, y=260)
    if finance == ():
        pay_debt = Label(gui, text=0, font=(my_font),bg="#232429",fg="#ffffff", width=20)
        pay_debt.place(x=350, y=220)
        owe = Label(gui, text=0, font=(my_font),bg="#232429",fg="#ffffff", width=20)
        owe.place(x=350, y=260)

lbl = Label(gui, text="รายได้ทั้งหมดที่ได้ในวันนี้ : ",bg="#232429",fg="#737988",font= (my_font))
lbl.place(x=165, y=180)
income = Entry(gui,font=(my_font),width=17)
income.place(x=350, y=180)

lbl = Label(gui, text="จำนวนเงินที่ลูกค้าชำระหนี้ : ",bg="#232429",fg="#737988",font= (my_font))
lbl.place(x=157, y=220)


lbl = Label(gui, text="จำนวนเงินที่ลูกค้าติดหนี้เพิ่ม : ",bg="#232429",fg="#737988",font= (my_font))
lbl.place(x=143, y=260)

def on_enter_1(event):
    btn1.config(bg="#1d5ffe", fg="#ffffff")
def on_leave_2(event):
    btn1.config(bg="#ffffff", fg="#000000")

btn1 = Button(gui,text="calculate", command=show_finance,font= (my_font,14),width=19)
btn1.place(x=352, y=305)
btn1.bind("<Enter>", on_enter_1)
btn1.bind("<Leave>", on_leave_2)

def on_enter(event):
    btn2.config(bg="#1d5ffe", fg="#ffffff")
def on_leave(event):
    btn2.config(bg="#ffffff", fg="#000000")

btn2 = Button(gui, text="บันทึกข้อมูล", command=save_data,font= (my_font,14),width=14)
btn2.bind("<Enter>", on_enter)
btn2.bind("<Leave>", on_leave)

enter_btn = Button(gui,text="ตกลง",command=search_data,font= (my_font,13))
enter_btn.place(x=580, y=140)

gui.mainloop()