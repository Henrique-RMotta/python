import webbrowser
# informe a url do vídeo aqui:
url = "https://www.youtube.com/watch?v=2QlYKKiT4Js"
download = url[:12] + "ss" + url[12:]

webbrowser.open(download)