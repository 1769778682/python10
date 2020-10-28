# 1.打开文件
file_read = open('./read_line.txt', encoding='utf-8')
file_write = open('./read_line_副本.txt', 'w', encoding='utf-8')

while True:
    text = file_read.readline()
    if not text:
        break

    file_write.write(text)
    print(text, end='')

# 关闭文件
file_read.close()
file_write.close()