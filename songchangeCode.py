import requests
#调用requests库
import json
#调用json库
url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
headers={
    'referer':'https://y.qq.com/portal/search.html',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
#标记了请求从什么设备什么浏览器发出
}
#伪装请求头
singer=input('你喜欢的歌手是？')
#输入喜欢的歌手
for x in range(5):
    params={
    'ct':'24',
    'qqmusic_ver': '1298',
    'new_json':'1',
    'remoteplace':'sizer.yqq.lyric_next',
    'searchid':'94267071827046963',
    'aggr':'1',
    'cr':'1',
    'catZhida':'1',
    'lossless':'0',
    'sem':'1',
    't':'7',
    'p':str(x+1),
    'n':'10',
    'w':singer,
    'g_tk':'1714057807',
    'loginUin':'0',
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'utf-8',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0'
    }
    #将参数封装成字典
    res=requests.get(url,params=params)
    #获取数据，下载该字典
    json_music=res.json()
    #使用json方法，将response对象，转为字典/列表
    list_music=json_music['data']['lyric']['list']
    #一层一层取字典获取歌单列表
    for music in list_music:
        print('歌曲名'+music['name'])
        #打印歌曲名
        print('专辑'+music['album']['name'])
        #打印专辑名
        print('播放时长：'+str(music['interval'])+'秒')
        #打印播放时长
        print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid'] +'.html\n\n')
        #打印播放链接