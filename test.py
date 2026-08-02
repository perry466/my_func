from my_func.FileUtils import FileUtils

# res = FileUtils.read_file('test.py')
#print(res)

# res2 = FileUtils.write_file('111.txt','我改完了哦')
# print(res2)

# res3 = FileUtils.append_file('111.txt',"我是新来的哦\n")
# print(res3)
# res4 = FileUtils.read_file('111.txt')
# print(res4)

# from my_func.FileUtils import FileUtils
# if FileUtils.exists(input()):
#
#     print("文件存在")
# else:
#     print("文件不存在")

from my_func.FileUtils import FileUtils

res = FileUtils.write_file("111.txt","我是高手")