import youtube_dl

ydl_opts = {
    'format': 'worst',
    'postprocessors': [{
        'key': 'FFmpegMetadata',
        # 'recode-video':'mp4'
        # 'preferredcodec': 'mp4',
        # 'preferredquality': '192',
    }],
}

def download(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


# download('https://youtu.be/Hn5P5h107Ws')
# download('https://youtu.be/KjVcEuDXHG4')
# download('https://youtu.be/aMserc5rLZA')
# download('https://youtu.be/RzOYeI-S0c0')
# download('https://youtu.be/6P5o8yhrpIA')
