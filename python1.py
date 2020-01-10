import os 


for i in range(1,11):
    command='you-get https://www.bilibili.com/video/av20858020?p=%d '%i
    r=os.system(command)
    if i==0:
        print('第%d集下载成功！%i')
    else:
        print('第%d集下载失败！%i')
