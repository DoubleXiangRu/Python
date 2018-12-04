#文件只可以保存在文件的根目录中（此方案）
import os
root_path = os.getcwd()
offset = len(root_path.split("\\"))

for root,dirs,files in os.walk(root_path):
	current_dir = root.split("\\")
	indent = len(current_dir)-offset
	print("\t"*indent,current_dir[-1])

	for f in files:
		print("\t"*(indent+1)+f)