import argparse
from pytube import YouTube
from pytube.cli import on_progress

def main():
  parser = argparse.ArgumentParser(description="Baixar vídeo do YouTube.")
  parser.add_argument("url", help="URL do vídeo do YouTube")
  args = parser.parse_args()
  url = args.url
  video = YouTube(url, on_progress_callback=on_progress)
  videoStream = video.streams.get_highest_resolution()

  videoStream.download()

  print("\nDownload concluído com sucesso!")
  

if __name__ == "__main__":
    main()