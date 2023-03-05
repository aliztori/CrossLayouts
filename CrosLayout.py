from pyautogui import *
import clipboard
import json

def Copy(): hotkey('ctrl', 'c')
def Paste(): hotkey('ctrl', 'v')

def CrosLayout():
	
	JSONPATH = "T:/Programming/AutoHotkey/2.0/Support Files/CrossLayout.Json"
	with open(JSONPATH, 'r', encoding='utf-8-sig') as Jf:
		txt = Jf.read()
		
	KEYWORDS = json.loads(txt)['All']
	Copy()

	oldStr = clipboard.paste()

	newStr = ''
	for char in oldStr:
		try: 
			newStr = f"{newStr}{KEYWORDS[char]}"
		except KeyError:
			newStr = f"{newStr}{char}"


	clipboard.copy(newStr)
	Paste()

CrosLayout()
