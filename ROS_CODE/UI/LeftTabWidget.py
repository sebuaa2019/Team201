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
                elif i == 4:
                    self.item.setIcon(qtawesome.icon('fa.tags',color ='white'))
                elif i == 8:
                    self.item.setIcon(qtawesome.icon('fa.envelope',color ='white'))

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

                self.centralWidget2.setStyleSheet('''background:black;border-width:0;''');
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
		
	    elif i == 7:
                self.centralWidget7=QtWidgets.QWidget()
                self.centralWidget7.setStyleSheet('''background:black;border-width:0;''');

                self.layout7 = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
                self.centralWidget7.setLayout(self.layout7)

                ##start coding
                self.label7_1 = QtWidgets.QLabel()
                self.label7_1.setTextFormat(QtCore.Qt.AutoText)
                self.label7_1.setText("硬件设置")
                self.label7_1.setStyleSheet('''color:white;font-size:23px;background:#FF9900;
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
		
            else:
                self.centralWidget0=QtWidgets.QWidget()
                self.centralWidget0.setStyleSheet('''background:white;border-width:0;''');
                self.right_widget.addWidget(self.centralWidget0)
            
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
