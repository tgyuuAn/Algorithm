from tkinter import *
import datetime as dt
import random as rd

def gui():
    global TARGET

    def game_main():
        global now_year
        global COUNT
        global TARGET
        month = int(entry_1.get())
        day = int(entry_2.get())

        text = label_7.cget("text")

        input = dt.datetime(now_year,month,day)

        delta = (input-TARGET).days
        if delta <0 :
            text += f"\n{COUNT+1}회 : {month}월, {day}일, 이릅니다."
            label_7.config(text=text)            
            COUNT +=1

        elif delta >0 :
            text += f"\n{COUNT+1}회 : {month}월, {day}일, 늦습니다."
            label_7.config(text=text)
            COUNT +=1

        else :
            label_7.config(text = "축하합니다. 성공입니다.")
        
        if COUNT == 11:
            label_7.config(text="횟수초과, 실패하셨습니다.\n 타겟이 재설정 됩니다.")
            TARGET=make_target()
            label_8.config(text=f"타 겟 : {TARGET}")
            COUNT = 0

    window = Tk()
    window.geometry("300x320")
    window.title("날짜 맞추기")

    label_1 = Label(window,text="게임을 시작합니다.")
    label_2 = Label(window,text="월/일을 입력하세요.")
    label_5 = Label(window, text="월")
    label_6 = Label(window, text="일")
    label_7 = Label(window, text=" ")
    label_8 = Label(window, text=f"타 겟 : {TARGET}")

    entry_1 = Entry(window,width=10)
    entry_2 = Entry(window,width=10)

    button_1 = Button(window, text="제 출", command=game_main)

    label_1.grid(row=0,column=1)

    label_2.grid(row=1,column=1)

    label_5.grid(row=2,column=0)
    entry_1.grid(row=2,column=1)

    label_6.grid(row=3,column=0)
    entry_2.grid(row=3,column=1)

    button_1.grid(row=4,column=1)

    label_7.grid(row=5,column=1)

  #  label_8.grid(row=6,column=1)
    window.mainloop()

def make_target():
    global now_year
    gap = dt.datetime(now_year,12,31)-dt.datetime(now_year,1,1)
    random_days=rd.randint(0,gap.days)
    return dt.datetime(2022,1,1)+dt.timedelta(days=random_days)

now_year=dt.datetime.now().year
COUNT = 0
TARGET = make_target()

gui()
