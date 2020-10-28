# 需求 读取文件内容
# 注意：打开文件后，先实现关闭，再操作文件
# 1.打开文件
# open('文件路径/文件名.文件后缀')
# file = open('./demo.txt')
file = open('./demo.txt', encoding='utf-8')
# 2.读取文件内容
# 文件对象.read()
text = file.read()
print(text)
# 3.关闭文件
# 文件对象.close()
file.close()