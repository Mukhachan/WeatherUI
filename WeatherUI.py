from cgitb import text
import sys, pyowm, datetime
from time import sleep
from tkinter import *
from pyowm.utils.config import get_default_config
from tkinter import messagebox as mb

dt = datetime.datetime.now()
dt_string = dt.strftime("%H:%M:%S")
print(f"Now is {dt_string}")

from Config import *
f = open('config.cfg', 'r')

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
    try:
        S = CityEntry.get()
        observation = mgr.weather_at_place(S)
        w = observation.weather
        Deg = w.temperature('celsius')['temp']
        print(Deg)
    except:
        mb.showerror("ошЫбка",
        "Ты неправильно ввёл город")
        sleep(1)
        CityEntry.delete(0, END)
        

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
    text_desc = 'Эта программа написана непрограммистом из Москвы',
    'Я надеюсь кому-то она обязательно поможет и будет удобна для использования',
    'Все ссылки:',
    ' vk:https://vk.com/fly_desiner'
    description = Text(window, text=text_desc , width=30)
    description.place(relx=0.5)

def start_PC_configuration():
    window_2 = Toplevel(root)
    window_2.title( 'О твоём ПК' )
    #window_2.iconbitmap('ICO.ico')
    window_2.geometry('350x370+750+250')
    window_2.resizable(0,1)
    canvas1 = Canvas(window_2)
    canvas1.pack()  

    text = Text(window_2, width=30)
    text.place(relx = 0.5, anchor=N)
    from PcConfigure import PC_CONFIGURE

    text.insert(1.0, PC_CONFIGURE)

def preferences():
    f = open("config.cfg", "r")
    def DEB():        
        print(f'DEB. {var1.get()}')
        if var1.get() == 0:
            
            f = open("config.cfg", "w")
            f.write("0\n"+str(var2.get()))
            f.close()
            
            UnMatch['text'] = 'Автопоиск выключен'

        elif var1.get()==1:
            f = open("config.cfg", "w")
            f.write("1\n" + str(var2.get()))
            f.close()

            UnMatch['text'] = 'Автопоиск включен'    
    
    window_1 = Toplevel(root)
    window_1.title('Настройки')
    #window_1.iconbitmap('ICO.ico')
    window_1.geometry('290x200+350+350')
    window_1.resizable(0,0)

    canvas1 = Canvas(window_1, width=250, height=200)
    canvas1.pack()

    var1 = IntVar()
    
    list  = f.readlines()
    print(f'str.113 {list}')
    var1.set(int(list[0]))
    var1.get()

    var2 = IntVar()
    list  = f.readlines()
    var2.get()

    UnMatch = Label(window_1,text='', bd=10, bg='#F0F0F0')
    UnMatch.place(relx=0.5, rely=0.30, anchor=CENTER)

    if var1.get()=='1':
        UnMatch[text] = 'Автопоиск включен'
        output_search
    elif var1.get()=='0':
        UnMatch[text] = 'Автопоиск выключен'
        

    auto_search = Checkbutton(window_1, text='Автопоиск города',
     onvalue=1, offvalue=0, variable=var1, command=DEB)
    print(var1)
    auto_search.place(relx=0.5, rely=0.1, anchor=CENTER)
    
    
    def WIND():
        print(f'WIND. {var2.get()}')
        if var2.get() == 0:
            f = open("config.cfg", "w+")
            f.write(str(var1.get())+"\n0")
            f.close()
            
            UnMatch2 = Label(window_1,text="Выключено", fg='#c20e0e')
            UnMatch2.place(relx=0.5, rely=0.65, anchor=CENTER)
            Wind.place_forget()
            CloudsEntry.place_forget()
            root.geometry("450x250")
            split_var2()
            
        elif var2.get()==1:
            f = open("config.cfg", "w+")
            f.write(str(var1.get())+"\n1")
            f.close()

            UnMatch2 = Label(window_1,text="Включено",bd=12, bg='#F0F0F0', fg='#00ad09')
            UnMatch2.place(relx=0.5, rely=0.65, anchor=CENTER)
            Wind.place(relx=0.2, rely=0.77, anchor=CENTER)
            CloudsEntry.place(relx=0.5,rely=0.77, anchor=CENTER)
            split_var2()
        

    wind_count = Checkbutton(window_1, text='Показывать ветренность',
     onvalue=1,offvalue=0, variable=var2, command=WIND)
    wind_count.place(relx=0.5, rely=0.5, anchor=CENTER)

    f.close()


# root #
root = Tk()
root.title("WeatherUI")
root.geometry('450x300+750+250')
root.resizable(False,False)
#root.iconbitmap('ICO.ico')

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
CityEntry.insert(0, 'Здесь ваш город')
DEGEntry = Entry(justify=CENTER)
DEGEntry.insert(0, 'Здесь температура')
CloudsEntry = Entry(justify=CENTER)
CloudsEntry.insert(0, 'Облачность')
TimeEntry = Entry(justify=CENTER)

# PLACE #
# BtnLNG.grid(pady=5, padx=5, row=0, column=0, sticky=NW) #
CityLabel.place(relx=0.5, rely=0.1, anchor=CENTER)
CityEntry.place(relx=0.5, rely=0.2, anchor=CENTER)
CityEntryB.place(relx=0.5, rely=0.35, anchor=CENTER)
#TimeEntry.place(relx=0.8, rely=0.35, anchor=CENTER, width=90)  
# НАДО РАЗОБРАТЬСЯ С 
# ВВЕДЕНИЕМ ВРЕМЕНИ!!!
Result.place(relx=0.5, rely=0.47, anchor=CENTER)
DEGEntry.place(relx=0.5, rely=0.6, anchor=CENTER)
CloudsEntry.place(relx=0.5,rely=0.77, anchor=CENTER)
Temp.place(relx=0.2, rely=0.6, anchor=CENTER)
Wind.place(relx=0.2, rely=0.77, anchor=CENTER)

# bind #
#BtnLNG.bind('<Button-1>', output_lang)#
CityEntryB.bind('<Button-1>', output_search)

def split_var2():
    f = open('config.cfg', 'r')
    splited = str(f.readlines())
    print(splited)
    
split_var2()
f.close

# AUTO-SEARCH #
f = open('config.cfg', 'r')
check_auto_search = f.readlines()[0]
print(f' Переменная - {check_auto_search}')
if check_auto_search == "1":
    
    from CityGet1 import *
    from CityGet1 import Gorod

    CityEntry.delete(0, END)
    CityEntry.insert(0, Gorod)
    output_search
elif check_auto_search == "0":
    
    print('Автопоиск выключен')

f.close()
root.mainloop()