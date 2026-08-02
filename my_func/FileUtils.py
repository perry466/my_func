class FileUtils:
    """
    文件操作函数
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

        res2 = FileUtils.write_file('111.txt','我改完了哦')
        print(res2)
        """

        with open(file_path,'w',encoding='utf-8') as f:
            context = f.write(content)
        return content