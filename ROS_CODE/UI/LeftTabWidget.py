import sys
import os
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore,QtGui,QtWidgets
import qtawesome


class LeftTabWidget(QWidget):
    '''左侧选项栏'''

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
                

            else:
                self.centralWidget0=QtWidgets.QWidget()
                self.centralWidget0.setStyleSheet('''background:white;border-width:0;''');
                self.right_widget.addWidget(self.centralWidget0)
            


def main():
    ''' '''
    app = QApplication(sys.argv)

    main_wnd = LeftTabWidget()
    main_wnd.show()

    app.exec()

if __name__ == '__main__':
    main()
