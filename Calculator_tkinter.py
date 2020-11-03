import tkinter
newNum = True
operator=''
num1=0
result=0

window=tkinter.Tk()
window.title("My Calculator")

entry=tkinter.Entry(window, justify="right")
entry.grid(row=0, column=0,columnspan=4)
entry.insert(0,"0")

def pressNum(num):
    global newNum
    
    if newNum:
        newNum=False
        entry.delete(0,tkinter.END)
    
    entry.insert(tkinter.END,num)


seq=0
for char in [7, 8, 9, 4, 5, 6, 1, 2, 3]:
    btn=tkinter.Button(window, text=char, width=4)
    btn["command"]=lambda num = char : pressNum(num)
        
    btn.grid(row=int(seq/3)+2, column=int(seq%3))
    seq=seq+1

btn= tkinter.Button(window, text=0, width=9)
btn["command"]=lambda num = char : pressNum(num)
btn.grid(row=5,column=0, columnspan=2)


def pressOp(op) :
    global operator, num1, newNum
    num1=int(entry.get())
    operator= op
    newNum=True

seq=1
for char in ['/','*','+','-']:
    btn=tkinter.Button(window,text=char,width=4)
    btn["command"]=lambda op= char : pressOp(op)
    btn.grid(row=seq, column=3)
    seq+=1

btn= tkinter.Button(window, text='%', width=4)
btn["command"]=lambda op = char : pressOp(op)
btn.grid(row=1,column=2)

def calc():
    global num1
    global newNum
    if operator =="+":
        result=num1+int(entry.get())
        entry.delete(0,tkinter.END)
        entry.insert(0,str(result))
        num1=0
        newNum=True
    elif operator =="-":
        result=num1-int(entry.get())
        entry.delete(0,tkinter.END)
        entry.insert(0,str(result))
        num1=0
        newNum=True
    elif operator =="*":
        result=num1*int(entry.get())
        entry.delete(0,tkinter.END)
        entry.insert(0,str(result))
        num1=0
        newNum=True
    elif operator =="/":
        result=int(num1/int(entry.get()))
        entry.delete(0,tkinter.END)
        entry.insert(0,str(result))
        num1=0
        newNum=True
    elif operator =="%":
        result=num1%int(entry.get())
        entry.delete(0,tkinter.END)
        entry.insert(0,str(result))
        num1=0
        newNum=True
btn=tkinter.Button(window, text='=',width=4,command=calc)
btn.grid(row=5,column=3)
window.mainloop()
