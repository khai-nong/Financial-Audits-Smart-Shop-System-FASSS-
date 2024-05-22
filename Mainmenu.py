from tkinter import *

gui = Tk()
gui.title("FASSS (Financial Accounting Smart Shops System)")
gui.geometry("1152x648")  # ขนาดหน้าต่าง
icon_image = PhotoImage(file="pic/logo.png")
gui.wm_iconphoto(True, icon_image)
gui.configure(background='#232429')
my_font = ("Quark-Bold")


# เม้าส์ชี้เปลี่ยนสี
def on_enter(event):
    btn_vd.config(bg="#1d5ffe", fg="#ffffff")

def on_leave(event):
    btn_vd.config(bg="#ffffff", fg="#000000")

def on_enter_1(event):
    btn_vc.config(bg="#1d5ffe", fg="#ffffff")

def on_leave_2(event):
    btn_vc.config(bg="#ffffff", fg="#000000")

def on_enter_3(event):
    btn_ad.config(bg="#1d5ffe", fg="#ffffff")

def on_leave_4(event):
    btn_ad.config(bg="#ffffff", fg="#000000")

def on_enter_5(event):
    btn_ed.config(bg="#1d5ffe", fg="#ffffff")

def on_leave_6(event):
    btn_ed.config(bg="#ffffff", fg="#000000")

def go_finnace():  # เมนูรองหน้าดูข้อมูลการเงิน
    btn_vd.place_forget()
    btn_vc.place_forget()
    btn_ad.place_forget()
    btn_ed.place_forget()

    def on_enter(event):
        vi_day.config(bg="#1d5ffe", fg="#ffffff")

    def on_leave(event):
        vi_day.config(bg="#ffffff", fg="#000000")

    def on_enter_1(event):
        vi_month.config(bg="#1d5ffe", fg="#ffffff")

    def on_leave_2(event):
        vi_month.config(bg="#ffffff", fg="#000000")

    def on_enter_3(event):
        vi_year.config(bg="#1d5ffe", fg="#ffffff")

    def on_leave_4(event):
        vi_year.config(bg="#ffffff", fg="#000000")

    def on_enter_5(event):
        btn_main.config(bg="#1d5ffe", fg="#ffffff")

    def on_leave_6(event):
        btn_main.config(bg="#ffffff", fg="#000000")

    vi_day.place(x=410, y=210)
    vi_day.bind("<Enter>", on_enter)
    vi_day.bind("<Leave>", on_leave)

    vi_month.place(x=410, y=320)
    vi_month.bind("<Enter>", on_enter_1)
    vi_month.bind("<Leave>", on_leave_2)

    vi_year.place(x=410, y=430)
    vi_year.bind("<Enter>", on_enter_3)
    vi_year.bind("<Leave>", on_leave_4)

    btn_main.place(x=410, y=540)
    btn_main.bind("<Enter>", on_enter_5)
    btn_main.bind("<Leave>", on_leave_6)

def go_edit():  # เมนูรองหน้าแก้ไข
    btn_vd.place_forget()
    btn_vc.place_forget()
    btn_ad.place_forget()
    btn_ed.place_forget()

    def on_enter(event):
        ed_fin.config(bg="#1d5ffe", fg="#ffffff")

    def on_leave(event):
        ed_fin.config(bg="#ffffff", fg="#000000")

    def on_enter_1(event):
        ed_po.config(bg="#1d5ffe", fg="#ffffff")

    def on_leave_2(event):
        ed_po.config(bg="#ffffff", fg="#000000")

    def on_enter_3(event):
        ed_record.config(bg="#1d5ffe", fg="#ffffff")

    def on_leave_4(event):
        ed_record.config(bg="#ffffff", fg="#000000")

    def on_enter_5(event):
        btn_main.config(bg="#1d5ffe", fg="#ffffff")

    def on_leave_6(event):
        btn_main.config(bg="#ffffff", fg="#000000")

    ed_fin.place(x=410, y=210)
    ed_fin.bind("<Enter>", on_enter)
    ed_fin.bind("<Leave>", on_leave)

    ed_po.place(x=410, y=320)
    ed_po.bind("<Enter>", on_enter_1)
    ed_po.bind("<Leave>", on_leave_2)

    ed_record.place(x=410, y=430)
    ed_record.bind("<Enter>", on_enter_3)
    ed_record.bind("<Leave>", on_leave_4)

    btn_main.place(x=410, y=540)
    btn_main.bind("<Enter>", on_enter_5)
    btn_main.bind("<Leave>", on_leave_6)

def go_add():  # เมนูรองหน้าเพิ่มข้อมูล
    btn_vd.place_forget()
    btn_vc.place_forget()
    btn_ad.place_forget()
    btn_ed.place_forget()

    def on_enter(event):
        ad_fin.config(bg="#1d5ffe", fg="#ffffff")

    def on_leave(event):
        ad_fin.config(bg="#ffffff", fg="#000000")

    def on_enter_1(event):
        ad_po.config(bg="#1d5ffe", fg="#ffffff")

    def on_leave_2(event):
        ad_po.config(bg="#ffffff", fg="#000000")

    def on_enter_3(event):
        ad_record.config(bg="#1d5ffe", fg="#ffffff")

    def on_leave_4(event):
        ad_record.config(bg="#ffffff", fg="#000000")

    def on_enter_5(event):
        btn_main.config(bg="#1d5ffe", fg="#ffffff")

    def on_leave_6(event):
        btn_main.config(bg="#ffffff", fg="#000000")

    ad_fin.place(x=410, y=210)
    ad_fin.bind("<Enter>", on_enter)
    ad_fin.bind("<Leave>", on_leave)

    ad_po.place(x=410, y=320)
    ad_po.bind("<Enter>", on_enter_1)
    ad_po.bind("<Leave>", on_leave_2)

    ad_record.place(x=410, y=430)
    ad_record.bind("<Enter>", on_enter_3)
    ad_record.bind("<Leave>", on_leave_4)

    btn_main.place(x=410, y=540)
    btn_main.bind("<Enter>", on_enter_5)
    btn_main.bind("<Leave>", on_leave_6)

def back_main():  # กลับหน้าหลัก
    vi_day.place_forget()
    vi_month.place_forget()
    vi_year.place_forget()
    btn_main.place_forget()
    ed_fin.place_forget()
    ed_po.place_forget()
    ed_record.place_forget()
    ad_fin.place_forget()
    ad_po.place_forget()
    ad_record.place_forget()

    def on_enter(event):
        btn_vd.config(bg="#1d5ffe", fg="#ffffff")

    def on_leave(event):
        btn_vd.config(bg="#ffffff", fg="#000000")

    def on_enter_1(event):
        btn_vc.config(bg="#1d5ffe", fg="#ffffff")

    def on_leave_2(event):
        btn_vc.config(bg="#ffffff", fg="#000000")

    def on_enter_3(event):
        btn_ad.config(bg="#1d5ffe", fg="#ffffff")

    def on_leave_4(event):
        btn_ad.config(bg="#ffffff", fg="#000000")

    def on_enter_5(event):
        btn_ed.config(bg="#1d5ffe", fg="#ffffff")

    def on_leave_6(event):
        btn_ed.config(bg="#ffffff", fg="#000000")

    btn_vd.place(x=440, y=210)
    btn_vd.bind("<Enter>", on_enter)
    btn_vd.bind("<Leave>", on_leave)

    btn_vc.place(x=440, y=320)
    btn_vc.bind("<Enter>", on_enter_1)
    btn_vc.bind("<Leave>", on_leave_2)

    btn_ad.place(x=440, y=430)
    btn_ad.bind("<Enter>", on_enter_3)
    btn_ad.bind("<Leave>", on_leave_4)

    btn_ed.place(x=440, y=540)
    btn_ed.bind("<Enter>", on_enter_5)
    btn_ed.bind("<Leave>", on_leave_6)


# =======================================แสดงผล====================================

def view_day():
    from View_data import View_day
def view_month():
    from View_data import View_month
def view_year():
    from View_data import View_Year
def view_record():
    from View_data import View_record

def add_finannce():
    from Add_menu import Add_data_finance
def add_payowe():
    from Add_menu import Add_data_payowe
def add_record():
    from Add_menu import Add_data_Customer

def edit_finannce():
    from Edit_menu import Edit_data_finance
def edit_payowe():
    from Edit_menu import Edit_data_payowe
def edit_record():
    from Edit_menu import Edit_data_record
# =========================ชื่อโปรแกรม================
name = Label(gui, text="FASSS", bg="#232429", fg="#737988", font=(my_font, 55), )
name.place(x=460, y=40)
name_1 = Label(gui, text="Financial Accounting Smart Shops System", bg="#232429", fg="#737988", font=(my_font, 35), )
name_1.place(x=190, y=120)

# ==================================ปุ่มเมนูหลัก====================================
btn_vd = Button(gui, text="ดูข้อมูลการเงิน", font=(my_font, 20), width=16, command=go_finnace)
btn_vd.place(x=440, y=210)
btn_vd.bind("<Enter>", on_enter)
btn_vd.bind("<Leave>", on_leave)

btn_vc = Button(gui, text="ดูข้อมูลลูกค้า", font=(my_font, 20), width=16,command=view_record)
btn_vc.place(x=440, y=320)
btn_vc.bind("<Enter>", on_enter_1)
btn_vc.bind("<Leave>", on_leave_2)

btn_ad = Button(gui, text="เพิ่มข้อมูล", font=(my_font, 20), width=16, command=go_add)
btn_ad.place(x=440, y=430)
btn_ad.bind("<Enter>", on_enter_3)
btn_ad.bind("<Leave>", on_leave_4)

btn_ed = Button(gui, text="แก้ไขข้อมูล", font=(my_font, 20), width=16, command=go_edit)
btn_ed.place(x=440, y=540)
btn_ed.bind("<Enter>", on_enter_5)
btn_ed.bind("<Leave>", on_leave_6)
# ==============================================================================

# ==================================ปุ่มเมนูรอง====================================
vi_day = Button(gui, text="ข้อมูลรายวัน", font=(my_font, 20), width=20,command=view_day)
vi_month = Button(gui, text="ข้อมูลรายเดือน", font=(my_font, 20), width=20,command=view_month)
vi_year = Button(gui, text="ข้อมูลรายปี", font=(my_font, 20), width=20,command=view_year)

ed_fin = Button(gui, text="การเงิน/รายได้", font=(my_font, 20), width=20,command=edit_finannce)
ed_po = Button(gui, text="การชำระหนี้/ติดหนี้", font=(my_font, 20), width=20,command=edit_payowe)
ed_record = Button(gui, text="ข้อมูลประวัติลูกค้า", font=(my_font, 20), width=20,command=edit_record)

ad_fin = Button(gui, text="การเงิน/รายได้", font=(my_font, 20), width=20,command=add_finannce)
ad_po = Button(gui, text="การชำระหนี้/ติดหนี้", font=(my_font, 20), width=20,command=add_payowe)
ad_record = Button(gui, text="ข้อมูลประวัติลูกค้า", font=(my_font, 20), width=20,command=add_record)

btn_main = Button(gui, text="กลับหน้าหลัก", font=(my_font, 20), width=20, command=back_main)
# =============================================================================

gui.mainloop()

