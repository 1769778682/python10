# 1.打开文件

file = open('./data.txt', 'w', encoding='utf-8')
# 写入文件
file.write('空山新雨后，\n')
file.write('天气晚来秋')
# 关闭文件
file.close()

# 打开文件
file1 = open('./data.txt', encoding='utf-8')
# 读取文件
text = file1.read()
print(text)
# 关闭文件
file1.close()

# 打开文件
file2 = open('./data.txt', 'a', encoding='utf-8')
