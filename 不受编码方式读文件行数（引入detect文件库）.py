
from chardet import detect

count,blanks=0,0

#进行探测
with open("a.txt",'rb') as fp:	#'rb'以二进制编码
	#测试文件编码，编码信息保存到code中
	code=detect(fp.read())['encoding']
	print(code)	#detect 是以一个字典序，保存的是文件的保存信息

#引用第三方库：chardet

# pip install chardet   导入第三方库的方法，在命令提示符中导入

with open("a.txt","r",encoding=code) as fp:	#encoding 得到编码方式名  r是一种读模式
	while True:
		line = fp.readline()	#readline读一行
		if not line:
			break 
		if len(line.strip())==0:	#判断空白行
			blanks+=1;		#得到空白行个数
		#print(len(line.strip()))	#line.strip()得到真正意义上的空白行(空格、换行符)
		count+=1;
print(count,blanks)