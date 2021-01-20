from tkinter import *

root=Tk()
root.title("Secret Selection")
def Print():
    import login
    root.destroy()
    login.main()

F1=Frame(root,bd=10,highlightcolor="green", highlightthickness=1,padx=2,pady=2).pack()
img=PhotoImage(file='Raw.png')
L1=Label(F1,image=img,height=400)
L1.pack(fill=X,padx=5,pady=5)

for i in range(1,51):
    Bi=Button(F1,text=i,width=1,height=1,bg='Deep Sky Blue').place(x=0+26*i,y=500)#.grid(row=0,column=i)
        
for i in range(1,51):
    c=i+50
    Bc=Button(F1,text=50+i,bg='Deep Sky Blue',width=1,height=1).place(x=0+26*i,y=550)#.grid(row=1,column=i)

B101=Button(F1,width=1,height=1,command=Print,relief=FLAT).place(x=26,y=600)

root.geometry('2555x1455+0+0')
root.mainloop()
