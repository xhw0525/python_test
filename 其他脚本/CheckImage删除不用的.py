# -*- coding: utf-8 -*-
import os
import re
import shutil

rootdir = '/Users/xhw/XcodeProjects/newDuiaApp/newDuiaApp'


def dirlist(path, allfile):
    filelist = os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)
        else:
            if len(os.path.splitext(filepath)) > 1 and (os.path.splitext(filepath)[1].__eq__(".xib")):
                allfile.append(filepath)

            if len(os.path.splitext(filepath)) > 1 and (os.path.splitext(filepath)[1].__eq__(".m")):
                allfile.append(filepath)
            if len(os.path.splitext(filepath)) > 1 and (os.path.splitext(filepath)[1].__eq__(".mm")):
                allfile.append(filepath)

    return allfile

list = dirlist(rootdir, [])

# print   list
strs = set()

for path in list:
    # print path
    file_1 = open(path,'r')
    file_1.readline()
    str = file_1.readline()
    while str:
        if  re.search('"([a-z_A-Z0-9\u4e00-\u9fa5.\.\--]+)"',str):
            img = re.search('"([a-z_A-Z0-9\u4e00-\u9fa5.\.\--]+)"',str).group(1)
            if img.endswith('.png'):
                img = img[0:len(img)-4]

            strs.add(img)
        str = file_1.readline()



rootimgdir = '/Users/xhw/XcodeProjects/newDuiaApp/newDuiaApp/Assets.xcassets/'

filehavelist = []
count = 0
def dirImagelist(path, allfile):
    filelist = os.listdir(path)
    global count

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if filename.endswith(".imageset"):

            imagName = os.path.splitext(filename)[0]

            if re.search('([0-9]+)', imagName):#不处理包含数字的 动画文件
                continue
            if strs.__contains__(imagName):
                # filehavelist.append(filepath)
                pass
            else: #不包含
                count = count + 1
                print  count , '不包含',imagName
                # shutil.move(filepath, "/Users/xhw/Desktop/delete_image/share/"+filename)
                pass

        elif os.path.isdir(filepath):
            dirImagelist(filepath,allfile)




        else:
            pass



dirImagelist(rootimgdir, [])

for havestr in filehavelist:
    print havestr
