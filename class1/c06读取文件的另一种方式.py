# 前提：如果只是读取文件内容操作
# with open()
with open('./read_line.txt', encoding='utf-8') as text:
    print(text.read())