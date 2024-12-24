from tkinter import *
import json
import requests
from PIL import ImageTk, Image

root = Tk()
root.title('API')
root.iconbitmap('C:/Users/HP/Documents/malo\'s/download.ico')
root.geometry('400x100')

try:
    req = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=90712&distance=5&API_KEY=5B4F9938-08BB-4555-A8AE-CDF4CD40BEAC')
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
    webLabel = Label(root, text=area + ' Air Quality ' + quality + ' ' + category, background=quality_colour)
    webLabel.pack()
except Exception:
    req2 = 'Error...'

root.mainloop()