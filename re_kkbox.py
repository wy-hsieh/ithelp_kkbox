import requests
import json
import time
import csv
from bs4 import BeautifulSoup

# kkbox 華語新歌日榜，category=297
# kkbox 西洋新歌日榜，category=390
# kkbox 日語新歌日榜，category=308
# kkbox 韓語新歌日榜，category=314
# kkbox 台語新歌日榜，category=304
# kkbox 粵語新歌日榜，category=320
url = "https://kma.kkbox.com/charts/api/v1/daily?category=320&lang=tc&limit=50&terr=tw&type=newrelease"

# 取得歌曲資訊 json 檔
response = requests.get(url)

# 將 json 轉為 python 的 dictionary
data = json.loads(response.text)

# 取得歌單
song_list = data["data"]["charts"]["newrelease"]


# 儲存成 csv 檔
with open('songs.csv', 'w', newline='', encoding="utf-8") as csvfile:
  # 建立 CSV 檔寫入器
  writer = csv.writer(csvfile)

  # 寫入一列資料
  writer.writerow(["排名", "歌名", "作者", "發行日期", "連結"])

  for song in song_list:
    song_rank = song["rankings"]["this_period"]
    song_name = song["song_name"]
    song_url = song["song_url"]
    song_artist = song["artist_name"]
    song_timestamp = int(song["release_date"])
    # 從 timestamp 轉為日期格式
    song_date = time.strftime("%Y-%m-%d", time.localtime(song_timestamp))

    # # 取得歌詞
    # song_response = requests.get(song_url)
    # result = BeautifulSoup(song_response.text, "html.parser")
    # lyric = result.find("div", class_ = "lyrics").text

    # print("歌詞", lyric )
    # print("排名", song_rank)
    # print("歌名", song_name)
    # print("連結", song_url)
    # print("作者", song_artist)
    # print("發行日期", song_date)
    # print("-" * 30)
    
    # 寫入資料
    writer.writerow([song_rank, song_name, song_artist, song_date, song_url])

print("完成")


