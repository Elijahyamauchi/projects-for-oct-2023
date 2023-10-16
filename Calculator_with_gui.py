#written by Elijah Yamauchi
#goal, a calculator with a gui that can take in 2 numbers then add, subtract, multiply, or divide
#posible upgrade in line with this project, make it so that the buttons are all the same size.
import tkinter as tk
def button_click(event):
    text = event.widget.cget("text")
    if text == '=':
        try:
            result=str(eval(screen.get()))
            screen.set(result) 
        except:
            screen.set("Error")
    elif text=='C':
        screen.set("")
    else:
        screen.set(screen.get()+text)
        #this line causes a glith where the user can change the result after the calculation.

#creates the main aplication window
height=300
width=400
root = tk.Tk()
root.geometry(f"{height}x{width}")    
root.title("Calculator")

#creates the variable that holds the string that the cal will manipulate
screen=tk.StringVar()
entry=tk.Entry(root,textvariable=screen,font="lucida 20 bold")
entry.pack(fill="both",ipadx=8,padx=10,pady=10)

#creates the frames for the button
button_Frame = tk.Frame(root)
button_Frame.pack()

buttons = ["7","8","9","+",
           "4","5","6","-",
           "1","2","3","*",
           "C","0","=","/",]

# I want to tie the height and width variable to the button so that they will fill the space no matter what
#question one, how do I manipulate the size of the button?
b=0
for button in buttons:
    button=tk.Button(button_Frame,text=button,font=f"lucida {height//10} bold")
    button.grid(row=b//4,column=b%4)
    button.bind("<Button-1>", button_click)
    b+=1

for i in range(4):
    button_Frame.grid_rowconfigure(i, weight=1)
    button_Frame.grid_columnconfigure(i, weight=1)



root.mainloop()

