# *
'''扫描指定目录及其子目录下的指定类型的文件，生成index.html文件'''
#############################################################
import os
#############################################################
root_dir = os.getcwd()
kg = '&nbsp'  # html中的空格
#############################################################
html = os.path.dirname(__file__)+'\\index.html'


def txt(self_kg, self_path, text, self_lv):
    return self_kg+'<a href="'+self_path+'\\'+text+'">'+kg*(self_lv+1)*4+text+'</a><br>\n'


def mp4(self_kg, self_path, text, self_lv) -> str:
    t=self_kg+'<a>'+ text+'</a><br>\n'
    t = t+self_kg+'<video controls><br>\n'
    t = t+self_kg+'    <source src="'+self_path+'\\'+text+'" type="video/mp4"><br>\n'
    t = t+self_kg+'</video><br>\n'
    return t


class Item():
    def __init__(self, _path: str):
        self.path = _path
        self.child = []
        self.lv = len(_path.split('\\'))-len(root_dir.split('\\'))

    def kg(self, n=0):
        return '    '*(self.lv+n)

    def display(self):
        '''测试用'''
        print('f=', self.path)

    def write_one(self, text):
        f = open(html, 'a', encoding='utf-8')
        #text = txt(self.kg(1), self.path, text, self.lv)
        text = mp4(self.kg(1), self.path, text, self.lv)
        f.write(text)
        #f.write(self.kg(1)+'<a href="')
        # f.write(self.path+'\\'+text)
        # f.write('">')
        # f.write(kg*(self.lv+1)*4+text)
        # f.write('</a><br>\n')
        f.close()
        return self.path

    def write(self):
        folder = os.path.basename(self.path)
        f = open(html, 'a', encoding='utf-8')
        f.write(self.kg()+'<div>\n')
        f.write(self.kg(1)+'<a>'+kg*self.lv*4+'-'*20 + '</a><br>\n')
        f.write(self.kg(1)+'<a>'+kg*self.lv*4+folder +
                ' ' + kg*2 + ' >>>> </a><br>\n')
        f.close()
        for i in self.child:
            if type(i) == str:
                self.write_one(i)
        #########################################
        for i in self.child:
            if type(i) == Item:
                i.write()
        f = open(html, 'a', encoding='utf-8')
        f.write(self.kg()+'</div>\n')
        f.close()
# <a href="https://www.runoob.com/">访问菜鸟教程!</a>


def get_file_list(_dir: str) -> None:
    '''获取目录下的文件列表，包括文件夹内的文件'''
    item = Item(_dir)
    for i in os.listdir(_dir):
        p = _dir+'\\'+i
        if os.path.isfile(p):
            item.child.append(i)
        elif os.path.isdir(p):
            item.child.append(get_file_list(p))
        else:
            print('出现错误，获取文件列表出错   ', item.path)
            print('错误文件', i)
    return item


print('=='*20)
print('already get file list')
print('=='*20)

if os.path.exists(html):
    os.remove(html)

myfile = get_file_list(root_dir)
myfile.write()
