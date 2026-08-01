class FileUtils:
    """
    文件操作函数
    """


    def read_file(file_path):
        """
        测试代码
        from my_func.FileUtils import FileUtils

        res = FileUtils.read_file('pycharm.txt')
        print(res)
        """
        with open(file_path,'r',encoding='utf-8') as f:
            content = f.read()
        return content