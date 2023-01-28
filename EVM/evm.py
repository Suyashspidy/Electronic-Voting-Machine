from tkinter import *
import tkinter as tk
root=Tk()
vote_count=0
counta=0
countb=0
countc=0
countd=0


l1=Label(root)
l1.grid(row=5,column=3,columnspan=4)


l2=Label(root)
l2.grid(row=6,column=3,columnspan=2)

def BJP():
    #vote A
    global vote_count,counta
    vote_count+=1
    counta+=1
    
    result="Total number of votes are:"+str(vote_count)
    l1.config(text=str(result))
    
    

def AAP():
    #vote B
    global vote_count,countb
    vote_count+=1
    countb+=1
    
    result="Total number of votes are:"+str(vote_count)
    l1.config(text=str(result))
    
     
def BSP():
    #vote C
    global vote_count,countc
    vote_count+=1
    countc+=1
    
    result="Total number of votes are:"+str(vote_count)
    l1.config(text=str(result))
    
def SP():
    #vote D
    global vote_count,countd
    vote_count+=1
    countd+=1
    
    result="Total number of votes are:"+str(vote_count)
    l1.config(text=str(result))
   











def result_disp():
    
    global counta,countb,countc,countd,vote_count
    if counta>countb and counta>countc and counta>countd:
        per=(counta/vote_count)*100
        winner="BJP is winner"
        l2.config(text=str(winner))
    elif countb>countc and countb>countd:
        per=(countb/vote_count)*100
        winner="AAP is winner"
        l2.config(text=str(winner))
        #b
    elif countc>countd:
        per=(countc/vote_count)*100
        winner="BSP is winner"
        l2.config(text=str(winner))
        #c
    else:
        per=(countd/vote_count)*100
        winner="SP is winner"
        l2.config(text=str(winner))
        #d




votea= tk.Button(root, 
                   text="VOTE BJP", 
                   fg="black",bg="white",
                   command=BJP,height=2,width=10,borderwidth=4)
votea.grid(row=0,column=3,padx=10,pady=10)


voteb= tk.Button(root,
                   text="VOTE AAP",
                   fg="black",bg="white",
                   command=AAP,height=2,width=10,borderwidth=4)
voteb.grid(row=1,column=3,padx=10,pady=10)


votec= tk.Button(root, 
                   text="VOTE BSP", 
                   fg="black",bg="white",
                   command=BSP,height=2,width=10,borderwidth=4)
votec.grid(row=2,column=3,padx=10,pady=10)
voted= tk.Button(root,
                   text="VOTE SP",
                   fg="black",bg="white",
                   command=SP,height=2,width=10,borderwidth=4)
voted.grid(row=3,column=3,padx=10,pady=10)
rs= tk.Button(root,
                   text="Result",
                   fg="black",bg="white",
                   command=result_disp,height=2,width=10,borderwidth=4)
rs.grid(row=4,column=3,padx=10,pady=10)




photo=PhotoImage(file="abc1.png")
label1=Label(root,image=photo, height=50,width=50)
label1.grid(row=0,padx=10,pady=10)



'''label12=Label(root,text="BJP")
label12.grid(row=0,padx=10,pady=10)'''


photo1=PhotoImage(file="abc.png")
label2=Label(root,image=photo1, height=50,width=50)
label2.grid(row=1,padx=10,pady=10)
label13=Label(root,text="AAP")
label13.grid(row=1,padx=10,pady=10)

photo2=PhotoImage(file="abc2.png")
label3=Label(root,image=photo2, height=50,width=50)
label3.grid(row=2,padx=10,pady=10)
label14=Label(root,text="BSP")
label14.grid(row=2,padx=10,pady=10)

photo3=PhotoImage(file="abc3.png")
label4=Label(root,image=photo3, height=50,width=50)

label4.grid(row=3,padx=10,pady=10)
label15=Label(root,text="SP")
label15.grid(row=3,padx=10,pady=10)






root.geometry("480x640")

root.mainloop()
