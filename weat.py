from tkinter import *
from tkinter import ttk
import requests
import os

def get_data():
    city = city_name.get()
    api_key=API
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid={api_key}").json()
    des_label1.config(text=data["weather"][0]["main"])
    desc_label1.config(text=data["weather"][0]["description"])
    descr_label1.config(text=str(data["main"]["temp"]-273.15))
    descri1_label.config(text=data["main"]["pressure"])
win=Tk()
win.title("Weather app")
win.geometry('500x500')
win.configure(bg='pink')
name_label=Label(win,text="Weather forecast",font=("Freestyle Script",35))
name_label.place(x=10,y=55,height=50,width=500)
states_list=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
city_name=StringVar()
com=ttk.Combobox(win,text="Weather forecast",values=states_list,font=("MS PGothic",16),textvariable=city_name)
com.place(x=25,y=120,height=35,width=450)


des_label=Label(win,text="Weather Climate",font=("Freestyle Script",20))
des_label.place(x=5,y=290,height=40,width=200)
des_label1=Label(win,text="",font=("Freestyle Script",20))
des_label1.place(x=250,y=290,height=40,width=200)

desc_label=Label(win,text="Weather Description",font=("Freestyle Script",20))
desc_label.place(x=5,y=330,height=40,width=200)
desc_label1=Label(win,text="",font=("Freestyle Script",20))
desc_label1.place(x=250,y=330,height=40,width=200)

descr_label=Label(win,text="Temperature",font=("Freestyle Script",20))
descr_label.place(x=5,y=370,height=40,width=200)
descr_label1=Label(win,text="",font=("Freestyle Script",20))
descr_label1.place(x=250,y=370,height=40,width=200)

descri_label=Label(win,text="Pressure",font=("Freestyle Script",20))
descri_label.place(x=5,y=410,height=40,width=200)
descri1_label=Label(win,text="",font=("Freestyle Script",20))
descri1_label.place(x=250,y=410,height=40,width=200)

done_button=Button(win,text="Done",font=("MS PGothic",15),command=get_data)
done_button.place(y=190,height=50,width=100,x=200)


win.mainloop()