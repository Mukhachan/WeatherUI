import sys, os, geocoder, pyowm, datetime
from time import sleep
from tkinter import *
from pyowm.utils.config import get_default_config
from requests import get

dt = datetime.datetime.now()
dt_string = dt.strftime("%H:%M:%S")
print(f"Now is {dt_string}")


from Config import *
f = open('cfg.txt', 'r')



owm = pyowm.OWM('e8f63f748bfc269a3f4db8203af0c657')
mgr = owm.weather_manager()
config_dict = get_default_config()
config_dict['language'] = 'ru'


def output_lang(event):
    CityLabel = Label(text='')
    CityLabel.grid(row=0, column=1)
    CityEntryB = Button(text='Search')
    CityEntryB.grid(pady=5, row=2, column=1)

def output_search(event):    
    S = CityEntry.get()
    observation = mgr.weather_at_place(S)
    w = observation.weather
    Deg = w.temperature('celsius')['temp']
    print(Deg)

    D1 = round(Deg)
    Cloud = w.wind()['speed']

    DEGEntry.delete(0, END)
    DEGEntry.insert(0, f'{D1}°')
    CloudsEntry.delete(0, END)
    CloudsEntry.insert(0, f'{Cloud} м/с')

def close():
    sleep(0.15)
    sys.exit()

def start_reference():
    window = Toplevel(root)
    window.title('О программе')
    window.resizable(1,1)
    canvas = Canvas(window, width=350, height=350)
    canvas.pack()

def search():
    ip = get('https://api.my-ip.io/ip').text
    g = geocoder.ipinfo(ip)
    print(ip)
    print(g)
    print(g.city)
    CityEntry.delete(0, END)
    CityEntry.insert(0, g.city)

def preferences():
    f = open("cfg.txt", "r")
    
    def DEB():
        
        print(var1.get())
        if var1.get() == 0:
            os.remove("cfg.txt")
            f = open("cfg.txt", "w")
            f.write("0")
            f.close()
            
            #UnMatch = Label(window_1,text="Автопоиск отключен")
            #UnMatch.place(relx=0.5, rely=0.5)

        elif var1.get()==1:
            os.remove("cfg.txt")
            f = open("cfg.txt", "w")
            f.write("1")
            f.close()

            #UnMatch = Label(window_1,text="Автопоиск включен")
            #UnMatch.place(relx=0.5, rely=0.5)            
        
            

    window_1 = Toplevel(root)
    window_1.title('Настройки')
    window_1.iconbitmap('ICO.ico')
    canvas1 = Canvas(window_1, width=250, height=200)
    canvas1.pack()

    var1 = IntVar()
    stat = f.read(1)
    var1.set(stat)

    auto_search = Checkbutton(window_1, text='Автопоиск города',
     onvalue=1, offvalue=0, variable=var1, command=DEB)
    print(var1)
    auto_search.place(relx=0.5, rely=0.2, anchor=CENTER)
    f.close()

def start_PC_configuration():

    window_2 = Toplevel(root)
    window_2.title( 'О твоём ПК' )
    window_2.iconbitmap('ICO.ico')
    window_2.geometry('350x500+750+250')
    window_2.resizable(0,0)
    canvas1 = Canvas(window_2)
    canvas1.pack()  

    text = Text(window_2, width=30)
    text.place(relx = 0.5, anchor=N)
    from PcConfigure import PC_CONFIGURE
    text.insert(1.0, PC_CONFIGURE)


# root #
root = Tk()
root.title("WeatherUI")
root.geometry('450x300+750+250')
root.resizable(False,False)
root.iconbitmap('ICO.ico')

# Menu #
mainmenu = Menu(root)
root.config(menu=mainmenu)

referencemenu = Menu(mainmenu, tearoff=0)
referencemenu.add_command(label='О программе', command=start_reference)
referencemenu.add_command(label='О твоём компьютере', command=start_PC_configuration)

actionmenu = Menu(mainmenu, tearoff=0)
actionmenu.add_command(label='Закрыть', command=close)

""" prefmenu = Menu(mainmenu, tearoff=0)
prefmenu.add_command(label='Геопозиция') """

mainmenu.add_cascade(label='Действия', menu = actionmenu)
mainmenu.add_cascade(label='Настройки',command=preferences)
mainmenu.add_cascade(label='Справка', menu = referencemenu)


# LABEL #
CityLabel = Label(root, text='Пожалуйства введите город')
Result = Label(root, text='Результат')
Temp = Label(root, text='Температура:')
Wind = Label(root, text='Ветренность:')

# Button #
BtnLNG = Button(root, text='', width=5, height=1)
CityEntryB = Button(root, text='Поиск', width=15)

# Entry #
CityEntry = Entry(justify=CENTER)
DEGEntry = Entry(justify=CENTER)
DEGEntry.insert(0, 'Здесь температура')
CloudsEntry = Entry(justify=CENTER)
CloudsEntry.insert(0, 'Облачность')

# PLACE #
# BtnLNG.grid(pady=5, padx=5, row=0, column=0, sticky=NW) #
CityLabel.place(relx=0.5, rely=0.1, anchor=CENTER)
CityEntry.place(relx=0.5, rely=0.2, anchor=CENTER)
CityEntryB.place(relx=0.5, rely=0.35, anchor=CENTER)
Result.place(relx=0.5, rely=0.47, anchor=CENTER)
DEGEntry.place(relx=0.5, rely=0.6, anchor=CENTER)
CloudsEntry.place(relx=0.5,rely=0.77, anchor=CENTER)
Temp.place(relx=0.2, rely=0.6, anchor=CENTER)
Wind.place(relx=0.2, rely=0.77, anchor=CENTER)


# bind #
#BtnLNG.bind('<Button-1>', output_lang)#
CityEntryB.bind('<Button-1>', output_search)


# AUTO-SEARCH #
if f.read(1) == "1":
    from CityGet1 import *
    from CityGet1 import Gorod

    CityEntry.delete(0, END)
    CityEntry.insert(0, Gorod)
    f.close()

f.close()
root.mainloop()