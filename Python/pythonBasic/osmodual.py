import os
import re

#重命名单个文件夹下的文件
path = "I:\Programming\二分查找"
for f in os.listdir(path):
    #如果同一目录下同时有文件和文件夹
    if os.path.isdir(os.path.join(path, f)):
        continue
    fname = os.path.splitext(f)[0]
    suffix = os.path.splitext(f)[1]
    fname = fname.replace('.','').replace(' ','')
    idx = re.match('\d+',fname).group(0).zfill(4)
    newfname = re.sub('\d+',idx,fname,count=1)
    os.rename(os.path.join(path,f), os.path.join(path,newfname+suffix))

#重命名多个文件夹下的文件
path = "I:\Programming"
for dir in os.listdir(path):
    if dir.startswith('.'):
        continue
    for file in os.listdir(os.path.join(path,dir)):
        fname = os.path.splitext(file)[0]
        suffix = os.path.splitext(file)[1]
        fname = fname.replace('.','').replace(' ','')
        idx = re.match('\d+',fname).group(0).zfill(4)
        newfname = re.sub('\d+',idx,fname,count=1)
        os.rename(os.path.join(path,dir,file), os.path.join(path,dir,newfname+suffix))


# s = "81. 搜索旋转排序数组 II.py"
# s = s.replace(' ','')
# digi = re.match('\d+',s).group(0).zfill(4)
# res = re.sub('\d+\.',digi,s,count=1)
# print(res)