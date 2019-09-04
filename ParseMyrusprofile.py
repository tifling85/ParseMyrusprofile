import requests
from bs4 import BeautifulSoup
import csv
from tkinter import *

root = Tk()

def get_url():
    return 'https://www.rusprofile.ru/search?query=' + e1.get() + '&type=ul'

def ins_buff():
    e1.insert(0, root.clipboard_get())

def get_html(url):
    r = requests.get(url)
    return r.text

def get_info(html):
    soup = BeautifulSoup(html, 'lxml')
    dates = []
    data = ['Наименование организации', soup.find('div', class_ = 'ya-share2-data').get('data-title')]
    dates.append(data)
    data = ['ОГРН', soup.find('div', class_ = 'ya-share2-data').get('data-ogrn')]
    dates.append(data)
    data = ['ИНН', soup.find('div', class_ = 'ya-share2-data').get('data-inn')]
    dates.append(data)
    data = ['Дата регистрации', soup.find('div', class_ = 'ya-share2-data').get('data-date')]
    dates.append(data)
    data = ['Юридический адрес', soup.find('div', class_ = 'ya-share2-data').get('data-address')]
    dates.append(data)
    data = ['Руководитель', soup.find('a', class_= 'link-arrow gtm_main_fl').find('span').text]
    dates.append(data)
    return dates

def csv_writer(data):
    with open('parse.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter = ';')
        for line in data:
            writer.writerow(line)

def main():
    #url = 'https://www.rusprofile.ru/search?query=2460242115&type=ul'
    url = 'https://www.rusprofile.ru/search?query=' + e1.get() + '&type=ul'
    data = get_info(get_html(url))
    print(data)
    csv_writer(data)


if __name__ == '__main__':
    Label(text = 'Введите ИНН организации').pack()
    e1 = Entry(width = 25)
    e1.pack()
    b1 = Button(text = 'Вставить из буфера', command = ins_buff)
    b1.pack()
    b = Button(text = 'Получить информацию', command = main)
    b.pack()
    root.mainloop()

