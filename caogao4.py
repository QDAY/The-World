



'''
一段失败代码：目的如下：
对路径下的每个文件提取2-4列的数据，分别形成一个2维列表，最后输出一个三维列表L,
并输出路径下CSV文件名和该路径，返回列表namelist, pathlist
还不知道原因，先记下
'''
import os
import numpy as np
import csv
import pandas as pd
def tiqu_lie (path1):
    L=[]
    def get_content (pathhh):
        columns = ['time', 'x-axis', 'y-axis', 'z-axis']
        files = os.listdir(pathhh)
        for file in files:
            newdir = os.path.join(pathhh, file)
            if os.path.isfile(newdir):
                if os.path.splitext(newdir)[1] == '.csv':
                    df = pd.read_csv(newdir, header=None, names=columns)
                    xs = df['x-axis'].values[:]
                    ys = df['y-axis'].values[:]
                    zs = df['z-axis'].values[:]
                    L.append([xs, ys, zs])
        return

    def get_name_and_path(path):  # 获取CSV文件名和该路径，返回列表
        namelist = []
        pathlist = []
        for dirpaths, dirnames, filesnames in os.walk(path):
            for i in range(len(filesnames)):
                namelist.append(filesnames[i])
                pathlist.append(os.path.join(dirpaths, filesnames[i]))
        return namelist, pathlist
    get_content(path1)
    namelist, pathlist = get_name_and_path(path1)

    return L,namelist, pathlist