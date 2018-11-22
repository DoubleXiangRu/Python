'''
	功能：nonlocal 的使用方法
'''
def test():
	b=123
	global a
	def foo():
		nonlocal b	#必须在函数外定义过b才可以用nonlocal函数
		b=456
		print(b)
	foo()
	print(b)
test()