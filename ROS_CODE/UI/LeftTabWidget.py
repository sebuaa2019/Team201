import sys
import os
import regex as re
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore,QtGui,QtWidgets
import qtawesome


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
                background:#454545;
            }

            QListWidget::Item:selected {
                background: lightGray;
                border-left: 5px solid #EE9A00;
                color: black
            }
            HistoryPanel:hover {
                background: rgb(52, 52, 52);
            }
        ''')


        self.main_layout = QHBoxLayout(self, spacing=0)     #窗口的整体布局
        self.main_layout.setContentsMargins(0,0,0,0)

        self.left_widget = QListWidget()     #左侧选项列表
        self.left_widget.setStyleSheet(self.list_style)
        self.main_layout.addWidget(self.left_widget)

        self.right_widget = QStackedWidget()
        self.main_layout.addWidget(self.right_widget)

        self._setup_ui()


    def _setup_ui(self):
        '''加载界面ui'''

        self.left_widget.currentRowChanged.connect(self.right_widget.setCurrentIndex)   #list和右侧窗口的index对应绑定

        self.left_widget.setFrameShape(QListWidget.NoFrame)    #去掉边框

        self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  #隐藏滚动条
        self.left_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        list_str = ['功能选择','避障','导航','取物','关于MOSS','使用方法','注意事项','硬件设置','联系与帮助','遇到问题','联系lzz']

        for i in range(11):
            self.item = QListWidgetItem(list_str[i],self.left_widget)   #左侧选项的添加
            self.item.setFont(QFont("等线",11))
            if i ==  0 or i == 4 or i == 8:
                self.item.setBackground(QColor('#EE9A00'))
                self.item.setFont(QFont("等线",13,QFont.Bold))
                if i == 0:
                    self.item.setIcon(qtawesome.icon('fa.hand-pointer-o',color ='white'))
		    
	            self.centralWidget0=QtWidgets.QWidget()
                    self.centralWidget0.setStyleSheet('''background:#636363;border-width:0;''');
                    self.layout0 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                    self.centralWidget0.setLayout(self.layout0) 
                    #self.centralWidget0.setLayout(self.layout0)
                    self.label0_1 = QtWidgets.QLabel()    #设置label
                    self.label0_1.setTextFormat(QtCore.Qt.AutoText)
                    self.label0_1.setStyleSheet('''color:white;font-size:23px; font-family:等线;''');
                    self.label0_1.setAlignment(Qt.AlignCenter)
                    self.label0_1.setPixmap(QPixmap('cp03.jpg'))
                    self.layout0.addWidget(self.label0_1, 0, 0, 1, 9)
                    
                    self.right_widget.addWidget(self.centralWidget0)
                elif i == 4:
                    self.item.setIcon(qtawesome.icon('fa.tags',color ='white'))
		
		    self.centralWidget4=QtWidgets.QWidget()
                    self.centralWidget4.setStyleSheet('''background:#636363;border-width:0;''');
                    self.layout4 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                    self.centralWidget4.setLayout(self.layout4) 
                    #self.centralWidget0.setLayout(self.layout0)
                    self.label4_1 = QtWidgets.QLabel()    #设置label
                    self.label4_1.setTextFormat(QtCore.Qt.AutoText)
                    self.label4_1.setStyleSheet('''color:white;font-size:23px; font-family:等线;''');
                    self.label4_1.setAlignment(Qt.AlignCenter)
                    self.label4_1.setPixmap(QPixmap('cp03.jpg'))
                    self.layout4.addWidget(self.label4_1, 0, 0, 1, 9)
                    
                    self.right_widget.addWidget(self.centralWidget4)
                elif i == 8:
                    self.item.setIcon(qtawesome.icon('fa.envelope',color ='white'))
		    
		    self.centralWidget8=QtWidgets.QWidget()
                    self.centralWidget8.setStyleSheet('''background:#636363;border-width:0;''');
                    self.layout8 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                    self.centralWidget8.setLayout(self.layout8) 
                    #self.centralWidget0.setLayout(self.layout0)
                    self.label8_1 = QtWidgets.QLabel()    #设置label
                    self.label8_1.setTextFormat(QtCore.Qt.AutoText)
                    self.label8_1.setStyleSheet('''color:white;font-size:23px; font-family:等线;''');
                    self.label8_1.setAlignment(Qt.AlignCenter)
                    self.label8_1.setPixmap(QPixmap('cp03.jpg'))
                    self.layout8.addWidget(self.label8_1, 0, 0, 1, 9)
                    
                    self.right_widget.addWidget(self.centralWidget8)
		
            self.item.setSizeHint(QSize(60,65))
            self.item.setTextAlignment(Qt.AlignCenter)                  #居中显示

            if i == 1:
                self.centralWidget1=QtWidgets.QWidget()
                self.centralWidget1.setStyleSheet('''background:#636363;border-width:0;''');
                self.layout1 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                self.centralWidget1.setLayout(self.layout1) 
                

                self.edit1_1 = QtWidgets.QLineEdit()
                self.edit1_1.setPlaceholderText("请输入速度(两位小数,0.0-1.0)")
                self.edit1_1.setStyleSheet('''color:white;background:transparent;border-width:0;
                                                border-style:outset;border-bottom:1px solid white;
                                                font-size:20px; font-family:等线;''')
        
                self.edit1_2 = QtWidgets.QLineEdit()
                self.edit1_2.setPlaceholderText("请输入时间(三位整数)")
                self.edit1_2.setStyleSheet('''color:white;background:transparent;border-width:0;
                                                border-style:outset;border-bottom:1px solid white;
                                                font-size:20px; font-family:等线;''')
                
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
                self.label1_3.setText("避障")
                self.label1_3.setStyleSheet('''color:white;font-size:23px;background:rgb(100,100,100,80;background:#454545);
                                                font-family:等线;''');
                self.label1_3.setAlignment(Qt.AlignCenter)

                self.button1 = QtWidgets.QPushButton()
                self.button1.setText("开始")
                self.button1.setFixedSize(100,40)
                self.button1.setStyleSheet('''QPushButton{background:#EE9A00;border-radius:10px;font-family:等线;
                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')
        
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

                self.centralWidget2.setStyleSheet('''background:#636363;border-width:0;''');
                self.layout2 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                self.centralWidget2.setLayout(self.layout2)
                
                self.button2_1 = QtWidgets.QPushButton(self.centralWidget2)
                self.button2_1.setObjectName("button1")
                self.button2_1.setText("构建地图")
                self.button2_1.clicked.connect(self.button2_1click)
                self.button2_1.setStyleSheet('''QPushButton{background:#EE9A00;border-radius:20px;font-family:等线;
                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')
                self.button2_1.setFixedHeight(40)

                self.button2_2 = QtWidgets.QPushButton(self.centralWidget2)
                self.button2_2.setObjectName("button2")
                self.button2_2.setText("保存地图")
                self.button2_2.clicked.connect(self.button2_2click)
                self.button2_2.setStyleSheet('''QPushButton{background:#EE9A00;border-radius:20px;font-family:等线;
                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')
                self.button2_2.setFixedHeight(40)

                self.button2_3 = QtWidgets.QPushButton(self.centralWidget2)
                self.button2_3.setObjectName("button3")
                self.button2_3.setText("设立航点")
                self.button2_3.clicked.connect(self.button2_3click)
                self.button2_3.setStyleSheet('''QPushButton{background:#EE9A00;border-radius:20px;font-family:等线;
                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')
                self.button2_3.setFixedHeight(40)

                self.button2_4 = QtWidgets.QPushButton(self.centralWidget2)
                self.button2_4.setObjectName("button4")
                self.button2_4.setText("保存航点")
                self.button2_4.clicked.connect(self.button2_4click)
                self.button2_4.setStyleSheet('''QPushButton{background:#EE9A00;border-radius:20px;font-family:等线;
                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')
                self.button2_4.setFixedHeight(40)

                self.button2_5 = QtWidgets.QPushButton(self.centralWidget2)
                self.button2_5.setObjectName("button5")
                self.button2_5.setText("开始导航")
                self.button2_5.clicked.connect(self.button2_5click)
                self.button2_5.setStyleSheet('''QPushButton{background:#EE9A00;border-radius:20px;font-family:等线;
                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')
                self.button2_5.setFixedHeight(40)
                

                self.comboBox2 = QtWidgets.QComboBox(self.centralWidget2)
                self.comboBox2.setObjectName("comboBox")
                self.comboBox2.setStyleSheet('''QComboBox{background:#EE9A00;border-radius:10px;font-family:等线;
                                               font-size:18px;color:white}QComboBox:hover{background:#EEDC82;}''')
                self.comboBox2.setFixedHeight(40)

                self.button2_6 = QtWidgets.QPushButton(self.centralWidget2)
                self.button2_6.setObjectName("button6")
                self.button2_6.setText("G O !")
                self.button2_6.clicked.connect(self.button2_6click)
                self.button2_6.setStyleSheet('''QPushButton{background:#EE9A00;border-radius:20px;font-family:等线;
                                               font-size:18px;color:white}QPushButton:hover{background:#EEDC82;}''')
                self.button2_6.setFixedHeight(40)

                self.label2_1 = QtWidgets.QLabel()
                self.label2_1.setTextFormat(QtCore.Qt.AutoText)
                self.label2_1.setText("导航")
                self.label2_1.setStyleSheet('''color:white;font-size:23px;background:rgb(100,100,100,80;background:#454545);
                                                font-family:等线;''')
                self.label2_1.setAlignment(Qt.AlignCenter)

                self.label2_2 = QtWidgets.QLabel()
                self.label2_2.setTextFormat(QtCore.Qt.AutoText)
                self.label2_2.setText("")
                self.label2_2.setAlignment(Qt.AlignCenter)
                
                self.layout2.setColumnStretch(0, 1)
                self.layout2.setColumnStretch(1, 2)
                self.layout2.setColumnStretch(2, 2)
                self.layout2.setColumnStretch(3, 1)            
                self.layout2.setColumnStretch(4, 2)
                self.layout2.setColumnStretch(5, 2)
                self.layout2.setColumnStretch(6, 1)
                self.layout2.setRowStretch(0,2)
                self.layout2.setRowStretch(1,2)
                self.layout2.setRowStretch(2,2)
                self.layout2.setRowStretch(3,2)
                self.layout2.setRowStretch(4,2)
                self.layout2.setRowStretch(5,2)
                self.layout2.setRowStretch(6,2)
                self.layout2.setRowStretch(7,2)
                self.layout2.setRowStretch(8,2)
                self.layout2.setHorizontalSpacing(5)
                self.layout2.setVerticalSpacing(5)


                self.layout2.addWidget(self.label2_1, 0,0,1,7)
                self.layout2.addWidget(self.button2_1, 2,1,1,2)
                self.layout2.addWidget(self.button2_2, 2,4,1,2)
                self.layout2.addWidget(self.button2_3, 4,1,1,2)
                self.layout2.addWidget(self.button2_4, 4,4,1,2)
                self.layout2.addWidget(self.button2_5, 6,1,1,5)
                self.layout2.addWidget(self.button2_6, 8,4,1,2)
                self.layout2.addWidget(self.comboBox2, 8,1,1,2)
                self.layout2.addWidget(self.label2_2, 9,1,1,7)
                
                self.right_widget.addWidget(self.centralWidget2)

	    elif i == 3:
                self.label3_1 = QtWidgets.QLabel()
                self.label3_1.setTextFormat(QtCore.Qt.AutoText)
                self.label3_1.setText("抓取")
                self.label3_1.setStyleSheet('''color:white;font-size:23px;background:rgb(100,100,100,80;background:#454545);
                                                font-family:等线;''');
                self.label3_1.setAlignment(Qt.AlignCenter)


                self.label3_2 = QtWidgets.QLabel()
                self.label3_2.setAlignment(Qt.AlignCenter)
                pixmap=QPixmap('C:\\Users\\lenovo\\Desktop\\指南针.png').scaled(self.label3_2.width()*0.25, self.label3_2.height()*0.35)
                self.label3_2.setPixmap(pixmap)


                self.label3_3 = QtWidgets.QLabel()
                self.label3_3.setAlignment(Qt.AlignCenter)
                pixmap=QPixmap('C:\\Users\\lenovo\\Desktop\\放大镜.png').scaled(self.label3_3.width()*0.25, self.label3_3.height()*0.35)
                self.label3_3.setPixmap(pixmap)
    
 
                self.centralWidget3=QtWidgets.QWidget()
                self.centralWidget3.setStyleSheet('''background:#636363;border-width:0;''');
                self.layout3 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                self.centralWidget3.setLayout(self.layout3) 

                self.button3_1 = QtWidgets.QPushButton()
                self.button3_1.setText("标定航点")
                self.button3_1.setFixedSize(200,40)
                self.button3_1.setStyleSheet('''
                    QPushButton{
                        border:none;color:white;
                        border-bottom:1px solid white;
                        font-size:20px;
                        font-weight:700;
                        font-family:等线;
                    }
                ''')
                

                self.button3_2 = QtWidgets.QPushButton()
                self.button3_2.setText("检测物体并抓取")
                self.button3_2.setFixedSize(200,40)
                self.button3_2.setStyleSheet('''
                    QPushButton{
                        border:none;color:white;
                        border-bottom:1px solid white;
                        font-size:20px;
                        font-weight:700;
                        font-family:等线;
                    }
                ''')

                self.layout3.addWidget(QtWidgets.QWidget(), 1, 0, 1, 10)
                self.layout3.addWidget(QtWidgets.QWidget(), 5, 0, 2, 10)
                self.layout3.addWidget(self.label3_1, 0, 0, 1, 9)
                self.layout3.addWidget(self.label3_2, 2, 2, 1, 1)
                self.layout3.addWidget(self.label3_3, 2, 6, 1, 1)
                self.layout3.addWidget(self.button3_1, 4, 2, 1, 2)
                self.layout3.addWidget(self.button3_2, 4, 6, 1, 2)
                self.right_widget.addWidget(self.centralWidget3)
		
	    elif i == 5:
                self.centralWidget5=QtWidgets.QWidget()
                self.centralWidget5.setStyleSheet('''background:#636363;border-width:0;''');
                self.layout5 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                self.centralWidget5.setLayout(self.layout5)

                self.label5_0 = QtWidgets.QLabel()
                self.label5_0.setTextFormat(QtCore.Qt.AutoText)
                self.label5_0.setText("使用方法")
                self.label5_0.setStyleSheet('''color:white;font-size:23px;background:rgb(100,100,100,80;background:#454545);
                                                font-family:等线;''');
                self.label5_0.setAlignment(Qt.AlignCenter)

                self.label5_1 = QtWidgets.QLabel()
                self.label5_1.setAlignment(Qt.AlignCenter)
                pixmap=QPixmap('robot.png').scaled(self.label5_1.width()*0.07, self.label5_1.height()*0.10)
                self.label5_1.setPixmap(pixmap)

                self.label5_2 = QtWidgets.QLabel()
                self.label5_2.setAlignment(Qt.AlignCenter)
                pixmap=QPixmap('避障.png').scaled(self.label5_2.width()*0.07, self.label5_2.height()*0.10)
                self.label5_2.setPixmap(pixmap)

                self.label5_3 = QtWidgets.QLabel()
                self.label5_3.setAlignment(Qt.AlignCenter)
                pixmap=QPixmap('导航.png').scaled(self.label5_3.width()*0.07, self.label5_3.height()*0.10)
                self.label5_3.setPixmap(pixmap)

                self.label5_4 = QtWidgets.QLabel()
                self.label5_4.setAlignment(Qt.AlignCenter)
                pixmap=QPixmap('抓取.png').scaled(self.label5_4.width()*0.07, self.label5_4.height()*0.10)
                self.label5_4.setPixmap(pixmap)


                self.label5_5 = QtWidgets.QLabel()    #设置label
                self.label5_5.setTextFormat(QtCore.Qt.AutoText)
                self.label5_5.setText('''
                                        控制界面：MOSS软件平台，了解关于MOSS的一切服务\n
                                        打开MOSS：按下底盘上的开关按钮使之变亮\n
                                        关闭MOSS：按下底盘上的开关按钮使之变暗\n
                                        USB连接： 麦克风、相机、机械臂、雷达、以太网等\n
                                       （具体接口参照MOSS手册）''')
                self.label5_5.setStyleSheet('''color:white;font-size:14px; font-family:等线;''');
                self.label5_5.setAlignment(Qt.AlignLeft)

                self.label5_6 = QtWidgets.QLabel()    #设置label
                self.label5_6.setTextFormat(QtCore.Qt.AutoText)
                self.label5_6.setText('''
                                        避障：遇到障碍物则避障，随机行走\n
                                        输入速度，机器人将以该速度前进\n
                                        输入时间，机器人在指定时间内运行，时间完毕则停止\n
                                        点击开始按钮，机器人开始避障（输入的时间与速度都\n
                                        应符合要求）''')
                self.label5_6.setStyleSheet('''color:white;font-size:14px; font-family:等线;''');
                self.label5_6.setAlignment(Qt.AlignLeft)

                self.label5_7 = QtWidgets.QLabel()    #设置label
                self.label5_7.setTextFormat(QtCore.Qt.AutoText)
                self.label5_7.setText('''
                                        导航：机器人行走至目标航点\n
                                        点击建立地图按钮，使用手柄建立地图，地图应覆盖需要行走到的航点\n
                                        点击保存地图按钮，保存刚刚建立的地图\n
                                        点击标定航点按钮，在地图上标定可能的航点\n
                                        点击保存航点按钮，保存刚刚标定的航点信息\n
                                        在下拉菜单中选择需要机器人行走到的航点\n
                                        点击开始导航按钮，机器人将行走至目标航点''')
                self.label5_7.setStyleSheet('''color:white;font-size:14px; font-family:等线;''');
                self.label5_7.setAlignment(Qt.AlignLeft)

                self.label5_8 = QtWidgets.QLabel()    #设置label
                self.label5_8.setTextFormat(QtCore.Qt.AutoText)
                self.label5_8.setText('''
                                        抓取：机器人识别目标物体并进行抓取\n
                                        点击建立航点按钮，带领机器人用语音标定航点\n
                                        点击开始检测并抓取按钮，机器人将识别出目标物体\n
                                        并完成抓取动作\n
                                        抓取结束后机器人将回到开始识别的地点并将物体递给用户''')
                self.label5_8.setStyleSheet('''color:white;font-size:14px; font-family:等线;''');
                self.label5_8.setAlignment(Qt.AlignLeft)
                

                '''
                self.layout5.addWidget(self.label5_3, 2, 6, 1, 1)
                self.layout5.addWidget(self.button5_1, 4, 2, 1, 2)
                self.layout5.addWidget(self.button5_2, 4, 6, 1, 2)
                '''
                self.layout5.addWidget(self.label5_0, 0, 0, 1, 8)
                self.layout5.addWidget(self.label5_1, 1, 0, 1, 4)
                self.layout5.addWidget(self.label5_2, 1, 4, 1, 4)
                self.layout5.addWidget(self.label5_3, 5, 0, 1, 4)
                self.layout5.addWidget(self.label5_4, 5, 4, 1, 4)
                self.layout5.addWidget(self.label5_5, 2, 0, 3, 4)
                self.layout5.addWidget(self.label5_6, 2, 4, 3, 4)
                self.layout5.addWidget(self.label5_7, 6, 0, 3, 4)
                self.layout5.addWidget(self.label5_8, 6, 4, 3, 4)
                self.right_widget.addWidget(self.centralWidget5)
		
            elif i == 6:
                self.centralWidget6=QtWidgets.QWidget()
                self.centralWidget6.setStyleSheet('''background:#636363;border-width:0;''');

                self.layout6 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                self.centralWidget6.setLayout(self.layout6)

                ##start coding
                self.label6_1 = QtWidgets.QLabel()
                self.label6_1.setTextFormat(QtCore.Qt.AutoText)
                self.label6_1.setText("注意事项")
                self.label6_1.setStyleSheet('''color:white;font-size:23px;background:#FF9900;
                                                font-family:Times new Romans;''');
                self.label6_1.setAlignment(Qt.AlignCenter)

                self.label6_2 = QtWidgets.QLabel()
                self.label6_2.setTextFormat(QtCore.Qt.AutoText)
                self.label6_2.setText('环境要求:\n\
                1、机器人一定要在室内运行，且空间不能过于狭窄。\n\
                2、最好时刻保证机器人的工作温度在15°C到35°C间。\n\
                3、避免与雨水、雾、积水以及任何其他液体接触等。')
                self.label6_2.setStyleSheet('''color:white;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#FF9900;
                                                font-family:等线;''')
                self.label6_2.setAlignment(Qt.AlignCenter)
                

                self.label6_3 = QtWidgets.QLabel()
                self.label6_3.setTextFormat(QtCore.Qt.AutoText)
                self.label6_3.setText("避免损伤:\n\
                1、避免因机器人速度过快造成的损伤。\n\
                2、避免机器人接近地图边界时的碰撞。\n\
                3、注意机械臂在抓取时的姿态和力度。")
                self.label6_3.setStyleSheet('''color:white;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#FF9900;
                                                font-family:等线;''')
                self.label6_3.setAlignment(Qt.AlignCenter)

                self.layout6.addWidget(self.label6_1,0,0,1,4)
                self.layout6.addWidget(self.label6_2,1,0,1,2)
                self.layout6.addWidget(self.label6_3,1,2,1,2)
                #self.layout6.addWidget(self.label6_4,2,0,1,2)
                #self.layout6.addWidget(self.label6_5,2,2,1,2)

                self.right_widget.addWidget(self.centralWidget6)
				
            elif i == 7:
                self.centralWidget7=QtWidgets.QWidget()
                self.centralWidget7.setStyleSheet('''background:#636363;border-width:0;''');

                self.layout7 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                self.centralWidget7.setLayout(self.layout7)

                ##start coding
                self.label7_1 = QtWidgets.QLabel()
                self.label7_1.setTextFormat(QtCore.Qt.AutoText)
                self.label7_1.setText("硬件设置")
                self.label7_1.setStyleSheet('''color:white;font-size:23px;background:#636363;
                                                font-family:Times new Romans;''');
                self.label7_1.setAlignment(Qt.AlignCenter)

                self.label7_2 = QtWidgets.QLabel()
                self.label7_2.setTextFormat(QtCore.Qt.AutoText)
                self.label7_2.setPixmap(QPixmap('structure.png'))
                self.label7_2.setStyleSheet('''color:white;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#FF9900;
                                                font-family:等线;''')
                #self.label7_2.setScaledContents(True)
                self.label7_2.setAlignment(Qt.AlignCenter)
                

                self.label7_3 = QtWidgets.QLabel()
                self.label7_3.setTextFormat(QtCore.Qt.AutoText)
                self.label7_3.setPixmap(QPixmap('panel.png'))
                self.label7_3.setStyleSheet('''color:white;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#FF9900;
                                                font-family:等线;''')
                self.label7_3.setAlignment(Qt.AlignCenter)

                self.label7_4 = QtWidgets.QLabel()
                self.label7_4.setTextFormat(QtCore.Qt.AutoText)
                self.label7_4.setText("结构组成")
                self.label7_4.setStyleSheet('''color:white;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#FF9900;
                                                font-family:等线;''')
                self.label7_4.setAlignment(Qt.AlignCenter)


                self.label7_5 = QtWidgets.QLabel()
                self.label7_5.setTextFormat(QtCore.Qt.AutoText)
                self.label7_5.setText("开关面板")
                self.label7_5.setStyleSheet('''color:white;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#FF9900;
                                                font-family:等线;''')
                self.label7_5.setAlignment(Qt.AlignCenter)                

                self.layout7.addWidget(self.label7_1,0,0,1,4)
                self.layout7.addWidget(self.label7_2,1,0,1,2)
                self.layout7.addWidget(self.label7_3,1,2,1,2)
                self.layout7.addWidget(self.label7_4,2,0,1,2)
                self.layout7.addWidget(self.label7_5,2,2,1,2)

                self.right_widget.addWidget(self.centralWidget7)
            elif i == 9:
                self.centralWidget9 = QtWidgets.QWidget()
                self.centralWidget9.setStyleSheet('''background:black;border-width:0;''');

                self.layout9 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                self.centralWidget9.setLayout(self.layout9)
                

                self.label9_1 = QtWidgets.QLabel()
                self.label9_1.setTextFormat(QtCore.Qt.AutoText)
                self.label9_1.setText("遇到问题")
                self.label9_1.setStyleSheet('''color:white;font-size:23px;background:#FF9900;
                                                font-family:Times new Romans;''');
                self.label9_1.setAlignment(Qt.AlignCenter)
                

                self.label9_2 = QtWidgets.QLabel()
                self.label9_2.setTextFormat(QtCore.Qt.AutoText)
                self.label9_2.setText("机器人不能运动：\n检查是否有充足电量(23%+)及急停按钮是否被释放")
                self.label9_2.setStyleSheet('''color:white;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#FF9900;
                                                font-family:等线;''')
                self.label9_2.setAlignment(Qt.AlignCenter)
                

                self.label9_3 = QtWidgets.QLabel()
                self.label9_3.setTextFormat(QtCore.Qt.AutoText)
                self.label9_3.setText("机器人部件损坏:\n联系我们、厂家进行维修")
                self.label9_3.setStyleSheet('''color:white;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#FF9900;
                                                font-family:等线;''')
                self.label9_3.setAlignment(Qt.AlignCenter)


                self.label9_4 = QtWidgets.QLabel()
                self.label9_4.setTextFormat(QtCore.Qt.AutoText)
                self.label9_4.setText("机器人撞击障碍物：\n立即使用急停按钮紧急停止并联系我们")
                self.label9_4.setStyleSheet('''color:white;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#FF9900;
                                                font-family:等线;''')
                self.label9_4.setAlignment(Qt.AlignCenter)


                self.label9_5 = QtWidgets.QLabel()
                self.label9_5.setTextFormat(QtCore.Qt.AutoText)
                self.label9_5.setText("其他未知错误信息：\n联系我们并报告相关信息（如发生错误前后的操作）")
                self.label9_5.setStyleSheet('''color:white;font-size:23px;background:rgb(0,0,00,00);
                                                border-width:5;border-style:ridge;border-color:#FF9900;
                                                font-family:等线;''')
                self.label9_5.setAlignment(Qt.AlignCenter)

                self.layout9.addWidget(self.label9_1,0,0,1,4)
                self.layout9.addWidget(self.label9_2,1,0,1,2)
                self.layout9.addWidget(self.label9_3,1,2,1,2)
                self.layout9.addWidget(self.label9_4,2,0,1,2)
                self.layout9.addWidget(self.label9_5,2,2,1,2)

                self.right_widget.addWidget(self.centralWidget9)
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
		if i!= 0 and i != 4 and i != 8:
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
        print("roslaunch wpb_home_tutorials gmapping.launch")
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpb_home_tutorials gmapping.launch\"'")
	
    def button2_2click(self):
        print("rosrun map_server map_saver -f map")
        os.system("gnome-terminal -e 'bash -c \"rosrun map_server map_saver -f map&&cp map.yaml /home/robot/catkin_ws/src/wpb_home/wpb_home_tutorials/maps/map.yaml&&cp map.pgm /home/robot/catkin_ws/src/wpb_home/wpb_home_tutorials/maps/map.pgm\"'")
	
    def button2_3click(self):
        print("roslaunch waterplus_map_tools add_waypoint.launch")
        os.system("gnome-terminal -e 'bash -c \"roslaunch waterplus_map_tools add_waypoint.launch\"'")
        
    def button2_4click(self):
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
        
    def button2_5click(self):
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpb_home_apps 6_path_plan.launch; exec bash\"'")
	
    def button2_6click(self):
        print(self.comboBox2.currentIndex()+1)
	#get to the chosed point
        pointoutput = open('/home/robot/point.txt', 'w')
        pointoutput.write(str(self.comboBox2.currentIndex()+1))
        pointoutput.close()

def main():
    ''' '''
    app = QApplication(sys.argv)

    main_wnd = LeftTabWidget()
    main_wnd.show()

    app.exec()

if __name__ == '__main__':
    main()
