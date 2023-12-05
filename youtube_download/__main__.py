from youtube_download import youtube as yt
from youtube_download import options

def main():
    arg = options.parse()
    youtube = yt.youtube_download(arg.urlpath)
    if arg.subparser == "video":
        youtube.download_single_video()
    if arg.subparser == "playlist":
        youtube.playlist_download(arg.num)


if __name__ == "__main__":
    main()
