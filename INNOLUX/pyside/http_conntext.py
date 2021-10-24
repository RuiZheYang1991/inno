from PySide2.QtWidgets import QApplication, QTextBrowser
from PySide2.QtUiTools import QUiLoader
from threading import Thread

from PySide2.QtCore import Signal, QObject


# 自定义信号源对象类型，一定要继承自 QObject
class MySignals(QObject):
    # 定义一种信号，两个参数 类型分别是： QTextBrowser 和 字符串
    # 调用 emit方法 发信号时，传入参数 必须是这里指定的 参数类型
    text_print = Signal(QTextBrowser, str)

    # 还可以定义其他种类的信号
    update_table = Signal(str)


# 实例化
global_ms = MySignals()


class Stats:

    def __init__(self):
        self.ui = QUiLoader().load('main.ui')

        # 自定义信号的处理函数
        global_ms.text_print.connect(self.printToGui)

    def printToGui(self, fb, text):
        fb.append(str(text))
        fb.ensureCursorVisible()

    def task1(self):
        def threadFunc():
            # 通过Signal 的 emit 触发执行 主线程里面的处理函数
            # emit参数和定义Signal的数量、类型必须一致
            global_ms.text_print.emit(self.ui.infoBox1, '输出内容')

        thread = Thread(target=threadFunc)
        thread.start()

    def task2(self):
        def threadFunc():
            global_ms.text_print.emit(self.ui.infoBox2, '输出内容')

        thread = Thread(target=threadFunc)
        thread.start()