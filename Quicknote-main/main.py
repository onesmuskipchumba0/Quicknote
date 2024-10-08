from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QMessageBox,QMainWindow,QDialog, QWidget,QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QFont
import sys

class Main(QMainWindow):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling,True)
    def __init__(self):
        super(Main,self).__init__()
        loadUi('main_ui.ui',self)
        self.current_path = None
        #Buttons
        self.open_btn.clicked.connect(self.open)
        self.new_btn.clicked.connect(self.new)
        self.save_btn.clicked.connect(self.save)
        self.cut_btn.clicked.connect(self.cut)
        self.undo_btn.clicked.connect(self.undo)
        self.redo_btn.clicked.connect(self.redo)
        self.copy_btn.clicked.connect(self.copy)
        self.paste_btn.clicked.connect(self.paste)
        #menu actions
        self.actionSave_as.triggered.connect(self.save_as)
        self.actionSave.triggered.connect(self.save)
        self.actionNew.triggered.connect(self.new)
        self.actionCut.triggered.connect(self.cut)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionCopy.triggered.connect(self.copy)
        self.actionPaste.triggered.connect(self.paste)
        #themes
        self.actionDark_Theme.triggered.connect(self.dark)
        self.actionMonokai_Theme.triggered.connect(self.monokai)
        self.actionLight_Theme.triggered.connect(self.light)
        self.actionDracula.triggered.connect(self.dracula)
        self.actionIncrease_Font.triggered.connect(self.increase_font)
        self.actionDecrease_Font.triggered.connect(self.decrease_font)
        #about
        self.actionWebsite.triggered.connect(self.about)
        self.actionDocumentation.triggered.connect(self.documentation)
        self.actionOther_Projects.triggered.connect(self.github)
        self.point_size = 8
    def about(self):
        import webbrowser
        webbrowser.open('https://onesmusbett.wordpress.com')
    def github(self):
        import webbrowser
        webbrowser.open("https://github.com/ONESMUSBETT")
    def documentation(selfl):
        import webbrowser
        webbrowser.open("https://github.com/ONESMUSBETT/Quicknote")
    def light(self):
        self.setStyleSheet('')
    def dark(self):
        self.setStyleSheet("""
            QMenuBar {
                background-color: #121212;  /* Background color */
                color: #e0e0e0;  /* Text color */
            }
            QMainWindow {
                background-color: #121212;  /* Background color */
                color: #e0e0e0;  /* Text color */
            }
            QTextEdit {
                background-color: #121212;  /* Background color */
                color: #e0e0e0;  /* Text color */
            }
            QMenuBar::item {
                background-color: #121212;  /* Background color */
                color: #e0e0e0;  /* Text color */
            }
            QMenuBar::item:selected { /* When mouse hover */
                background-color: #333333;
            }
            QMenuBar::item:pressed { /* When item is pressed */
                background-color: #bb86fc;
            }
            QMenu {
                background-color: #121212;  /* Background color */
                color: #e0e0e0;  /* Text color */
            }
            QMenu::item:selected { /* When mouse hover */
                background-color: #333333;
            }
            QMenu::item:pressed { /* When item is pressed */
                background-color: #bb86fc;
            }
        """)
    def monokai(self):
        self.setStyleSheet("""
            QMenuBar {
                background-color: #272822;  /* Background color */
                color: #f8f8f2;  /* Text color */
            }
            QTextEdit {
                background-color: #272822;  /* Background color */
                color: #f8f8f2;  /* Text color */
            }
            QMainWindow {
                background-color: #272822;  /* Background color */
                color: #f8f8f2;  /* Text color */
            }
            QMenuBar::item {
                background-color: #272822;  /* Background color */
                color: #f8f8f2;  /* Text color */
            }
            QMenuBar::item:selected { /* When mouse hover */
                background-color: #75715e;
            }
            QMenuBar::item:pressed { /* When item is pressed */
                background-color: #a6e22e;
            }
            QMenu {
                background-color: #272822;  /* Background color */
                color: #f8f8f2;  /* Text color */
            }
            QMenu::item:selected { /* When mouse hover */
                background-color: #75715e;
            }
            QMenu::item:pressed { /* When item is pressed */
                background-color: #a6e22e;
            }
        """)

    def dracula(self):
        self.setStyleSheet("""
            QMenuBar {
                background-color: #282a36;  /* Background color */
                color: #f8f8f2;  /* Text color */
            }
            QTextEdit {
                background-color: #282a36;  /* Background color */
                color: #f8f8f2;  /* Text color */
            }
            QMainWindow {
                background-color: #282a36;  /* Background color */
                color: #f8f8f2;  /* Text color */
            }                          
            QMenuBar::item {
                background-color: #282a36;  /* Background color */
                color: #f8f8f2;  /* Text color */
            }
            QMenuBar::item:selected { /* When mouse hover */
                background-color: #6272a4;
            }
            QMenuBar::item:pressed { /* When item is pressed */
                background-color: #bd93f9;
            }
            QMenu {
                background-color: #282a36;  /* Background color */
                color: #f8f8f2;  /* Text color */
            }
            QMenu::item:selected { /* When mouse hover */
                background-color: #6272a4;
            }
            QMenu::item:pressed { /* When item is pressed */
                background-color: #bd93f9;
            }
        """)
    def increase_font(self):
        self.point_size += 1
        self.textEdit.setFontPointSize(self.point_size)
    def decrease_font(self):
        self.point_size -= 1
        self.textEdit.setFontPointSize(self.point_size)
    def open(self):
        filename = QFileDialog.getOpenFileName(self,"Open file","","File name(*.txt)")
        if filename[0]:
            with open(filename[0],'r') as file:
                self.textEdit.setPlainText(file.read())
                self.setWindowTitle(filename[0])
                self.current_path = filename[0]
        
    def new(self):
        self.textEdit.clear()
        self.setWindowTitle("untitled")
        self.current_path = None

    def save(self):
        if self.current_path is not None:
            #filename = QFileDialog.getSaveFileName(self,"Open file","","File name(*.txt)")
            with open(self.current_path,'w') as file:
                file.write(self.textEdit.toPlainText())
                self.current_path = None
        else:
            self.save_as()
    def save_as(self):
            filename = QFileDialog.getSaveFileName(self,"Open file","","File name(*.txt)")
            self.current_path = filename[0]
            with open(filename[0],'w') as file:
                file.write(self.textEdit.toPlainText())
            
    def cut(self):
        self.textEdit.cut()
    def undo(self):
        self.textEdit.undo()
    def redo(self):
        self.textEdit.redo()
    def copy(self):
        self.textEdit.copy()
    def paste(self):
        self.textEdit.paste()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    app.exec_()
        