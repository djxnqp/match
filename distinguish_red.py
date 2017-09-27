#!/usr/bin/python
#-*-coding:utf-8-*-
import matplotlib.pyplot as plt
import csv
import string
import global_list
from utils import *


s90_x = []
s90d_y = []
s0 = []
s10 = []


sred_flag = []          #用于区分哪些是白细胞团，那些事嗜酸细胞

new1_csv_datalist = []  #新的csv文件数据列表



##数据预处理

printInfo("数据预处理开始")

csvFile = open(global_list.RAW_CSV_DIR, "r")
reader = csv.reader(csvFile)
i = 0;
for item in reader:                               
    if(i > 0):
       s90_int = string.atoi(item[2])
       s90d_int = string.atoi(item[3])
       s90_x.append(item[2])
       s90d_y.append(item[3])
       s0.append(item[0])
       s10.append(item[1])
       if((260 - s90d_int) < 225 or (260 - s90_int) < 60):
           sred_flag.append(1)
           global_list.RED_COUNT = global_list.RED_COUNT + 1
       else:
           sred_flag.append(0)
           global_list.CELL_GROUP_COUNT = global_list.CELL_GROUP_COUNT + 1
    i = i + 1

csvFile.close()

printInfo("数据预处理结束")

##将处理完的数据写入csv文件，便于下一阶段处理
printInfo("重写CSV文件开始")
csvFile2 = open(global_list.NEW_CSV_DIR,'w')
writer = csv.writer(csvFile2)
writer.writerow(["s0","s10","s90","s90d","red_flag"])
m = len(sred_flag)
for i in range(m):
        writer.writerow([s0[i],s10[i],s90_x[i],s90d_y[i],sred_flag[i]])

writer.writerow(["cell_group_count",global_list.CELL_GROUP_COUNT,"red_count",global_list.RED_COUNT,""])
csvFile2.close()
printInfo("重写CSV文件结束")



##绘图前的数据预处理

printInfo("绘图前数据预处理开始")
group_x = []
group_y = []


red_x = []
red_y = []


csvFile = open(global_list.NEW_CSV_DIR, "r")
reader = csv.reader(csvFile)
i = 0;
for item in reader:                               
    if(i > 0 and i < len(sred_flag) - 1):
        if(string.atoi(item[4]) == 1):
            red_x.append(item[2])
	    red_y.append(item[3])
	elif(string.atoi(item[4]) == 0):
	    group_x.append(item[2])
	    group_y.append(item[3])
    i = i + 1
    

csvFile.close()

printInfo("绘图前数据预处理结束")


#print len(red_x) + len(group_x)


printInfo("绘制嗜酸细胞和白细胞团图片开始")
#将分离后的数据绘制成图形
plt.figure(figsize=(8,6))
plt.scatter(red_x,red_y,s=10,c='red',marker='o',alpha=0.5,label='red')
plt.scatter(group_x,group_y,s=10,c='blue',marker='x',alpha=0.5,label='group')
plt.title('distinguish red')
plt.xlabel('S90')
plt.ylabel('S90d')
plt.legend(loc='upper right')
plt.show()

printInfo("关闭图片成功")





