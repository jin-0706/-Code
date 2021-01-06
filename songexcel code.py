import openpyxl
#调用openpyxl
import requests
#调用requests库
wb=openpyxl.Workbook()
#创新新的Excel表格
sheet=wb.active
#获取工作簿的活动表
sheet.title='music'
#给工作簿重命名
sheet['A1']='歌曲名'
#往A1的表格中写入歌曲名
sheet['B1']='所属专辑'
#往B1的表格中写入所属专辑
sheet['C1']='播放时长'
#往C1的表格中写入播放时长
sheet['D1']='播放链接'
#往D1的表格中写入播放链接
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
headers={
    'referer':'https://y.qq.com/portal/search.html',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
#标记了请求从什么设备什么浏览器发出
}
#伪装请求头
for x in range(5):
    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'sizer.yqq.song_next',
        'searchid': '64405487069162918',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(x+1),
        'n': '20',
        'w': '周杰伦',
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }
    #将参数封装成字典
    res_music=requests.get(url,params=params)
    #获取字典
    json_music=res_music.json()
    #以json的方法将res转为字典/列表
    list_music=json_music['data']['song']['list']
    #一层一层爬取字典
    for music in list_music:
        #提取
        name=music['name']
        album=music['album']['name']
        time=music['interval']
        link='https://y.qq.com/n/yqq/song/'+str(music['file']['media_mid'])+'.html\n\n'
        sheet.append([name,album,time,link])
        #以列表的形式加入表格
        print('歌曲名：'+name+'\n'+'所属专辑:'+album+'\n'+'播放时长:'+str(time)+'\n'+'播放链接:'+url)
        #打印结果
        wb.save('周杰伦.xlsx')
        #重命名表格