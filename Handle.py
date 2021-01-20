from tkinter import *

def Call_1():
    root.destroy()
    import Encrypt

def Call_2():
    root.destroy()
    import Decrypt

root=Tk()

F1=Frame(root,bg='black',width=600,height=600)

L1=Label(F1,bg='White',text='RAW',font=('Times New Roman',100,'bold'),width=200).pack(padx=50,pady=50)
L2=Label(F1,bg='White',text='Encryption',font=('arial',20,'bold')).pack(side=LEFT,padx=75,pady=80)
L3=Label(F1,bg='White',text='Decryption',font=('arial',20,'bold')).pack(side=RIGHT,padx=75,pady=80)

B1=Button(F1,text='Choose 1',fg='white',bg='grey',command=Call_1).place(x=125,y=500)
B2=Button(F1,text='Choose 2',fg='white',bg='grey',command=Call_2).place(x=425,y=500)

F1.pack(fill=BOTH,expand=1)
root.geometry('600x600+400+100')
root.mainloop()
