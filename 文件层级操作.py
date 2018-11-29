import os
root_path=os.getcwd()
offset=len(root_path.split("\\"))

print(root_path)
for root,dirs,flies in os.walk(root_path):
	current_dir=root
	path_list=current_dir.split("\\")
	indent_level=len(path_list)-offset
	print("\t"*indent_level,"\\"+path_list[-1])
	#print(dirs)
	for f in flies:
		file_name=os.path.splitext(f)[0]
		print("\t"*(indent_level+1),file_name)#文件名与扩展名分离
