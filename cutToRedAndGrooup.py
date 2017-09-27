#!/usr/bin/python
#-*-coding:utf-8-*-
import matplotlib.pyplot as plt
import csv
import string
import global_list
from utils import *


printInfo("数据预处理开始")
csvFile = open(global_list.NEW_CSV_DIR, "r")
reader = csv.reader(csvFile)
i = 0 #去除第一行和最后一行
group = []
red = []
for item in reader:                               
    if(i > 0 and i < global_list.RAW_DATA_COUNT + 1):  #分类数据
        if(string.atoi(item[4]) == 0):                 #只要白细胞团
	    group.append([item[0],item[1],item[2],item[3]])           
	elif(string.atoi(item[4]) == 1):
	    red.append([item[0],item[1],item[2],item[3]])       
    i = i + 1
csvFile.close()
printInfo("数据预处理结束")



##将处理完的数据写入csv文件

#分离白细胞团文件

printInfo("将白细胞团数据导入CSV文件开始")
csvFile2 = open(global_list.GROUP_CSV_DIR,'w')
writer = csv.writer(csvFile2)
writer.writerow(["s0","s10","s90","s90d"])
for i in group:
    writer.writerow(i)
csvFile2.close()
printInfo("将白细胞团数据导入CSV文件结束")



#分离嗜酸细胞文件
printInfo("将嗜酸细胞数据导入CSV文件开始")
csvFile2 = open(global_list.RED_CSV_DIR,'w')
writer = csv.writer(csvFile2)
writer.writerow(["s0","s10","s90","s90d"])
for i in red:
    writer.writerow(i)
csvFile2.close()
printInfo("将嗜酸细胞数据导入CSV文件结束")

