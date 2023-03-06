import json

def load_json(name):
    with open(name, "r", encoding="utf-8-sig") as f:
        a = json.load(f)
    return a

class CrosLayouts:

	JSONPATH = "CrossLayouts.Json"
	
	FATOENG: dict = load_json(JSONPATH)["English"]
	ENGTOFA: dict = load_json(JSONPATH)["Persian"]
	ALL: dict = load_json(JSONPATH)["All"]

	@classmethod
	def ConvertToOpposite(cls, Text: str) -> str:
		Text.replace("ریال", "R")

		newText = ""
		for char in Text:
			newText = f"{newText}{cls.ALL.get(char, char)}"

		return newText

	@classmethod
	def ConvertToEnglish(cls, Text: str) -> str:
		Text.replace("ریال", "R")

		newText = ""
		for char in Text:
			newText = f"{newText}{cls.FATOENG.get(char, char)}"
		    
		return newText

	@classmethod
	def ConvertToPersian(cls, Text: str) -> str:
		newText = ""
	    
		for char in Text:
			newText = f"{newText}{cls.ENGTOFA.get(char, char)}"

		return newText

# Example:
print(CrosLayouts.ConvertToOpposite('شمه'))
