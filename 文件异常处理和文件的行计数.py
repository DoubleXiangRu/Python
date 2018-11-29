'''
	功能：异常处理
'''
#file_path=r'C:\Users\Administrator\Desktop\root\dir1\cp3_data_size.c'
# try:
# 	f=open(file_path)
# 	#open("a.txt")
# except:
# 	print("No such file or directory!")
# finally:#最终处理块
# 	print("File closed!")

#自动抛出异常
# with open(file_path) as f:
# 	pass

#对文件行计数
file_path=r'C:\Users\Administrator\Desktop\root\dir1\cp3_data_size.c'
def line_count(file_path):
	code_line,blank_line=0,0
	with open(file_path,'r') as fp:		#r读模式
		while True:
			line=fp.readline()
			if not line:				#不是一行
				break
			else:
				code_line+=1			#得到文件行数
			print(line)
	print(code_line,"lines")
line_count(file_path)

