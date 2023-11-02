# main.p
import os
from pytube import YouTube, Playlist
import json
import sys

def download_video(url,path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        video_title = yt.title
        video_image = yt.thumbnail_url
        # Crie um diretório para salvar o vídeo, se ele não existir
        if not os.path.exists(path):
            os.makedirs(path)

        # Forçar a extensão para .mp4
        file_path = os.path.join(path, f"{video_title}.mp4")
        info = {'Downloading': video_title}
        print(json.dumps(info))
        # Realize o download do vídeo
        stream.download(output_path=path, filename=video_title)

        # Renomeie o arquivo para forçar a extensão .mp4
        os.rename(os.path.join(path, video_title), file_path)

        result = {'success': True, 'filename': f'{video_title}.mp4','image':f'{video_image}'}
    except Exception as e:
        result = {'success': False, 'error': str(e)}
    # Converta o resultado em JSON e imprima-o para que o JavaScript possa lê-lo
    print(json.dumps(result))
    
def download_playlist(url, output_path='.'):
    playlist = Playlist(url)
    for video_url in playlist.video_urls:
        download_video(video_url, output_path)

if len(sys.argv) < 2:
    print("Uso: main.py <funcao_a_executar>")
else:
    funcao_a_executar = sys.argv[1]
    if funcao_a_executar == 'download_video':
        if not os.path.exists(sys.argv[3]):
            os.makedirs(sys.argv[3])
        if "playlist" in sys.argv[2]:
             download_playlist(sys.argv[2], sys.argv[3])
        else:
              download_video(sys.argv[2], sys.argv[3])
      
