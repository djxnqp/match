#!/usr/bin/python
#-*-coding:utf-8-*-

##区分嗜酸细胞的全局变量

RAW_CSV_DIR = "CSV/rawDataCSV/2.csv" #原始csv文件目录
NEW_CSV_DIR = "CSV/resultCSV/distinguish_step1.csv" #第一步分类（白细胞团和嗜酸细胞的分离）后新生成csv文件路径

CELL_GROUP_COUNT = 0;  #分离后白细胞团的数量
RED_COUNT = 0;         #分离后嗜酸细胞的数量

##区分细胞团种类的全局变量

RAW_DATA_COUNT = 5000  #原始数据个数

BLUE_COUNT = 0         
GREEN_COUNT = 0
WHITE_COUNT = 0
PINK_COUNT = 0

RESULT_CSV_DIR = "CSV/resultCSV/result_step2.csv"


##cutToRedAndGrooup.py里面的全局变量(分离第一步得到的数据)
RED_CSV_DIR = "CSV/cutCSV/red.csv"    #嗜酸性细胞数据路径
GROUP_CSV_DIR = "CSV/cutCSV/group.csv"#白细胞团数据路径
