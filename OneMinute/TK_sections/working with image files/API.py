from tkinter import *
import json
import requests
from PIL import ImageTk, Image

root = Tk()
root.title('API')
root.iconbitmap('C:/Users/HP/Documents/malo\'s/download.ico')
root.geometry('600x100')

zip_box = Entry(root)
zip_box.grid(row=0, column=0, stick=W+N+E+S)

def get_zip():
    global webLabel
    try:
        req = requests.get(f'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip_box.get()}&distance=5&API_KEY=5B4F9938-08BB-4555-A8AE-CDF4CD40BEAC')
        req2 = json.loads(req.content)
        area = req2[0]['ReportingArea']
        quality = req2[0]['AQI']
        category = req2[0]['Category']['Name']
        if category == 'Good':
            quality_colour = '#00E400'
        elif category == 'Moderate':
            quality_colour = '#FFFF00'
        elif category == 'Unhealthy for Sensitive Groups':
            quality_colour = '#FF7E00'
        elif category == 'Unhealthy':
            quality_colour = '#FF0000'
        elif category == 'Very Unhealthy':
            quality_colour = '#8f3f97'
        elif category == 'Hazardous':
            quality_colour = '#7e0023'
        webLabel = Label(root, text=area + ' Air Quality ' + str(quality) + ' ' + category, font='Helvetica',
                         background=quality_colour)
        webLabel.grid(row=1, column=0, columnspan=2)
        root.configure(background=quality_colour)
    except Exception:
        req2 = 'Error...'

zip_button = Button(root, text='Get Air Quality', command=get_zip)
zip_button.grid(row=0, column=1, stick=W+N+E+S)


def clear():
    global webLabel
    webLabel.destroy()
    zip_box.destroy()
    root.configure(background='white')

choose_another = Button(root, text='Clear and choose another', command=clear)
choose_another.grid(row=0, column=3)

root.mainloop()