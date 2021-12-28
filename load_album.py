import requests 
from bs4 import BeautifulSoup
from tmp import download
import os
import time 

def album(album_url):
    res = requests.get(album_url, headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"})
    if res.status_code==200:
        text = res.text
        ### Раскомментировать если необходимо считать из файла
        # text = open('denis.html', 'r')
        # text = text.read()
        soup = BeautifulSoup(text, 'html.parser')
        arr = soup.find_all("a", class_="VideoCard__title") # вывод содержимого тэга 'p' классом 'some-class'
        index = 0
        for a in arr:
            ### Раскомментировать, если необходимо скачать не с первой серии
            # if index < 30:
            #     index += 1
            #     continue
            try:
                download('https://vk.com' + a.get('href'))
            except Exception as e:
                print(str(e))
                pass 
            time.sleep(3)
def rename_mp4():
    files = os.listdir(path=".")
    for file in files:
        try:
            os.rename(file, file.replace('.unknown_video', '.mp4'))
        except Exception as e:
            print("Ошибка")
        

album('https://vk.com/video/playlist/-155272962_113')
rename_mp4()
