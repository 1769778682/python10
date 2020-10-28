# 1.导包
import json

dict_data = {'name': '刘备', 'age': 45, 'title': True, 'son': None}

with open('./json_data.json', 'w', encoding='utf-8') as f:
    json.dump(dict_data, f)


# "\u5218\u5907" 这是unicode编码的中文字符，不是乱码