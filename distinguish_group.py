#!/usr/bin/python
#-*-coding:utf-8-*-
import matplotlib.pyplot as plt
import csv
import string
import global_list
from utils import *

#红色的横纵坐标
s90_x_red = []
s0_y_red  = []
s10_y_red = []


#绿色的横纵坐标
s90_x_green = []
s0_y_green  = []
s10_y_green = []

#粉色的横纵坐标
s90_x_pink = []
s0_y_pink  = []
s10_y_pink = []


#蓝色的横纵坐标
s90_x_blue = []
s0_y_blue  = []
s10_y_blue = []


#白色的横纵坐标
s90_x_white = []
s0_y_white  = []
s10_y_white = []


##数据预处理
printInfo("数据预处理开始")
csvFile = open(global_list.NEW_CSV_DIR, "r")
reader = csv.reader(csvFile)
i = 0 #去除第一行和最后一行

for item in reader:                               
    if(i > 0 and i < global_list.RAW_DATA_COUNT + 1):  #分类数据
        if(string.atoi(item[4]) == 0):                 #只要白细胞团
            if(string.atoi(item[0]) < 70 and string.atoi(item[1]) < 50 and string.atoi(item[2]) < 30): #淋巴细胞团
                s90_x_green.append(item[2])
                s0_y_green.append(item[0])
                s10_y_green.append(item[1])
                global_list.GREEN_COUNT = global_list.GREEN_COUNT + 1
            elif(string.atoi(item[0]) > 70 and string.atoi(item[1]) > 50 and string.atoi(item[1]) < 70 and string.atoi(item[2]) > 30 and string.atoi(item[2]) < 50):
                s90_x_pink.append(item[2])
                s0_y_pink.append(item[0])
                s10_y_pink.append(item[1])
                global_list.PINK_COUNT = global_list.PINK_COUNT + 1
            elif(string.atoi(item[0]) > 70 and string.atoi(item[1]) > 70 and string.atoi(item[2]) > 50):
                s90_x_blue.append(item[2])
                s0_y_blue.append(item[0])
                s10_y_blue.append(item[1])
                global_list.BLUE_COUNT = global_list.BLUE_COUNT + 1
            else:
                s90_x_white.append(item[2])
                s0_y_white.append(item[0])
                s10_y_white.append(item[1])
                global_list.WHITE_COUNT = global_list.WHITE_COUNT + 1
	elif(string.atoi(item[4]) == 1):
	   s90_x_red.append(item[2])
           s0_y_red.append(item[0])
           s10_y_red.append(item[1])             
		
    if(i == global_list.RAW_DATA_COUNT + 1):           #获取最后一行数据（白细胞团的数量和嗜酸细胞的数量）
        global_list.CELL_GROUP_COUNT = item[1] 
        global_list.RED_COUNT = item[3]
    i = i + 1

csvFile.close()
printInfo("数据预处理结束")


'''
## 打印细胞种类的数目
printInfo("打印分类结果开始")
print {
	"total_cells_num" : string.atoi(global_list.RED_COUNT) + global_list.GREEN_COUNT + global_list.PINK_COUNT + global_list.BLUE_COUNT + global_list.WHITE_COUNT, 
	"red_cell_num" :  global_list.RED_COUNT,
	"green_cell_num" : global_list.GREEN_COUNT,
	"pink_cell_num" : global_list.PINK_COUNT,
	"blue_cell_num" : global_list.BLUE_COUNT,
	"white_cell_num" : global_list.WHITE_COUNT 
}
printInfo("打印分类结果结束")
'''


##将统计完的数据写入csv文件，
printInfo("写CSV文件开始")
global_list.RAW_DATA_COUNT = string.atoi(global_list.RED_COUNT) + global_list.GREEN_COUNT + global_list.PINK_COUNT + global_list.BLUE_COUNT + global_list.WHITE_COUNT
csvFile2 = open(global_list.RESULT_CSV_DIR,'w')
writer = csv.writer(csvFile2)
writer.writerow(["项目","结果","参考范围"])
writer.writerow(["白细胞总数(WBC)",global_list.RAW_DATA_COUNT,"10.00 ~ 4.00"])
writer.writerow(["淋巴细胞比率(LYM%)",round(global_list.GREEN_COUNT/float(global_list.RAW_DATA_COUNT),2),"40.00 ~ 20.00"])
writer.writerow(["单核细胞比率(MON%)",round(global_list.PINK_COUNT/float(global_list.RAW_DATA_COUNT),2),"10.00 ~ 3.00"])
writer.writerow(["中性粒细胞比率(NEU%)",round(global_list.BLUE_COUNT/float(global_list.RAW_DATA_COUNT),2),"70.00 ~ 50.00"])
writer.writerow(["嗜酸性粒细胞比率(EOS%)",round(int(global_list.RED_COUNT)/float(global_list.RAW_DATA_COUNT),2),"5.00 ~ 0.50"])
writer.writerow(["嗜碱性粒细胞比率(BASO%)",round(global_list.WHITE_COUNT/float(global_list.RAW_DATA_COUNT),2),"1.00 ~ 0.00"])


writer.writerow(["淋巴细胞值(LYM#)",global_list.GREEN_COUNT,str(int(round(global_list.RAW_DATA_COUNT * 0.4))) + " ~ " + str(int(round(global_list.RAW_DATA_COUNT * 0.2)))])
writer.writerow(["单核细胞值(MON#)",global_list.PINK_COUNT,str(int(round(global_list.RAW_DATA_COUNT * 0.1))) + " ~ " + str(int(round(global_list.RAW_DATA_COUNT * 0.03)))])
writer.writerow(["中性粒细胞值(NEU#)",global_list.BLUE_COUNT,str(int(round(global_list.RAW_DATA_COUNT * 0.7))) + " ~ " + str(int(round(global_list.RAW_DATA_COUNT * 0.5)))])
writer.writerow(["嗜酸性粒细胞值(EOS#)",global_list.RED_COUNT,str(int(round(global_list.RAW_DATA_COUNT * 0.05))) + " ~ " + str(int(round(global_list.RAW_DATA_COUNT * 0.005)))])
writer.writerow(["嗜碱性粒细胞值(BASO#)",global_list.WHITE_COUNT,str(int(round(global_list.RAW_DATA_COUNT * 0.01))) + " ~ " + "0"])





csvFile2.close()
printInfo("写CSV文件结束")



##画出s90 - s0 坐标图
printInfo("绘制 S90 - S0 分类结果开始")

plt.figure(figsize=(8,6))
plt.scatter(s90_x_red,s0_y_red,s=3,c='red',marker='o',alpha=0.5,label='red')
plt.scatter(s90_x_green,s0_y_green,s=3,c='green',marker='o',alpha=0.5,label='green')
plt.scatter(s90_x_pink,s0_y_pink,s=3,c='pink',marker='o',alpha=1,label='pink')
plt.scatter(s90_x_blue,s0_y_blue,s=3,c='blue',marker='o',alpha=0.5,label='blue')
plt.scatter(s90_x_white,s0_y_white,s=3,c='white',marker='o',alpha=0.5,label='white')
plt.title('distinguish group')
plt.xlabel('S90')
plt.ylabel('S0')
plt.legend(loc='upper left')
plt.show()

printInfo("关闭 S90 - S0 分类结果图片")



##画出s90 - s10 坐标图
printInfo("绘制 S90 - S10 分类结果开始")

plt.figure(figsize=(8,6))
plt.scatter(s90_x_red,s10_y_red,s=3,c='red',marker='o',alpha=0.5,label='red')
plt.scatter(s90_x_green,s10_y_green,s=3,c='green',marker='o',alpha=0.5,label='green')
plt.scatter(s90_x_pink,s10_y_pink,s=3,c='pink',marker='o',alpha=1,label='pink')
plt.scatter(s90_x_blue,s10_y_blue,s=3,c='blue',marker='o',alpha=0.5,label='blue')
plt.scatter(s90_x_white,s10_y_white,s=3,c='white',marker='o',alpha=0.5,label='white')
plt.title('distinguish group')
plt.xlabel('S90')
plt.ylabel('S10')
plt.legend(loc='upper left')
plt.show()

printInfo("关闭 S90 - S10 分类结果图片")










