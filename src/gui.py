from tkinter import *
from turtle import onclick
from PIL import ImageTk, Image
from model.DataCenter import DataCenter

WIDTH = 910
bg_color = '#1E4154'
fontc = 'Calibri'

def start():
    data_center = DataCenter(inputfile.get())
    






# GUI settings
window = Tk()

window.geometry('900x500')
window.configure(bg=bg_color)
window.resizable(0,0)
window.title('Optimize a Data Center')


Label(window,text='OPTIMIZE A DATA \nCENTER',font=(fontc,45,'bold'),justify=LEFT, fg='white',background=bg_color).place(x=80, y=30)
Label(window,text='Inteligência Artificial 21/22',font=(fontc,10,'italic'),fg='white',background=bg_color).place(x=740, y=10)

small_circle = ImageTk.PhotoImage(Image.open('./assets/small_circle.png'))
medium_circle = ImageTk.PhotoImage(Image.open('./assets/medium_circle.png'))
big_circle = ImageTk.PhotoImage(Image.open('./assets/big_circle.png'))

Label(window, image=small_circle, background=bg_color, width=300).place(x=600,y=100)
Button(window, text='Additional\ninfo', font=(fontc,18), command= print('oi'), fg='white',background='#5A9BC0', bd=0, cursor='hand2').place(x=690,y=140)

Label(window, image=big_circle, background=bg_color, width=300).place(x=300,y=130)
Button(window, text='START', font=(fontc,35,'bold'), fg='white',background='#306A8A', bd=0, cursor='hand2', command=start).place(x=370,y=200)

inputfile = StringVar(window, value='input.txt')
Label(window, image=medium_circle, background=bg_color, width=300).place(x=570,y=300)
Entry(window, textvariable = inputfile, fg='white',width=9, font=(fontc,23,'italic'), background='#4A5D68').place(x=670,y=370)




def display():
    window.mainloop()

