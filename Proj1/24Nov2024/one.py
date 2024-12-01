# #day 10 : exceptions
#
# print("start of prog")
# print("start of prog")
# try:
#     print("my input..",x)
# except:
#     print("=====>exception occur..")
# else:
#     print("will print when no exception occur..")
# finally:
#     print("will print always..")
#
# print("End..")
#
#
# #file handling
#
# file = open("C:\\Users\\e010846\\PycharmProjects\\Proj1\\file\\text.txt",'w')
# file.write("priti...\n")
# file.write("pritibhavika...\n")
# file.write("pritipratap...\n")
# file.close()
# #reading
# file = open("C:\\Users\\e010846\\PycharmProjects\\Proj1\\file\\text.txt",'r')
# print(file.read())
#
# #append
#
# file = open("C:\\Users\\e010846\\PycharmProjects\\Proj1\\file\\text.txt",'a')
# file.write("newline....")
# file.close()

#
# from pytube import YouTube
#
# def Download(link):
#     youtubeObject = YouTube(link)
#     youtubeObject = youtubeObject.streams.get_highest_resolution()
#     try:
#         youtubeObject.download()
#     except:
#         print("An error has occurred")
#     print("Download is completed successfully")
#
#
# link = input("Enter the YouTube video URL: ")
# Download(link)


from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=yhqYOUyfC8I")
# yt = yt.get('mp4', '720p')
YouTube("https://www.youtube.com/watch?v=yhqYOUyfC8I").streams.first().download("C:\\Users\\e010846\\PycharmProjects\\Proj1\\file")
# yt.download('c:')