from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import requests 


url ='https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
api_key ='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'




def get_weather(city):
    result =requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        #city, timezone, country, temp (degrees), temp (fahrenheit), pressure,humidity  icon, weather, description
        
        city =json['name']
        country =json['sys']['country']
        wind_speed = json['wind']['speed']
        temp_kelvin = json['main']['temp']
        temp_degrees = temp_kelvin - 273.15
        temp_fahrenheits = (temp_kelvin - 273.15) * 9/5 + 32
        pressure =json['main']['pressure']
        humidity = json['main']['humidity']
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        description= json['weather'][0]['description']
        
        final = (city, country,  temp_degrees, temp_fahrenheits, wind_speed, weather, pressure, humidity,  description)
        return final
    else:
        return None
    


def search():
    
    city = city_entry.get()    
    weather = get_weather(city)
    
    if weather:
        location_lbl['text']= '{}, {}'.format(weather[0], weather[1])
        # image['bitmap']= 'icons/{}.png'.format(weather[4])
        temp_lbl['text']= '{:.2f}◦C,    {:.2f}◦F'.format(weather[2], weather[3])
        weather_lbl['text']=weather[5]
        wind_speed['text']='{:.2f}  metres per seconds'.format(weather[4])
        pressure['text']='{:.2f}    pascal (Pa)'.format(weather[6])
        humidity['text']='{:.2f}  g.m-3'.format(weather[7])
        description['text']=weather[8]
    
    
    else:
        messagebox.showerror('Error', 'Cannot find city{}'.format(city))
        



app = Tk()
app.title("Weather Focus created by Mashup-J")
app.geometry('900x480')
app.resizable(False, False)
icon =ImageTk.PhotoImage(file="images/officiallogoi.png")
app.iconphoto(False, icon)


bg =ImageTk.PhotoImage(file="images/20201229_185954.jpg")
bg_image=Label(app, image=bg).place(x=0,y=0, relwidth=1, relheight=1)



city_entry = Entry(app, width=40, font=(34))
city_entry.place(x=300, y=16)

search_btn =Button(app, text='Search Weather', width=12,font=(2),command= search, bg="#FFFF00")
search_btn.place(x=420, y=50)

location_lbl = Label(app, text='', font=('bold', 30), width=12)
location_lbl.place(x=350, y=100)

wind_speed =Label(app, text='', bg="#CCFFFF", width=20)
wind_speed.place(x=410, y=170)

pressure =Label(app, text='', bg="#CCFFFF", width=20)
pressure.place(x=410, y=220)

humidity =Label(app, text='', bg="#CCFFFF", width=20)
humidity.place(x=410, y=270)


# image = Label(app, bitmap='')
# image.pack()

temp_lbl = Label(app, text='', bg="#CCFFFF", width=20)
temp_lbl.place(x=410, y=320)

weather_lbl = Label(app, text='', bg="#CCFFFF", width=20)
weather_lbl.place(x=410, y=370)

description =Label(app, text='', bg="#CCFFFF", width=20)
description.place(x=410, y=420)



app.mainloop()


