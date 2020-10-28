# 1.打开文件
file_read = open('./demo.txt', encoding='utf-8')
file_write = open('./demo_副本.txt', 'w', encoding='utf-8')
# 2.读取原文件
text = file_read.read()
file_write.write(text)

# 关闭文件
file_read.close()
file_write.close()

