
import json
import os
import pandas as pd
import pdb 
cwd = os.getcwd()
#data= pd.read_json('D:/Mtech/ML/Project/NBC/Naive-Bayes-Classifier-In-Python/smaple.json', lines=True)
pdb.set_trace()
data= pd.read_json('../smaple.json', lines=True)
#data= pd.read_json('D://Mtech//ML//Project//NBC//Naive-Bayes-Classifier-In-Python//smaple.json', lines=True)
#data= pd.read_json('../smaple.json', lines=True)

# basePath = os.path.dirname(os.path.abspath(__file__))
# print(basePath)
# path = basePath + '\smaple.json'
# print(path)
# df = pd.read_json(r'path', lines=True)

# with open('./smaple.json', encoding='utf-8-sig') as f_input:
#     print(f_input)
#     df = pd.read_json(f_input)

#df.to_csv('PeshVsQuetta.csv', encoding='utf-8', index=False)

#pd.read_json(open("./smaple.json", "r", encoding="utf8"),lines=True)
#df = pd.read_json('D:\\Mtech\\ML\\Project\\NBC\\Naive-Bayes-Classifier-In-Python\\smaple.json', lines=True, encoding='utf-8-sig')



#data= pd.read_json('./smaple.json', lines=True, orient='records')

#data= pd.read_json('./smaple.json', orient=str)