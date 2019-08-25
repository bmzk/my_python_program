'''如果文件名包含 指定字符,则将其移动到上一级目录中'''
mystr=''

mypath="D:\\KwDownload"


import os

os.chdir(path)
os.getcwd()

#os.path.dirname(path)


def get_all_files(mydir):
    '''python 获取文件夹下所有文件包含子目录文件'''
    files_ = []
    mylist = os.listdir(mydir)
    for i in range(0, len(mylist)):
        path = os.path.join(mydir, list[i])
        if os.path.isdir(path):
            files_.extend(get_all_files(path))
        if os.path.isfile(path):
            files_.append(path)
    return files_

get_all_files(mypath)
mydir="D:\\KwDownload"