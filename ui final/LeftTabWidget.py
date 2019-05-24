#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: jyroy
import sys
import os
import regex as re
import time
from PyQt5.QtCore import QUrl,QRegExp
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QListWidget,QStackedWidget
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QColor,QFont
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
import qtawesome
from PyQt5.QtGui import QRegExpValidator,QDoubleValidator

free_walk_cmd = "roslaunch my_vel_package my_vel.launch"
config_path = "/home/robot/catkin_ws/src/my_vel_package/src/config.txt"
vel_config = r"^#define vel ((0)|(0\.[0-9])|(1)|(1\.0))\n$"
time_config = r"^#define time [0-9]{1,3}\n$"

class LeftTabWidget(QWidget):
    '''左侧选项栏'''
    pointlist=[] #########
    renameIndex = 1

    def __init__(self):
        super(LeftTabWidget, self).__init__()
        self.setObjectName('LeftTabWidget')
        
        self.setWindowTitle('LeftTabWidget')
        self.list_style = ('''
            QListWidget, QListView, QTreeWidget, QTreeView {
                outline: 0px;
            }
            QListWidget {
                min-width: 200px;
                max-width: 200px;
                
                color: White;
                background:#454545                            }
            QListWidget::Item:selected {
                background: lightGray;
                border-left: 5px solid #EE9A00;
                color: black
            }
            HistoryPanel:hover {
                background: rgb(52, 52, 52);
            }
        ''')

        #####################################################ZL
        self.left = 200
        self.top = 200
        self.width = 1000
        self.height = 800
        self.setGeometry(self.left, self.top, self.width, self.height)
        #####################################################ZL

        self.main_layout = QHBoxLayout(self, spacing=0)     #窗口的整体布局
        self.main_layout.setContentsMargins(0,0,0,0)

        self.left_widget = QListWidget()     #左侧选项列表
        self.left_widget.setStyleSheet(self.list_style)
        self.main_layout.addWidget(self.left_widget)

        self.right_widget = QStackedWidget()
        self.main_layout.addWidget(self.right_widget)

        self._setup_ui()
        '''
        if os.path.exists('/home/robot/waypoints.xml') == False :
            file = open('/home/robot/waypoints.xml','w')
            file.write('<Waterplus>\n</Waterplus>')
            file.close()
        f=open('/home/robot/waypoints.xml', 'r')#############
        pointlist=re.findall(r"(?<=<Name>).+?(?=</Name>)", f.read(), re.S)########
        f.close()#######
        self.comboBox2.addItems(pointlist)######
        '''

    def _setup_ui(self):
        '''加载界面ui'''

        self.left_widget.currentRowChanged.connect(self.right_widget.setCurrentIndex)   #list和右侧窗口的index对应绑定

        self.left_widget.setFrameShape(QListWidget.NoFrame)    #去掉边框

        self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  #隐藏滚动条
        self.left_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        list_str = ['功能选择','扫地','导航','取物','关于MOSS','使用方法','注意事项','硬件设置','联系与帮助','遇到问题','联系我们']

        for i in range(11):
            self.item = QListWidgetItem(list_str[i],self.left_widget)   #左侧选项的添加
            self.item.setFont(QFont("等线",11))
            if i ==  0 or i == 4 or i == 8:
                self.item.setBackground(QColor('#EE9A00'))
                self.item.setFont(QFont("等线",13,QFont.Bold))
                if i == 0:
                    self.item.setIcon(qtawesome.icon('fa.hand-pointer-o',color ='white'))
                elif i == 4:
                    self.item.setIcon(qtawesome.icon('fa.tags',color ='white'))
                elif i == 8:
                    self.item.setIcon(qtawesome.icon('fa.envelope',color ='white'))

            self.item.setSizeHint(QSize(60,65))
            self.item.setTextAlignment(Qt.AlignCenter)                  #居中显示

            if i == 1:
                self.centralWidget1=QtWidgets.QWidget()
                self.centralWidget1.setStyleSheet('''background:black;border-width:0;''');
                self.layout1 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                self.centralWidget1.setLayout(self.layout1) 
                

                self.edit1_1 = QtWidgets.QLineEdit()
                self.edit1_1.setPlaceholderText("请输入速度(两位小数,0.0-1.0)")
                self.edit1_1.setStyleSheet('''color:white;background:transparent;border-width:0;
                                                border-style:outset;border-bottom:1px solid white;
                                                font-size:20px; font-family:等线;''')
                self.vel_reg = QRegExp(r"^(0)|(0\.[0-9])|(1)|(1\.0)$")
                self.vel_validator = QRegExpValidator(self.vel_reg,self.edit1_1)
                self.edit1_1.setValidator(self.vel_validator)
            
                self.edit1_2 = QtWidgets.QLineEdit()
                self.edit1_2.setPlaceholderText("请输入时间(三位整数)")
                self.edit1_2.setStyleSheet('''color:white;background:transparent;border-width:0;
                                                border-style:outset;border-bottom:1px solid white;
                                                font-size:20px; font-family:等线;''')
                self.time_reg = QRegExp("^[0-9]{3}$")
                self.time_validator = QRegExpValidator(self.time_reg,self.edit1_2)
                self.edit1_2.setValidator(self.time_validator)
                
                self.label1_1 = QtWidgets.QLabel()    #设置label
                self.label1_1.setTextFormat(QtCore.Qt.AutoText)
                self.label1_1.setText("速度")
                self.label1_1.setStyleSheet('''color:white;font-size:23px; font-family:等线;''');
                self.label1_1.setAlignment(Qt.AlignCenter)
                
                self.label1_2 = QtWidgets.QLabel()
                self.label1_2.setTextFormat(QtCore.Qt.AutoText)
                self.label1_2.setText("时间")
                self.label1_2.setStyleSheet('''color:white;font-size:23px; font-family:等线;''');
                self.label1_2.setAlignment(Qt.AlignCenter)

                self.label1_3 = QtWidgets.QLabel()
                self.label1_3.setTextFormat(QtCore.Qt.AutoText)
                self.label1_3.setText("扫地")
                self.label1_3.setStyleSheet('''color:white;font-size:23px;background:rgb(100,100,100,80;background:#454545);
                                                font-family:等线;''');
                self.label1_3.setAlignment(Qt.AlignCenter)

                self.button1 = QtWidgets.QPushButton()
                self.button1.setText("开始")
                self.button1.setFixedSize(100,40)
                self.button1.setStyleSheet('''QPushButton{background:#EE9A00;border-radius:10px;font-family:等线;
                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')
                self.button1.clicked.connect(self.button1_1click)

                self.layout1.setColumnStretch(0, 2)
                self.layout1.setColumnStretch(1, 2)
                self.layout1.setColumnStretch(2, 2)
                self.layout1.setColumnStretch(3, 2)
                self.layout1.setColumnStretch(5, 2)
                self.layout1.setColumnStretch(6, 2)
                self.layout1.setColumnStretch(7, 2)
                self.layout1.setColumnStretch(8, 2)
                self.layout1.setColumnStretch(4, 1)

                self.layout1.addWidget(self.label1_3, 0, 0, 1, 9)
                self.layout1.addWidget(self.label1_1, 4, 2, 2, 2)
                self.layout1.addWidget(self.label1_2, 6, 2, 2, 2)
                self.layout1.addWidget(self.edit1_1,  4, 4, 2, 3)
                self.layout1.addWidget(self.edit1_2,  6, 4, 2, 3)
                self.layout1.addWidget(self.button1,  9, 4, 2, 2)
                self.right_widget.addWidget(self.centralWidget1)
                
            elif i == 2:
                self.centralWidget2=QtWidgets.QWidget()

                self.centralWidget2.setStyleSheet('''background:black;border-width:0;''');
                self.layout2 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                self.centralWidget2.setLayout(self.layout2)
                
                self.button2_1 = QtWidgets.QPushButton(self.centralWidget2)
                #self.button2_1.setGeometry(QtCore.QRect(210, 110, 100, 60))
                self.button2_1.setObjectName("button1")
                self.button2_1.setText("构建地图")
                self.button2_1.clicked.connect(self.button2_1click)
                self.button2_1.setFixedSize(200,80)
                self.button2_1.setStyleSheet('''QPushButton{background:#EE9A00;border-radius:20px;font-family:等线;
                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')

                self.button2_2 = QtWidgets.QPushButton(self.centralWidget2)
                #self.button2_2.setGeometry(QtCore.QRect(350, 110, 100, 60))
                self.button2_2.setObjectName("button2")
                self.button2_2.setText("保存地图")
                self.button2_2.clicked.connect(self.button2_2click)
                self.button2_2.setFixedSize(200,80)
                self.button2_2.setStyleSheet('''QPushButton{background:#EE9A00;border-radius:20px;font-family:等线;
                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')

                self.button2_3 = QtWidgets.QPushButton(self.centralWidget2)
                #self.button2_3.setGeometry(QtCore.QRect(210, 210, 100, 60))
                self.button2_3.setObjectName("button3")
                self.button2_3.setText("设立航点")
                self.button2_3.clicked.connect(self.button2_3click)
                self.button2_3.setFixedSize(200,80)
                self.button2_3.setStyleSheet('''QPushButton{background:#EE9A00;border-radius:20px;font-family:等线;
                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')

                self.button2_4 = QtWidgets.QPushButton(self.centralWidget2)
                #self.button2_4.setGeometry(QtCore.QRect(350, 210, 100, 60))
                self.button2_4.setObjectName("button4")
                self.button2_4.setText("保存航点")
                self.button2_4.clicked.connect(self.button2_4click)
                self.button2_4.setFixedSize(200,80)
                self.button2_4.setStyleSheet('''QPushButton{background:#EE9A00;border-radius:20px;font-family:等线;
                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')

                self.button2_5 = QtWidgets.QPushButton(self.centralWidget2)
                #self.button2_5.setGeometry(QtCore.QRect(210, 310, 240, 60))
                self.button2_5.setObjectName("button5")
                self.button2_5.setText("开始导航")
                self.button2_5.clicked.connect(self.button2_5click)
                self.button2_5.setFixedSize(466,80)
                self.button2_5.setStyleSheet('''QPushButton{background:#EE9A00;border-radius:20px;font-family:等线;
                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')
                

                self.comboBox2 = QtWidgets.QComboBox(self.centralWidget2)
                #self.comboBox2.setGeometry(QtCore.QRect(210, 410, 100, 30))
                self.comboBox2.setObjectName("comboBox")
                #self.comboBox2.addItems(self.pointlist)
                self.comboBox2.setFixedSize(200,50)
                self.comboBox2.setStyleSheet('''QComboBox{background:#EE9A00;border-radius:10px;font-family:等线;
                                               font-size:18px;color:white}QComboBox:hover{background:#EEDC82;}''')

                self.button2_6 = QtWidgets.QPushButton(self.centralWidget2)
                #self.button2_6.setGeometry(QtCore.QRect(350, 410, 100, 30))
                self.button2_6.setObjectName("button6")
                self.button2_6.setText("G O !")
                self.button2_6.clicked.connect(self.button2_6click)
                self.button2_6.setFixedSize(200,50)
                self.button2_6.setStyleSheet('''QPushButton{background:#EE9A00;border-radius:20px;font-family:等线;
                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')

                self.label2_1 = QtWidgets.QLabel()
                self.label2_1.setTextFormat(QtCore.Qt.AutoText)
                self.label2_1.setText("导航")
                self.label2_1.setStyleSheet('''color:white;font-size:23px;background:rgb(100,100,100,100);
                                                font-family:等线;''');
                self.label2_1.setAlignment(Qt.AlignCenter)
                
                self.layout2.setColumnStretch(0, 1)
                self.layout2.setColumnStretch(1, 1)
                self.layout2.setColumnStretch(2, 1)
                self.layout2.setColumnStretch(3, 1)
                self.layout2.setColumnStretch(4, 1)
                self.layout2.setColumnStretch(5, 1)
                self.layout2.setColumnStretch(6, 1)
                self.layout2.setColumnStretch(7, 1)
                self.layout2.setColumnStretch(8, 1)
                self.layout2.setColumnStretch(9, 1)
                self.layout2.setColumnStretch(10, 1)
                self.layout2.setColumnStretch(11, 1)
                self.layout2.setColumnStretch(12, 1)

                self.layout2.addWidget(self.label2_1, 0, 0, 1, 13)
                self.layout2.addWidget(self.button2_1, 2, 3, 2, 3)
                self.layout2.addWidget(self.button2_2, 2, 7, 2, 3)
                self.layout2.addWidget(self.button2_3, 6, 3, 2, 3)
                self.layout2.addWidget(self.button2_4, 6, 7, 2, 3)
                self.layout2.addWidget(self.button2_5, 10, 3, 2, 7)
                self.layout2.addWidget(self.button2_6, 14, 7, 2, 3)
                self.layout2.addWidget(self.comboBox2, 14, 3, 2, 3)
                
                self.right_widget.addWidget(self.centralWidget2)

            elif i == 10:
                self.centralWidget10=QtWidgets.QWidget()
                self.centralWidget10.setStyleSheet('''background:black;border-width:0;''');

                self.layout10 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                self.centralWidget10.setLayout(self.layout10)

                self.label10_1 = QtWidgets.QLabel()
                self.label10_1.setTextFormat(QtCore.Qt.AutoText)
                self.label10_1.setText("Contact us!")
                self.label10_1.setStyleSheet('''color:white;font-size:23px;background:#FF9900;
                                                font-family:Times new Romans;''');
                self.label10_1.setAlignment(Qt.AlignCenter)

                self.label10_2 = QtWidgets.QLabel()
                self.label10_2.setTextFormat(QtCore.Qt.AutoText)
                self.label10_2.setPixmap(QPixmap('lzz.png'))
                self.label10_2.setStyleSheet('''color:white;font-size:23px;background:rgb(0,0,0,0);
                                                border-width:10;border-style:outset;border-color:red;
                                                font-family:等线;''');
                self.label10_2.setAlignment(Qt.AlignCenter)

                self.label10_3 = QtWidgets.QLabel()
                self.label10_3.setTextFormat(QtCore.Qt.AutoText)
                self.label10_3.setText("组长 李贞子\n邮箱：ZhenziL@buaa.edu.cn\n负责：UI架构、自由避障行走、抓取\n格言：我是傻猪")
                self.label10_3.setStyleSheet('''color:white;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#FF9900;
                                                font-family:等线;''');
                self.label10_3.setAlignment(Qt.AlignCenter)

                self.label10_4 = QtWidgets.QLabel()
                self.label10_4.setTextFormat(QtCore.Qt.AutoText)
                self.label10_4.setPixmap(QPixmap('wrz.png'))
                self.label10_4.setStyleSheet('''color:white;font-size:23px;background:rgb(0,0,0,0);
                                                border-width:10;border-style:outset;border-color:red;
                                                font-family:等线;''');
                self.label10_4.setAlignment(Qt.AlignCenter)

                self.label10_5 = QtWidgets.QLabel()
                self.label10_5.setTextFormat(QtCore.Qt.AutoText)
                self.label10_5.setText("组员：王润泽\n邮箱：beihangcj@hotmail.com\n负责：自由避障行走以及抓取部分UI\n格言：广告位招租")
                self.label10_5.setStyleSheet('''color:white;font-size:23px;background:rgb(00,0,0,0);
                                                border-width:5;border-style:ridge;border-color:#FF9900;
                                                font-family:等线;''');
                self.label10_5.setAlignment(Qt.AlignCenter)

                self.label10_6 = QtWidgets.QLabel()
                self.label10_6.setTextFormat(QtCore.Qt.AutoText)
                self.label10_6.setPixmap(QPixmap('zl.png'))
                self.label10_6.setStyleSheet('''color:white;font-size:23px;background:rgb(0,0,00,0);
                                                border-width:10;border-style:outset;border-color:red;
                                                font-family:等线;''');
                self.label10_6.setAlignment(Qt.AlignCenter)

                self.label10_7 = QtWidgets.QLabel()
                self.label10_7.setTextFormat(QtCore.Qt.AutoText)
                self.label10_7.setText("组员：张璐\n邮箱：beihangcj@hotmail.com\n负责：导航部分功能\n格言：好好学习天天向上")
                self.label10_7.setStyleSheet('''color:white;font-size:23px;background:rgb(0,00,0,0);
                                                border-width:5;border-style:ridge;border-color:#FF9900;
                                                font-family:等线;''');
                self.label10_7.setAlignment(Qt.AlignCenter)

                self.label10_8 = QtWidgets.QLabel()
                self.label10_8.setTextFormat(QtCore.Qt.AutoText)
                self.label10_8.setPixmap(QPixmap('zjl.png'))
                self.label10_8.setStyleSheet('''color:white;font-size:23px;
                                                border-width:10;border-style:outset;border-color:red;
                                                background:rgb(100,100,100,100);
                                                font-family:等线;''');
                self.label10_8.setAlignment(Qt.AlignCenter)

                self.label10_9 = QtWidgets.QLabel()
                self.label10_9.setTextFormat(QtCore.Qt.AutoText)
                self.label10_9.setText("组员：张佳琳\n邮箱：beihangcj@hotmail.com\n负责：导航部分UI\n格言：戏说不是胡说，改编不是乱编")
                self.label10_9.setStyleSheet('''color:white;font-size:23px;background:rgb(0,0,0,0);
                                                border-width:5;border-style:ridge;border-color:#FF9900;
                                                font-family:等线;''');
                self.label10_9.setAlignment(Qt.AlignCenter)

                self.label10_10 = QtWidgets.QLabel()
                self.label10_10.setTextFormat(QtCore.Qt.AutoText)
                self.label10_10.setPixmap(QPixmap('lty.png'))
                self.label10_10.setStyleSheet('''color:white;font-size:23px;background:rgb(00,00,0,0);
                                                 border-width:10;border-style:outset;border-color:red;
                                                font-family:等线;''');
                self.label10_10.setAlignment(Qt.AlignCenter)

                self.label10_11 = QtWidgets.QLabel()
                self.label10_11.setTextFormat(QtCore.Qt.AutoText)
                self.label10_11.setText("组员：李天宇\n邮箱：beihangcj@hotmail.com\n负责：动态避障功能\n格言：我不做人啦")
                self.label10_11.setStyleSheet('''color:white;font-size:23px;background:rgb(0,0,0,0);
                                                border-width:5;border-style:ridge;border-color:#FF9900;
                                                font-family:等线;''');
                self.label10_11.setAlignment(Qt.AlignCenter)

                #self.layout10.setColumnStretch(0, 1)
                self.layout10.addWidget(self.label10_1,1,1,1,6)

                self.layout10.addWidget(self.label10_2,2,1)
                self.layout10.addWidget(self.label10_3,3,1,2,1)

                self.layout10.addWidget(self.label10_4,2,2)
                self.layout10.addWidget(self.label10_5,3,2,2,1)

                self.layout10.addWidget(self.label10_6,2,3)
                self.layout10.addWidget(self.label10_7,3,3,2,1)

                self.layout10.addWidget(self.label10_8,2,4)
                self.layout10.addWidget(self.label10_9,3,4,2,1)

                self.layout10.addWidget(self.label10_10,2,5)
                self.layout10.addWidget(self.label10_11,3,5,2,1)

                self.right_widget.addWidget(self.centralWidget10)

            else:
                self.centralWidget0=QtWidgets.QWidget()
                self.centralWidget0.setStyleSheet('''background:white;border-width:0;''');
                self.right_widget.addWidget(self.centralWidget0)
                
    def button1_1click(self):
        vel = 0
        time = 0  

        if self.edit1_1.text() == "":
            vel = 0.5
        else:
            vel = float(self.edit1_1.text())

        if self.edit1_2.text() == "":
            time = 60
        else: 
            time = int(self.edit1_2.text())

        self.setConfig(vel,time)

        os.system(free_walk_cmd)

    def setConfig(self,vel,time):
        vel_pattern = re.compile(vel_config)
        time_pattern = re.compile(time_config)

        with open(config_path,"w") as f:
            f.truncate()
            f.write(str(vel))
            f.write("\n")
            f.write(str(time))

    def button2_1click(self):
        '''
        print("roslaunch wpb_home_tutorials gmapping.launch")
        #os.system("roslaunch wpb_home_tutorials gmapping.launch")
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpb_home_tutorials gmapping.launch\"'")
        #os.system("gnome-terminal -e 'bash -c \"ls\"'")
        #os.system("gnome-terminal -e 'bash -c \"roslaunch wpb_home_tutorials gmapping.launch; exec bash\"'")
        '''
        pass
    def button2_2click(self):
        '''
        print("rosrun map_server map_saver -f map")
        os.system("gnome-terminal -e 'bash -c \"rosrun map_server map_saver -f map&&cp map.yaml /home/robot/catkin_ws/src/wpb_home/wpb_home_tutorials/maps/map.yaml&&cp map.pgm /home/robot/catkin_ws/src/wpb_home/wpb_home_tutorials/maps/map.pgm\"'")##yidong
	#save in the main dir
        #print("移动指令")
	#may be we do not need to really change the map path, because we can change the map path in some launch files
	#such as, in add_waypoint.launch, we can change 
	#args="$(find wpb_home_tutorials)/maps/map.yaml"/>
	#into
	#args="/home/robot/map.yaml"/>
    '''
        pass

    def button2_3click(self):
        '''
        print("roslaunch waterplus_map_tools add_waypoint.launch")
        os.system("gnome-terminal -e 'bash -c \"roslaunch waterplus_map_tools add_waypoint.launch\"'")
        ###???????????????????????????????????
        '''
        pass

    def button2_4click(self):
        '''
        def indexRename(matched):
                self.renameIndex+=1;
                return str(self.renameIndex-1);
        print("rosrun waterplus_map_tools wp_saver")
        os.system("gnome-terminal -e 'bash -c \"cd /home/robot/&&rosrun waterplus_map_tools wp_saver\"'")
        time.sleep(2)
        #os.system("rosrun waterplus_map_tools wp_saver")
        #os.system("gnome-terminal -e 'bash -c \"rosrun waterplus_map_tools wp_saver; exec bash\"'")
	#save waypoints.xml into /home/robot/
        self.comboBox2.clear()
        if os.path.exists('/home/robot/waypoints.xml') == False :
            file = open('/home/robot/waypoints.xml','w')
            file.write('<Waterplus>\n</Waterplus>')
            file.close()
        f=open('/home/robot/waypoints.xml', 'r')
        newFile=re.sub(r"(?<=<Name>).+?(?=</Name>)",indexRename,f.read())
        f.close()
        f=open('/home/robot/waypoints.xml', 'w')
        f.write(newFile)
        f.close()
        self.renameIndex = 1
        f=open('/home/robot/waypoints.xml', 'r')
        pointlist=re.findall(r"(?<=<Name>).+?(?=</Name>)", f.read(), re.S)
        print(pointlist)
        self.comboBox2.addItems(pointlist)
        f.close()
        '''
        pass

    def button2_5click(self):
        '''
        print("roslaunch wpb_home_apps 6_path_plan.launch")
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpb_home_apps 6_path_plan.launch; exec bash\"'")
        '''
        pass

    def button2_6click(self):
        pass
        '''
        print(self.comboBox2.currentIndex()+1)
	#get to the chosed point
        pointoutput = open('/home/robot/point.txt', 'w')
        pointoutput.write(str(self.comboBox2.currentIndex()+1))
        pointoutput.close()
        '''

    def button3_1click(self):
        os.system("roslaunch myshop shopping_201.launch")

    def button3_2click(self):
        r = os.popen("roslaunch darknet_ros darknet_ros.launch")
        text = r.read()
        textlist = text.split("\n")
        for text in textlist:
            if text.startswith("[ERROR]"):
                button3_2click()
                return

def main():
    ''' '''
    app = QApplication(sys.argv)

    main_wnd = LeftTabWidget()
    main_wnd.show()

    app.exec()

if __name__ == '__main__':
    main()
