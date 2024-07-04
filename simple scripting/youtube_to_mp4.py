from pytube import YouTube

url = input("Enter Link: ")
youtube_1 = YouTube(url)

video = youtube_1.streams.all()
vid = list(enumerate(video))

for i in vid:
    print(i)
print()
stream = int(input("Enter ur selected quality: "))
print(f"Downloading Video: {youtube_1.title}")
video[stream].download()
print("Done!")


# *****FOR PLAYLISTS(144P)*****
# from pytube import Playlist
#
# url = input("Enter Link: ")
# py = Playlist(url)
# print(f"Downloading: {py.title}")
# for video in py.videos:
#     video.streams.first().download()
# print("Done!")
