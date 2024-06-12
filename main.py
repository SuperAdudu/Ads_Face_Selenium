import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

from ui_object import Ui_MainWindow  # Thay "your_ui_file" bằng tên của file UI của bạn
#import cái này vì khi để nỏ trong thư mục backend thì nó chả chạy được ra hồn
import facebook_login_test_Full_Multithread_V2

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Event with Clicked
        self.ui.btn_push.clicked.connect(self.runFB)
    def runFB(self):
        # Get content with QComboBox
        print(self.ui.comboBox.currentText())
        #Get content with QLineEdit
        print(self.ui.inputcontent.text())
        #Getpost Content
        postContent = self.ui.inputcontent.text()
        facebook_login_test_Full_Multithread_V2.main(postContent)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())