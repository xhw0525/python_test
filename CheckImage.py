# -*- coding: utf-8 -*-
import os
import re
import shutil

rootdir = '/Users/xhw/XcodeProjects/DPSDKDemo/DPSDKKIT/Kit/'


def dirlist(path, allfile):
    filelist = os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)
        else:
            if len(os.path.splitext(filepath)) > 1 and (os.path.splitext(filepath)[1].__eq__(".xib"))  :
                allfile.append(filepath)
    return allfile

list = dirlist(rootdir, [])
strs = set()
for path in list:
    # print path
    file_1 = open(path,'r')
    file_1.readline()
    str = file_1.readline()
    while str:
        if  re.search('@"([a-z_A-Z0-9\u4e00-\u9fa5.-]+)"',str):
            img = re.search('@"([a-z_A-Z0-9\u4e00-\u9fa5.-]+)"',str).group(1)
            strs.add(img)
        # print strs
        str = file_1.readline()


    # break
print strs


rootdir = '/Users/xhw/XcodeProjects/newDuiaApp/newDuiaApp/Assets.xcassets'


def dirImagelist(path, allfile):
    filelist = os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirImagelist(filepath, allfile)
            if filename.endswith(".imageset"):
                imagName = os.path.splitext(filename)[0]
                for str in strs:
                    if str == imagName:
                        print imagName
                        if not os.path.exists("/Users/xhw/Desktop/Assets.xcassets/"+filename):
                            shutil.copytree(filepath, "/Users/xhw/Desktop/Assets.xcassets/"+filename)
                    if str == 'dp_'+imagName:
                        print imagName
                        if not os.path.exists("/Users/xhw/Desktop/Assets.xcassets/" + 'dp_'+filename):
                            shutil.copytree(filepath, "/Users/xhw/Desktop/Assets.xcassets/" + 'dp_' + filename)
        else:
                pass
    return allfile
imagelist = dirImagelist(rootdir, [])