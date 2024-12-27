import json
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QLineEdit
class HomePage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("home.ui",self) 
        self.ui.btnAddNote.clicked.connect(self.addTask)
        self.ui.btnDelete.clicked.connect(self.deleteTask)  
        self.ui.listNote.itemClicked.connect(self.showDetails)
        self.tasks_file = "tasks.json"
        self.tasks = self.loadTasks() 

        self.displayTasks()
    def addTask(self):
        title = self.ui.ipTitle.text().strip()
        content = self.ui.ipContent.toPlainText().strip()
        if not title:
            QMessageBox.warning(self, "Lỗi", "Tiêu đề công việc không được để trống!")
            return
        #Tạo công việc mới với dict
        task = {"title": title, "content": content}
        self.tasks.append(task)
        self.ui.listNote.addItem(title)
        self.ui.ipTitle.clear()
        self.ui.ipContent.clear()
        self.saveTasks()
    def deleteTask(self):
        selected = self.ui.listNote.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Lỗi", "Hãy chọn công việc bạn muốn xoá!")
            return
        for i in selected:
            title = i.text()
            new_tasks = []
            for task in self.tasks:
                if task["title"] != title:
                    new_tasks.append(task)
            self.task = new_tasks
            #Code gọn: self.tasks = [task for task in self.tasks if task["title"] != title]
            
            self.ui.listNote.takeItem(self.ui.listNote.row(i))
            #self.ui.listNote.row(i) trả về chỉ số dòng của danh sách
            #takeItem dùng để xoá giá trị và trả về chỉ sổ dòng cho list
        self.saveTasks()
    def loadTasks(self):
        try: 
            with open(self.tasks_file, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return[]
    def saveTasks(self):
        with open(self.tasks_file, "w") as f:
            json.dump(self.tasks, f, indent=4)
    def displayTasks(self):
        self.ui.listNote.clear()
        for task in self.tasks:
            self.ui.listNote.addItem(task["title"])
    def showDetails(self,item):
        title = item.text()
        for task in self.tasks:
            if task["title"] == title:
                self.ui.ipTitle.setText(task["title"])
                self.ui.ipContent.setPlainText(task["content"])
                break
class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.users_file = "users.json"

        # Load login UI
        self.login_window = uic.loadUi("login.ui")
        self.login_window.btnLogin.clicked.connect(self.login)
        self.login_window.btnRegister.clicked.connect(self.show_register)

        # Thiết lập trường mật khẩu trong login.ui
        self.login_window.login_ip_pass.setEchoMode(QLineEdit.EchoMode.Password)

        # Load register UI
        self.register_window = uic.loadUi("register.ui")
        self.register_window.btnRegister.clicked.connect(self.register)

        # Thiết lập trường mật khẩu trong register.ui
        self.register_window.register_ip_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.register_window.register_ip_repass.setEchoMode(QLineEdit.EchoMode.Password)

        # Load home UI
        self.home_window = HomePage()

        # Hiển thị giao diện đăng nhập mặc định
        self.show_login()

    def show_login(self):
        """Hiển thị giao diện đăng nhập."""
        self.register_window.hide()
        self.home_window.hide()
        self.login_window.show()

    def show_register(self):
        """Hiển thị giao diện đăng ký."""
        self.login_window.hide()
        self.register_window.show()

    def show_home(self):
        """Hiển thị giao diện chính sau khi đăng nhập thành công."""
        self.login_window.hide()
        self.home_window.show()

    def register(self):
        """Xử lý đăng ký tài khoản."""
        username = self.register_window.register_ip_username.text()
        password = self.register_window.register_ip_pass.text()
        repassword = self.register_window.register_ip_repass.text()

        if not username or not password:
            QMessageBox.warning(self.register_window, "Lỗi", "Tên người dùng và mật khẩu không được để trống.")
            return

        if password != repassword:
            QMessageBox.warning(self.register_window, "Lỗi", "Mật khẩu xác nhận không khớp.")
            return

        users = self.load_users()

        if username in users:
            QMessageBox.warning(self.register_window, "Lỗi", "Người dùng đã tồn tại.")
            return

        users[username] = password
        self.save_users(users)
        QMessageBox.information(self.register_window, "Thành công", "Đăng ký thành công.")
        self.show_login()

    def login(self):
        """Xử lý đăng nhập."""
        username = self.login_window.login_ip_username.text()
        password = self.login_window.login_ip_pass.text()

        users = self.load_users()

        if username in users and users[username] == password:
            QMessageBox.information(self.login_window, "Thành công", "Đăng nhập thành công.")
            self.show_home()
        else:
            QMessageBox.warning(self.login_window, "Lỗi", "Tên người dùng hoặc mật khẩu không đúng.")

    def load_users(self):
        """Tải danh sách người dùng từ tệp JSON."""
        try:
            with open(self.users_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    def save_users(self, users):
        """Lưu danh sách người dùng vào tệp JSON."""
        with open(self.users_file, "w") as f:
            json.dump(users, f, indent=4)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = App()
    sys.exit(app.exec())
