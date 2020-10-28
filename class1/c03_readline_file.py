# 1.打开文件
file = open('read_line.txt', encoding='utf-8')
# 2.读取文件
# 由于内容不确定有几行，所以使用死循环
while True:
    # 该方法调用1次，只读取1行内容，因此，需要使用循环
    text = file.readline()
    # 添加判断条件，是否还有内容，如果没有结束循环
    if not text:  # 如果没有内容
        break
    # print()会自带自动换行效果
    print(text, end='')
# 3.关闭文件
file.close()