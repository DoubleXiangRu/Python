'''
	功能：python中函数之间是地址的交换
'''
def add(x,y):
	print(id(x),id(y))
	x=2
	y=6
	print(id(x),id(y))
	return x+y
a=1
b=2
print(id(a),id(b))
add(a,b)
print(add(a,b))