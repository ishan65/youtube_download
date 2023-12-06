## Dependency

- pytube[https://pypi.org/project/pytube/]

## CLI

USAGE
```
usage: Download [-h] [-v] {video,playlist} ...

Download Youtube CLI

positional arguments:
  {video,playlist}
    video           video to download
    playlist        playlist to download

options:
  -h, --help        show this help message and exit
  -v, --version     show program's version number and exit
```

To download single video:
```
 python -m youtube_download video -url "https://www.youtube.com/watch?v=7uCpVOSXk8I" -save "C:\Users\im530\Downloads\dtdt"
```
``````

To download entire playlist:
```
 python -m youtube_download playlist -url "https://www.youtube.com/playlist?list=PLW489siXAtnoA_fOdIzMHU8gAZHHfp-T5" -save "C:\Users\im530\Downloads\dtdt" -num 2
```
 - num : How many videos to be downloaded parallelly.

