#國家考駕照年齡問題
country = input('請輸入你的國家: ')
age = input('請輸入你的年齡: ')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不可以考駕照')
