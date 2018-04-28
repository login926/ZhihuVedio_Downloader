import requests
import json
import re
import os
from prettytable import PrettyTable

headers = {'Authorization':'oauth c3cef7c66a1843f8b3a9e6a1e3160e20','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
print("输入知乎回答链接")
AnswerURL = input()
AnswerReq = requests.get(AnswerURL,headers=headers)
VideoID = re.findall(r'(?<=zhihu\.com\/video/).*?(?=\" target)',AnswerReq.text)[0]
VideoPlaylistURL = 'https://lens.zhihu.com/api/videos/' + str(VideoID)
print(VideoPlaylistURL)
VideoPlaylistReq = requests.get(VideoPlaylistURL,headers=headers)
VideoPlaylist = VideoPlaylistReq.json()
VedioId = 0
DownloadURLList = []
Row = PrettyTable()
Row.field_names = [" 视频质量 "," 分辨率 "," 下载ID "]
for VideoQuality in VideoPlaylist['playlist']: 
    DownloadURLList.append(VideoPlaylist['playlist'][VideoQuality]['play_url'])
    VedioRatio = str(VideoPlaylist['playlist'][VideoQuality]['width'])+ 'P'
    Row.add_row([VideoQuality,VedioRatio,VedioId])
    VedioId = VedioId + 1
print(Row) 
print('输入下载ID') 
DownloadURL = ''
while True:
    try:
        SelectNum = int(input())
    except:
        print('无效输入')
        continue
    if (SelectNum < 0 or SelectNum > VedioId):
        print('无效输入')
        continue
    else:
         if (SelectNum == 0):
            print('0')
            DownloadURL = DownloadURLList[0]
            break
         elif (SelectNum == 1):
            DownloadURL = DownloadURLList[1]
            break
         elif (SelectNum == 2):
            DownloadURL = DownloadURLList[2]
            break
command = 'ffmpeg -i '+ '"'+ DownloadURL + '"' + ' -c copy output.mp4'
print(command)
os.system(command)
print('下载完成')