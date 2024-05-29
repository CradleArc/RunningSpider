import requests
from PyQt5.QtCore import Qt
from bs4 import BeautifulSoup
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5 import QtWidgets

# 要抓取的URL
url = 'https://www.baidu.com'

# 创建一个Session对象
session = requests.Session()

# 发送HTTP请求
response = session.get(url)

# 获取HTTP请求的响应
html_doc = response.text

# 创建一个BeautifulSoup对象
soup = BeautifulSoup(html_doc, 'html.parser')

# 获取所有链接
links = soup.find_all('a')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle("爬虫")

        # 创建一个按钮
        self.button = QPushButton("开始爬虫")

        # 创建一个标签
        self.label = QLabel("爬虫结果")

        # 设置按钮的槽函数
        self.button.clicked.connect(self.on_button_clicked)

        # 在主窗口对象中添加控件
        self.setCentralWidget(self.button)

        # 设置控件的属性
        self.label.setAlignment(Qt.AlignCenter)

        # 显示窗口
        self.show()

    def on_button_clicked(self):
        # 爬虫逻辑

        # 更新标签的内容
        self.label.setText("爬虫完成")

# 创建一个QApplication对象
app = QApplication(sys.argv)

# 创建一个主窗口对象
window = MainWindow()

# 进入主循环
sys.exit(app.exec_())