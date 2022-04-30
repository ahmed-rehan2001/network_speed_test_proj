from tkinter import *
from tkinter.ttk import *
import speedtest
import multiprocessing
jobs = []
top = Tk()
top.minsize(300,300)

def speed_test():
    s = speedtest.Speedtest()
    download_result = s.download() / 1025 / 1024
    upload_result = s.upload() / 1024 / 1024
    dowlabel = Label(text=str(f"Your download speed is:{download_result:.2f}mbit/s"))
    uplabel = Label(text=str(f"Your upload speed is:{upload_result:.2f}mbit/s"))
    dowlabel.pack()
    uplabel.pack()


def loading():
   task =10
   x=0
   while(x<task):
    bar['value'] += 10
    x+=1

def test():

    p = multiprocessing.Process(target=loading())
    jobs.append(p)
    f = multiprocessing.Process(target=speed_test())
    jobs.append(f)
    p.start()
    f.start()

if __name__ == '__main__':
 bar = Progressbar (top,orient=HORIZONTAL,length=250)
 bar.pack(pady=30)
 but=Button(text="speed test",command=test)
 but.pack(pady=30)
 top.mainloop()

#######################################

