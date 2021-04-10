import zipfile as zp

target = 'target.zip'
wordList = 'word-list.txt'

with open(wordList, mode='rb') as f:
	listPassword = f.readlines()
	for password in listPassword:
		try:
			with zp.ZipFile(target, 'r') as f:
				f.extractall(pwd=password.strip())
			print('Password Found >> ['+str(password.strip().decode('utf8'))+']')
			break
		except:
			print('Password ['+str(password.strip().decode('utf8'))+'] Wrong!!!')