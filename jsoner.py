import pandas as pd
import chardet

rawdata = open('merged.csv', 'rb').read()
result = chardet.detect(rawdata)
charenc = result['encoding']
print(charenc)

data = pd.read_csv("merged.csv", sep=";", encoding="ISO-8859-1")
data = data.drop(columns=["category"])
print(data)

data.insert(0, 'id', range(0, len(data)))

with open('kb.json', 'w', encoding='utf-8') as file:
	data.to_json(file, orient='records', force_ascii=False, index=True)



