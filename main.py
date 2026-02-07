import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QPalette, QImage, QBrush
from PyQt5.QtWidgets import QDialog, QApplication
from script2 import encrypt_file, decrypt_file
import os
import sqlite3
import smtplib
import hashlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


class Window1(QDialog):
    def __init__(self):
        super(Window1, self).__init__()
        self.initUI()

    def initUI(self):

        self.title = QtWidgets.QLabel(self)
        self.title.setText("User Login")
        self.title.move(950, 200)
        self.title.setFont(QFont('arial', 30))
        self.title.setStyleSheet("color : yellow ")

        font = QFont()
        font.setFamily("franklin gothic demi")
        font.setPointSize(14)
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Username")
        self.label1.move(947, 305)
        self.label1.setStyleSheet("color : white ")
        self.label1.setFont(font)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Password")
        self.label2.move(947, 405)
        self.label2.setStyleSheet("color : white ")
        self.label2.setFont(font)

        font = QFont()
        font.setFamily("arail")
        font.setPointSize(14)
        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText("Create Account")
        self.label3.move(947, 643)
        self.label3.setStyleSheet("color : white ")
        self.label3.setFont(font)

        font = QFont()
        font.setFamily("arial")
        font.setPointSize(12)
        self.lineedit1 = QtWidgets.QLineEdit(self)
        self.lineedit1.move(947, 350)
        self.lineedit1.resize(300, 45)
        self.lineedit1.setFont(font)
        self.lineedit1.setStyleSheet("border: 2px solid blue")

        self.lineedit2 = QtWidgets.QLineEdit(self)
        self.lineedit2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineedit2.move(947, 450)
        self.lineedit2.resize(300, 45)
        self.lineedit2.setFont(font)
        self.lineedit2.setStyleSheet("border: 2px solid blue")

        self.label3 = QtWidgets.QLabel(self)
        self.label3.move(220, 30)

        font = QFont()
        font.setFamily("arail")
        font.setPointSize(10)
        self.login_btn = QtWidgets.QPushButton(self)
        self.login_btn.setText("LOGIN")
        self.login_btn.move(947, 550)
        self.login_btn.setFont(font)
        self.login_btn.setStyleSheet('QPushButton { background-color : #0492C2; }')
        self.login_btn.resize(300, 40)
        self.login_btn.clicked.connect(self.loggedin)

        self.register_btn = QtWidgets.QPushButton(self)
        self.register_btn.setText("SIGN UP")
        self.register_btn.move(1140, 640)
        self.register_btn.setFont(font)
        self.register_btn.setStyleSheet('QPushButton { background-color : red; color : white; }')
        self.register_btn.clicked.connect(self.register)
        self.register_btn.resize(100, 35)

    def loggedin(self):
        user = self.lineedit1.text()
        pwd = self.lineedit2.text()

        font = QFont()
        font.setFamily("arial")
        font.setPointSize(12)

        if not user or not pwd:
            self.label3.setText("Please input all fields.")
            self.label3.setFont(font)
            self.label3.adjustSize()
            self.label3.move(1110, 200)
            return

        conn = sqlite3.connect("network.db")
        cur = conn.cursor()

        cur.execute("SELECT password FROM logins WHERE name = ?", (user,))
        result = cur.fetchone()

        conn.close()

        if result is None:
            self.label3.setText("User not found")
            self.label3.setFont(font)
            self.label3.adjustSize()
            self.label3.move(1110, 200)
            return

        stored_hash = result[0]
        entered_hash = hashlib.sha256(pwd.encode()).hexdigest()

        if stored_hash == entered_hash:
            print("Successfully logged in.")
            self.label3.setText("")
            loggedin = Page()
            widget.addWidget(loggedin)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            widget.setWindowTitle("IMAGE ENCRYPTION")
        else:
            self.label3.setText("Invalid username or password")
            self.label3.setFont(font)
            self.label3.adjustSize()
            self.label3.move(1110, 200)

    def register(self):
        register = Register()
        widget.addWidget(register)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("REGISTER")

class Register(QDialog):
    def __init__(self):
        super(Register, self).__init__()
        self.initUI()

    def initUI(self):

        font = QFont()
        font.setFamily("franklin gothic demi")
        font.setPointSize(17)
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("UserName :")
        self.label1.move(800, 305)
        self.label1.setStyleSheet("color : white ")
        self.label1.setFont(font)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Password :")
        self.label2.move(800, 445)
        self.label2.setStyleSheet("color : white ")
        self.label2.setFont(font)

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText("Confirm Password :")
        self.label3.move(1310, 445)
        self.label3.setStyleSheet("color : white ")
        self.label3.setFont(font)

        self.label4 = QtWidgets.QLabel(self)
        self.label4.setText("First Name :")
        self.label4.move(800, 165)
        self.label4.setStyleSheet("color : white ")
        self.label4.setFont(font)

        self.label5 = QtWidgets.QLabel(self)
        self.label5.setText("Last Name :")
        self.label5.move(1310, 165)
        self.label5.setStyleSheet("color : white ")
        self.label5.setFont(font)

        self.label6 = QtWidgets.QLabel(self)
        self.label6.setText("Email :")
        self.label6.move(1310, 305)
        self.label6.setStyleSheet("color : white ")
        self.label6.setFont(font)

        self.label7 = QtWidgets.QLabel(self)
        self.label7.setText("Address :")
        self.label7.move(800, 585)
        self.label7.setStyleSheet("color : white ")
        self.label7.setFont(font)

        self.label8 = QtWidgets.QLabel(self)
        self.label8.setText("Phone Number :")
        self.label8.move(1310, 585)
        self.label8.setStyleSheet("color : white ")
        self.label8.setFont(font)

        font = QFont()
        font.setFamily("arial")
        font.setPointSize(12)
        self.lineedit1 = QtWidgets.QLineEdit(self)
        self.lineedit1.move(800, 350)
        self.lineedit1.resize(450, 50)
        self.lineedit1.setFont(font)
        self.lineedit1.setStyleSheet("border: 2px solid blue")

        self.lineedit2 = QtWidgets.QLineEdit(self)
        self.lineedit2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineedit2.move(800, 490)
        self.lineedit2.resize(450, 50)
        self.lineedit2.setFont(font)
        self.lineedit2.setStyleSheet("border: 2px solid blue")

        self.lineedit3 = QtWidgets.QLineEdit(self)
        self.lineedit3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineedit3.move(1310, 490)
        self.lineedit3.resize(450, 50)
        self.lineedit3.setFont(font)
        self.lineedit3.setStyleSheet("border: 2px solid blue")

        self.lineedit4 = QtWidgets.QLineEdit(self)
        self.lineedit4.move(800, 210)
        self.lineedit4.resize(450, 50)
        self.lineedit4.setFont(font)
        self.lineedit4.setStyleSheet("border: 2px solid blue")

        self.lineedit5 = QtWidgets.QLineEdit(self)
        self.lineedit5.move(1310, 210)
        self.lineedit5.resize(450, 50)
        self.lineedit5.setFont(font)
        self.lineedit5.setStyleSheet("border: 2px solid blue")

        self.lineedit6 = QtWidgets.QLineEdit(self)
        self.lineedit6.move(1310, 350)
        self.lineedit6.resize(450, 50)
        self.lineedit6.setFont(font)
        self.lineedit6.setStyleSheet("border: 2px solid blue")

        self.lineedit7 = QtWidgets.QLineEdit(self)
        self.lineedit7.move(800, 630)
        self.lineedit7.resize(450, 50)
        self.lineedit7.setFont(font)
        self.lineedit7.setStyleSheet("border: 2px solid blue")

        self.lineedit8 = QtWidgets.QLineEdit(self)
        self.lineedit8.move(1310, 630)
        self.lineedit8.resize(450, 50)
        self.lineedit8.setFont(font)
        self.lineedit8.setStyleSheet("border: 2px solid blue")

        self.label9 = QtWidgets.QLabel(self)
        self.label9.move(220, 30)

        self.back_btn = QtWidgets.QPushButton(self)
        self.back_btn.setText("BACK")
        self.back_btn.move(1610, 750)
        self.back_btn.resize(100, 40)
        self.back_btn.setStyleSheet('QPushButton { background-color : #52B2BF; }')
        self.back_btn.clicked.connect(self.back)

        self.r_btn = QtWidgets.QPushButton(self)
        self.r_btn.setText("REGISTER")
        self.r_btn.move(1410, 750)
        self.r_btn.resize(100, 40)
        self.r_btn.setStyleSheet('QPushButton { background-color : #0492C2; }')
        self.r_btn.clicked.connect(self.register)

    def back(self):
        back = Window1()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("IMAGE ENCRYPTION")

    def register(self):
        user = self.lineedit1.text()
        pwd = self.lineedit2.text()
        cpwd = self.lineedit3.text()
        fn = self.lineedit4.text()
        ln = self.lineedit5.text()
        el = self.lineedit6.text()
        ad = self.lineedit7.text()
        ph = self.lineedit8.text()
        font = QFont()
        font.setFamily("arail")
        font.setPointSize(12)
        if len(user) == 0 or len(pwd) == 0 or len(cpwd) == 0 or len(fn) == 0 or len(ln) == 0 or len(el) == 0 or len(
                ad) == 0 or len(ph) == 0:
            self.label9.setText("Please fill in all inputs.")
            self.label9.setFont(font)
            self.label9.adjustSize()
            self.label9.move(1000, 750)

        elif pwd != cpwd:
            self.label9.setText("Passwords do not match.")
            self.label9.setFont(font)
            self.label9.adjustSize()
            self.label9.move(1000, 750)
        else:
            conn = sqlite3.connect("network.db")
            cur = conn.cursor()

            hashed_pwd = hashlib.sha256(pwd.encode()).hexdigest()
            user_info = [user, hashed_pwd]
            cur.execute('INSERT INTO logins (name, password) VALUES (?,?)', user_info)

            conn.commit()
            conn.close()
            self.label9.setText("Created user please login to continue")
            self.label9.setStyleSheet("color : red ")
            self.label9.setFont(font)
            self.label9.adjustSize()
            self.label9.move(1000, 750)


class Page(QDialog):
    def __init__(self):
        super(Page, self).__init__()
        self.initUI()

    def initUI(self):
        self.title = QtWidgets.QLabel(self)
        self.title.setText("IMAGE ENCRYPTION")
        self.title.move(750, 200)
        self.title.setFont(QFont('Bodoni MT', 50))
        self.title.setStyleSheet("color : #EC9706 ")

        self.label9 = QtWidgets.QLabel(self)
        self.label9.move(220, 30)

        self.encrypt_btn = QtWidgets.QPushButton(self)
        self.encrypt_btn.setText("ENCRYPTION")
        self.encrypt_btn.move(900, 500)
        self.encrypt_btn.resize(300, 100)
        self.encrypt_btn.setStyleSheet('QPushButton { background-color : #fc9834; }')
        self.encrypt_btn.clicked.connect(self.encrypt)

        self.decrypt_btn = QtWidgets.QPushButton(self)
        self.decrypt_btn.setText("DECRYPTION")
        self.decrypt_btn.move(1210, 500)
        self.decrypt_btn.resize(300, 100)
        self.decrypt_btn.setStyleSheet('QPushButton { background-color : #0492C2; }')
        self.decrypt_btn.clicked.connect(self.decrypt)

    def encrypt(self):
        encrypt = Encrypt()
        widget.addWidget(encrypt)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("ENCRYPTION")

    def decrypt(self):
        decrypt = Decrypt()
        widget.addWidget(decrypt)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("DECRYPTION")


class Encrypt(QDialog):
    def __init__(self):
        super(Encrypt, self).__init__()
        self.initUI()

    def initUI(self):
        font = QFont()
        font.setFamily("mongolian baiti")
        font.setPointSize(20)
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Select Image Location/ \nName")
        self.label1.move(780, 500)
        self.label1.setStyleSheet("color : white ")
        self.label1.setFont(font)

        self.lineedit1 = QtWidgets.QLineEdit(self)
        self.lineedit1.move(1100, 500)
        self.lineedit1.resize(500, 40)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Enter Key")
        self.label2.move(780, 610)
        self.label2.setStyleSheet("color : white ")
        self.label2.setFont(font)

        self.lineedit2 = QtWidgets.QLineEdit(self)
        self.lineedit2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineedit2.move(1100, 600)
        self.lineedit2.resize(500, 40)

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText("Set Location For \nEncrypted Image")
        self.label3.move(780, 700)
        self.label3.setStyleSheet("color : white ")
        self.label3.setFont(font)

        self.lineedit3 = QtWidgets.QLineEdit(self)
        self.lineedit3.move(1100, 700)
        self.lineedit3.resize(500, 40)

        self.label5 = QtWidgets.QLabel(self)
        self.label5.move(900, 150)
        self.label5.resize(700, 300)
        self.label5.setStyleSheet("border: 3px solid #ADD8E6")

        self.label4 = QtWidgets.QLabel(self)
        self.label4.move(250, 110)

        self.encrypt_btn = QtWidgets.QPushButton(self)
        self.encrypt_btn.setText("ENCRYPT")
        self.encrypt_btn.move(1340, 800)
        self.encrypt_btn.setStyleSheet('QPushButton { background-color : #0492C2; }')
        self.encrypt_btn.clicked.connect(self.encrypt)
        self.encrypt_btn.resize(100, 50)

        self.send_btn = QtWidgets.QPushButton(self)
        self.send_btn.setText("SEND")
        self.send_btn.move(1500, 800)
        self.send_btn.setStyleSheet('QPushButton { background-color : #0492C2; }')
        self.send_btn.clicked.connect(self.sumbit)
        self.send_btn.resize(100, 50)

        self.back_btn = QtWidgets.QPushButton(self)
        self.back_btn.setText("BACK")
        self.back_btn.move(200, 100)
        self.back_btn.resize(100, 30)
        self.back_btn.clicked.connect(self.back)

    def back(self):
        back = Page()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("IMAGE ENCRYPTION")

    def sumbit(self):
        sender_email = os.getenv("SENDER_EMAIL")
        sender_password = os.getenv("SENDER_PASSWORD")
        receiver_email = os.getenv("RECEIVER_EMAIL")
        sname = self.lineedit3.text()
        # Set up the message and add the file attachment
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = "send a file"

        # Add a text message to the email
        text = """\
        Hi there,

        Please find attached file.

        Best regards,
        Sender-name"""
        body = MIMEText(text)
        message.attach(body)

        # Add the file as an attachment to the message
        with open(sname, 'rb') as f:
            file_data = f.read()
        file = MIMEApplication(file_data, name=sname)
        message.attach(file)

        # Connect to the SMTP server and send the email
        with smtplib.SMTP_SSL('smtp.yandex.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(message)

    def encrypt(self):
        key = self.lineedit2.text().encode()
        fname = self.lineedit1.text()
        sname = self.lineedit3.text()
        encrypt_file(key, fname, sname)
        self.label4.setText("IMAGE SUCCESSFULLY \nENCRYPTED")
        self.label4.setStyleSheet("color : red ")
        font = QFont()
        font.setFamily("bell mt")
        font.setPointSize(30)
        self.label4.setFont(font)
        self.label4.adjustSize()
        self.label4.move(1020, 250)


class Decrypt(QDialog):
    def __init__(self):
        super(Decrypt, self).__init__()
        self.initUI()

    def initUI(self):
        font = QFont()
        font.setFamily("mongolian baiti")
        font.setPointSize(20)
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Select Image Location/ \n")
        self.label1.move(780, 500)
        self.label1.setStyleSheet("color : white ")
        self.label1.setFont(font)

        self.lineedit1 = QtWidgets.QLineEdit(self)
        self.lineedit1.move(1100, 500)
        self.lineedit1.resize(500, 40)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Enter Key")
        self.label2.move(780, 600)
        self.label2.setStyleSheet("color : white ")
        self.label2.setFont(font)

        self.lineedit2 = QtWidgets.QLineEdit(self)
        self.lineedit2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineedit2.move(1100, 600)
        self.lineedit2.resize(500, 40)

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText("Set Location For \nDecrypted Image")
        self.label3.move(780, 700)
        self.label3.setStyleSheet("color : white ")
        self.label3.setFont(font)

        self.lineedit3 = QtWidgets.QLineEdit(self)
        self.lineedit3.move(1100, 700)
        self.lineedit3.resize(500, 40)

        self.label5 = QtWidgets.QLabel(self)
        self.label5.move(900, 150)
        self.label5.resize(700, 300)
        self.label5.setStyleSheet("border: 3px solid #ADD8E6")

        self.label4 = QtWidgets.QLabel(self)
        self.label4.move(250, 110)

        self.decrypt_btn = QtWidgets.QPushButton(self)
        self.decrypt_btn.setText("DECRYPT")
        self.decrypt_btn.move(1400, 800)
        self.decrypt_btn.setStyleSheet('QPushButton { background-color : #0492C2; }')
        self.decrypt_btn.clicked.connect(self.decrypt)
        self.decrypt_btn.resize(100, 50)

        self.back_btn = QtWidgets.QPushButton(self)
        self.back_btn.setText("BACK")
        self.back_btn.move(200, 100)
        self.back_btn.resize(100, 30)
        self.back_btn.clicked.connect(self.back)

    def back(self):
        back = Page()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("IMAGE ENCRYPTION")

    def decrypt(self):
        key = self.lineedit2.text().encode()
        fname = self.lineedit1.text()
        sname = self.lineedit3.text()
        decrypt_file(key, fname, sname)
        self.label4.setText("IMAGE SUCCESSFULLY \nDECRYPTED")
        self.label4.setStyleSheet("color : red ")
        font = QFont()
        font.setFamily("bell mt")
        font.setPointSize(30)
        self.label4.setFont(font)
        self.label4.adjustSize()
        self.label4.move(1000, 200)


app = QApplication(sys.argv)
welcome = Window1()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(900)
widget.setFixedWidth(1800)
widget.setWindowTitle("IMAGE ENCRYPTION")
pal = QPalette()
background = QImage("image1.jpg")
background2 = background.scaled(QSize(1800, 989))
brush = QBrush(background2)
pal.setBrush(QPalette.Background, brush)
widget.setAutoFillBackground(True)
widget.setPalette(pal)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")