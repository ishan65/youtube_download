from youtube_download import youtube as yt
from youtube_download import options


def main():
    arg = options.parse()
    ytube = yt.youtube_download(arg.urlpath)
    if arg.subparser == "video":
        ytube.download_single_video(arg.savepath)
    if arg.subparser == "playlist":
        ytube.playlist_download(arg.num, arg.savepath)


if __name__ == "__main__":
    main()
