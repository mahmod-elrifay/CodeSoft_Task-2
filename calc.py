from tkinter import *
import customtkinter as s

def addoperation():
    if btn :
        label.configure(text="+")
def suboperation():
    if btn1 :
        label.configure(text="-")
def multoperation():
    if btn2 :
        label.configure(text="*")
def divoperation():        
    if btn3 :
        label.configure(text="/")

def result():
    if label._text == "+":
        m = int(num1.get()) + int(num2.get())
        result.delete(0,END)
        result.insert(0,m)
    elif label._text == "-":    
        m = int(num1.get()) - int(num2.get())
        result.delete(0,END)
        result.insert(0,m)
    elif label._text == "*":
        m = int(num1.get()) * int(num2.get())
        result.delete(0,END)
        result.insert(0,m)
    else:    
        m = int(num1.get()) / int(num2.get())
        result.delete(0,END)
        result.insert(0,m)
        
    
s.set_appearance_mode("dark")
s.set_default_color_theme("dark-blue")
form = s.CTk()
form.geometry("300x220")
form.resizable(False,False)
form.title("Calculator")
font = s.CTkFont(family="Bahnschrift",size=20)
font1 = s.CTkFont(family="Bahnschrift",size=14)

# Buttons frame
frame = s.CTkFrame(form,width=40,height=160)
frame.place(relx=0.88,rely=0.38,anchor = CENTER)
# Entry frame
frame1 = s.CTkFrame(form,width=230,height=160)
frame1.place(relx=0.4,rely=0.38,anchor = CENTER)
# Result frame
frame2 = s.CTkFrame(form,width=280,height=40)
frame2.place(relx=0.48,rely=0.87,anchor = CENTER)
# Entry of 1st num.
num1 = s.CTkEntry(frame1,font=font1,width=220,corner_radius=5,placeholder_text="Enter 1st number",fg_color="#212121",border_color="#383838")
num1.place(relx=0.5,rely=0.2,anchor = CENTER)
# Entry of 2nd num.
num2 = s.CTkEntry(frame1,font=font1,width=220,corner_radius=5,placeholder_text="Enter 2nd number",fg_color="#212121",border_color="#383838")
num2.place(relx=0.5,rely=0.5,anchor = CENTER)
# Buttons on frame
btn = s.CTkButton(frame,text="+",width=30,font=font,fg_color="#2d2d2d",hover_color="#383838",command=addoperation)
btn.place(relx=0.5,rely=0.12,anchor = CENTER)
btn1 = s.CTkButton(frame,text="-",width=30,font=font,fg_color="#2d2d2d",hover_color="#383838",command=suboperation)
btn1.place(relx=0.5,rely=0.37,anchor = CENTER)
btn2 = s.CTkButton(frame,text="×",width=30,font=font,fg_color="#2d2d2d",hover_color="#383838",command=multoperation)
btn2.place(relx=0.5,rely=0.62,anchor = CENTER)
btn3 = s.CTkButton(frame,text="÷",width=30,font=font,fg_color="#2d2d2d",hover_color="#383838",command=divoperation)
btn3.place(relx=0.5,rely=0.86,anchor = CENTER)
# Equal button
btn4 = s.CTkButton(frame1,text="=",width=210,font=font,fg_color="#2d2d2d",hover_color="#383838",command=result)
btn4.place(relx=0.5,rely=0.83,anchor = CENTER)
# Result
result = s.CTkEntry(frame2,font=font1,width=260,corner_radius=20,fg_color="#212121",border_color="#383838")
result.place(relx=0.5,rely=0.5,anchor = CENTER)
label = s.CTkLabel(form,text="")
label.place(relx=0.5,rely=5,anchor = CENTER)
form.mainloop()