import os

class FileUtils:
    """
    文件操作工具类
    提供常用的文件读写功能
    """


    def read_file(file_path):
        """
        读取文件功能

        测试代码
        from my_func.FileUtils import FileUtils

        res = FileUtils.read_file('pycharm.txt')
        print(res)
        """
        with open(file_path,'r',encoding='utf-8') as f:
            content = f.read()
        return content


    def write_file(file_path,content):
        """

        写入文件（覆盖原有内容）
        from my_func.FileUtils import FileUtils

        FileUtils.write_file('111.txt','我改完了哦')
        """

        with open(file_path,'w',encoding='utf-8') as f:
            f.write(content)
        print("写入成功！")




    def append_file(file_path,content):
        """
        追加内容到文件末尾
        测试代码
        from my_func.FileUtils import FileUtils

        res3 = FileUtils.append_file('111.txt',"我是新来的哦\n")
        print(res3)
        res4 = FileUtils.read_file('111.txt')
        print(res4)

        """

        with open(file_path,'a',encoding='utf-8') as f:
            f.write(content)
        return content


    def exists(file_path):
        """
        检查文件是否存在
        测试代码
        from my_func.FileUtils import FileUtils
        if FileUtils.exists(input()):
            print("文件存在")
        else:
            print("文件不存在")

        """

        return os.path.exists(file_path)
