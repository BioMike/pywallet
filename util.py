def iais(a):
	if a>= 2:
		return 's'
	else:
		return ''

def systype():
	if platform.system() == "Darwin":
		return 'Mac'
	elif platform.system() == "Windows":
		return 'Win'
	return 'Linux'

def determine_db_dir():
	if wallet_dir in "":
		if platform.system() == "Darwin":
			return os.path.expanduser("~/Library/Application Support/Bitcoin/")
		elif platform.system() == "Windows":
			return os.path.join(os.environ['APPDATA'], "Bitcoin")
		return os.path.expanduser("~/.bitcoin")
	else:
		return wallet_dir

def determine_db_name():
	if wallet_name in "":
		return "wallet.dat"
	else:
		return wallet_name