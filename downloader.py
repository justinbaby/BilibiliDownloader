#coding:utf-8
import os
import sys
import urllib.request
import http.cookiejar
import re
import random

av='7333931'#此处为下载视频av号
def download(nr):
	def report(count, blockSize, totalSize):
		percent = int(count*blockSize*100/totalSize*100)/100
		lpercent=int(percent/2)
		finish = str(count*blockSize/1024/1024)[0:5]+"MB"
		total=str(totalSize/1024/1024)[0:5]+"MB"
		sys.stdout.write("\r%.2f%%" % percent+'  '+finish+'/'+total+'['+lpercent * '-'+(50-lpercent)*' '+']')
		sys.stdout.flush()
	url = 'http://www.bilibilijj.com/video/av'+nr+'/'
	opener = urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04')]
	u=opener.open(url).read().decode()#获取bilibilijj界面
	bg=u.find('/DownLoad/Cid/')
	ed=u.find('\' target',bg)
	durl='http://www.bilibilijj.com'+u[bg:ed]+'?t='+str(random.uniform(0,1))#获取全是广告的下载页面
	u=opener.open(durl).read().decode()
	durl=re.search('<a href="http://.+" target="_blank" download=',u).group(0)[9:-27]#获取下载地址
	durl=durl.replace('&amp;','&')
	opener = urllib.request.build_opener()
	opener.addheaders = [('Host' , '219.138.27.30'),
						('User-Agent' , 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04'),
						('Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
						('Accept-Language' , 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
						('Accept-Encoding' , 'gzip, deflate'),
						('DNT' , '1'),
						('Connection' , 'keep-alive'),
						('Upgrade-Insecure-Requests' , '1')]
	urllib.request.urlretrieve(durl,nr+'.flv',report)
download(av)
os.popen(sys.path[0]+'\\ffmpeg.exe -y -i '+av+'.flv '+av+'.mp4')