import urllib3
import json
import tkinter as tk
from datetime import date
from tkinter.ttk import *
from tkinter import *
import tkinter.font as font



http = urllib3.PoolManager()

r = http.request('GET', 'https://api.covid19api.com/total/country/united-states')
j = http.request('GET', 'https://api.covid19api.com/live/country/united-states')
data = r.data
data2 = j.data

data = json.loads(data)
data2 = json.loads(data2)


window = Tk()

window.resizable(width=False, height=False)

window.title("Covid 19 Cases")

window.geometry('500x200')

myFont = font.Font(size=13)

def clicked():

    if(selected.get() == 1):

        for item in data:

                obj = item['Confirmed']
        addressText.insert(tk.END, f'U.S. Total Cases:{obj}\n')


    if(selected.get() == 2):

        for item in data:

                obj = item['Deaths']

        addressText.insert(tk.END, f'U.S. Total Deaths:{obj}\n')

    if(selected.get() == 3):

        for item in data2:

            if(item['Province'] == 'Ohio'):
                obj = item['Confirmed']

        addressText.insert(tk.END, f'Ohio Total Cases:{obj}\n')

    if(selected.get() == 4):

        for item in data2:

            if(item['Province'] == 'Ohio'):
                obj = item['Deaths']

        addressText.insert(tk.END, f'Ohio Total Deaths:{obj}\n')

def clicked_2():

    addressText.delete("1.0","end")

lbl = Label(window, text="",anchor=W, justify=RIGHT)
lbl.grid(column=1, row=2)
selected = IntVar()

button = Button(window, text='Search', command = clicked)
clear = Button(window, text='Clear', command = clicked_2)
rad1 = Radiobutton(window,text='Total Confirmed', value=1, variable=selected)
rad2 = Radiobutton(window,text='Total Deaths', value=2, variable=selected)
rad3 = Radiobutton(window,text='Ohio Total Confirmed', value=3, variable=selected)
rad4 = Radiobutton(window,text='Ohio Total Deaths', value=4, variable=selected)


rad1.grid(column=1, row=0, sticky=W+E)
rad2.grid(column=2, row=0, sticky=W+E)
rad3.grid(column=1, row=1, sticky=W+E)
rad4.grid(column=2, row=1, sticky=W+E)
button.grid(column=2, row=2, sticky=N)
clear.grid(column=2, row=2, sticky=S)
addressText = Text(window, padx=5, pady=5, width=30, height=6)
addressText.grid(row=2, column=1, padx=5, pady=5, sticky=W)


button['font'] = myFont
clear['font'] = myFont
rad1['font'] = myFont
rad2['font'] = myFont
rad3['font'] = myFont
rad4['font'] = myFont
lbl['font'] = myFont


window.mainloop()
