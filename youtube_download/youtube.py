import concurrent.futures
from pytube import Playlist, YouTube
import re


class youtube_download:
    def __init__(self, url):
        self.url = url
        if self._check_url_playlist(self.url):
            self.playlist = Playlist(self.url)
        else:
            self.video = YouTube(self.url)

    @staticmethod
    def _check_url_playlist(url):
        match = re.search(r"playlist", url)
        return True if match else False

    def download_videos(self, vid):
        print(f"Video to be downloaded: {vid.title}")
        vid.streams.get_highest_resolution().download()
        return vid.title

    def download_single_video(self):
        self.download_videos(self.video)

    @property
    def playlist_length(self):
        return len(self.playlist.video_urls)

    @staticmethod
    def _chunking(entire_list, num_of_elem_in_chunks):
        chunked_array = []
        for i in range(0, len(entire_list), num_of_elem_in_chunks):
            chunked_array.append(entire_list[i:i+num_of_elem_in_chunks])
        return chunked_array

    def playlist_download(self, parallel_number):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            chucked_video_array = self._chunking(list(self.playlist.videos), parallel_number)
            for vid_array in chucked_video_array:
                results = {}

                for video in vid_array:
                    results[executor.submit(self.download_videos, video)]=video.title

                for result in concurrent.futures.as_completed(results.keys()):
                    try:
                        success = result.result()
                        print(f"Video COMPLETED - {success} successfully.")
                    except Exception as e:
                        print(f"Video FAILED - {results[result]}.")

    def __str__(self) -> str:
        return f"Youtube download URL : {self.url}"

