pwd = 'a123456'
x = 3
pwd = input('請輸入密碼：')
while True:
	if pwd == 'a123456':
		print('登入成功')
		break
	else:
		print('密碼錯誤 還有', x ,'次機會')
		pwd = input('請輸入密碼：')
		x = x - 1
		if x <= 0:
			break