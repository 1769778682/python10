# 1.导包
import json

with open('./json_data.json', encoding='utf-8') as f:
    data = json.load(f)
    print(data)


# 注意：解析JSON文件，返回数据类型为字典

print(type(data))

for i in data.items():
    print(i)

