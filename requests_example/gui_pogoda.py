import tkinter
from pogoda import get_location_id, get_location_weather, weather_report

def pobierz_pogode():
    location_name = pole.get()
    location_id = get_location_id(location_name)
    weather = get_location_weather(location_id)
    wynik.configure(text=pierwiastek)

root = tkinter.Tk()
# print("To jest przed mainloop")

label = tkinter.Label(master=root, text="Wpisz liczbe: ")
# label.pack()
label.grid(row=1, column=1)

pole = tkinter.Entry(master=root)
# pole.pack()
pole.grid(row=1, column=2)

button = tkinter.Button(master=root, text="Przelicz", command=pierwiastkuj)
button.grid(row=2, column=1)

wynik = tkinter.Label(master=root)
wynik.grid(row=2, column=2)

root.mainloop()
print("To jest po mainloop")