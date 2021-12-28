import requests 
from tmp import download

def save_peter_pan():
    file1 = open("series.txt", "r")

    while True:
        # считываем строку
        line = file1.readline()
        
        # прерываем цикл, если строка пустая
        if not line:
            break
        else:
            lines = line.split(" - ")
            dest_name = lines[1] + ".mp4"
            id_video = lines[0].split('/')[-1]
            id_video = id_video.split('.')[0]
            url = "https://video.sibnet.ru/shell.php?videoid={}".format(id_video)
            destination = './pan/{}'.format(dest_name.replace("\n", ""))
            download(url)
    # закрываем файл
    file1.close

save_peter_pan()

