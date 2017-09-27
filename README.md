白细胞亚群分类算法的设计
====================
使用
--------------------
>`usage`:python [infile] [step1|step2|cutforstep1]
>>`example1`:python main.py step1 (分离出嗜酸性细胞和白细胞团并画图)<br>
>>`example2`:python main.py step2 (分离出其他种类的细胞并画s90 - s0，s90 - s10坐标图)<br>
>>`example3`:python main.py cutforstep1(将第一步得到的两类数据分成两个文件)<br>

目录结构
--------------------
>`main.py` (程序入口文件)<br>
>`global_list.py` (用来设置一些全局变量的文件)<br>
>`utils.py` (工具类文件)<br>
>`distinguish_red.py` (第一步处理的文件)<br>
>`distinguish_group.py` (第二步处理的文件)<br>
>`cutToRedAndGrooup.py` (将第一步得到的两类数据分成两个文件)<br>
>`CSV`<br>
>>`rawDataCSV` (原始数据 [1-5].csv)<br>
>>`resultCSV` (第一步和第二部得到的数据统计[distinguish_step1.csv,result_step2.csv])<br>
>>`cutCSV` (example3得到的两个文件[group.csv,red.csv])<br>

依赖
---------------------
* python环境


运行系统
---------------------
* windows
* linux 


所需要的包
---------------------
* numpy<br>
* matplotlib<br>
* csv<br>

