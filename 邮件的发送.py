import smtplib

from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def add_attachment(file):
	with open("test.txt",'r') as fp:
		mime=MIMEBase('application','octect-string',filename=file)
		mime.add_header("Content-Disposition",'attachment',filename=file)
		mime.add_header("Content-ID","<0>")
		mime.add_header("X-attachment-Id","0")
		mime.set_payload(fp.read())
		encoders.encode_base64(mime)
		att_msg.attach(mime)

from_addr ="1171899614@qq.com" 
to_addr = "1171899614@qq.com"
psw='sxrcbxcqldosgbej'
smtp_server="smtp.qq.com"#  这个应该是路径

#创建邮件正文对象
contents = "Hello world!"	#项目内容
msg=MIMEText(contents,'plain','utf-8')	#文件格式

#创建一个带有附件的邮件对象
att_msg=MIMEMultipart()
msg['From'],msg['To'] = from_addr,to_addr	#定义发件人和收件人
msg['Subject']="Test"	#项目名

att_msg.attach(msg)	#见正文添加到带附件的邮件中

#批量添加附件
att =["test.txt","test2.txt"]
for a in att:
	add_attachment(a)

server=smtplib.SMTP(smtp_server,25)
server.login(from_addr,psw)
server.sendmail(from_addr,to_addr,att_msg.as_string())
server.quit()	#退出服务器

#"192.168.20.2:500"#后面的这个：500是套接字
