# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import sys

class Ui_Dialog(object):
    def __init__(self, path ='C:\\Users\\Nidhi\\Real-time-Facial-Recognition-master\\absolute_face_1'):
        self.path = path
        
    def env(self):
        p1 = subprocess.call('activate myenv',shell=True)
        print(p1) 
    
        
    def train(self):
        #p2 = subprocess.call(['python', '{}'.format(self.path)])
        p2 = subprocess.call('python trainer.py',shell=True)
        print(p2)
    
    
    def webcam(self):
        subprocess.call('python data_set.py',shell=True)
        
        
    def runsw(self):
        p4 = subprocess.call('python recog.py',shell=True)
        print(p4)
        
    #def train(self):
        #process = subprocess.call(["python", "trainer.py"],stdout=subprocess.PIPE, universal_newlines = True)
        #while True:
            #output=process.stdout.readline()
            #print(output.strip())
            #return_code=process.poll()
            #if return_code is not None:
                #print('RETUTN CODE', return_code)
                #for output in process.stdout.readlines():
                    #print(output.strip())
                #break 
        
        
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(561, 255)
        self.pushButtonTrain = QtWidgets.QPushButton(Dialog)
        self.pushButtonTrain.setGeometry(QtCore.QRect(320, 130, 81, 23))
        self.pushButtonTrain.setObjectName("pushButtonTrain")
        
        self.pushButtonTrain.clicked.connect(self.train)
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 541, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 311, 20))
        self.label_2.setObjectName("label_2")
        self.pushButtonRun = QtWidgets.QPushButton(Dialog)
        self.pushButtonRun.setGeometry(QtCore.QRect(240, 180, 161, 23))
        self.pushButtonRun.setObjectName("pushButtonRun")
        
        self.pushButtonRun.clicked.connect(self.runsw)
        
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 281, 16))
        self.label_3.setObjectName("label_3")
        self.pushButtonOpenWebcam = QtWidgets.QPushButton(Dialog)
        self.pushButtonOpenWebcam.setGeometry(QtCore.QRect(320, 90, 81, 23))
        self.pushButtonOpenWebcam.setObjectName("pushButtonOpenWebcam")
        
        self.pushButtonOpenWebcam.clicked.connect(self.webcam)
        
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 271, 16))
        self.label_4.setObjectName("label_4")
        self.pushButtonOpenEnv = QtWidgets.QPushButton(Dialog)
        self.pushButtonOpenEnv.setGeometry(QtCore.QRect(320, 50, 81, 23))
        self.pushButtonOpenEnv.setObjectName("pushButtonOpenEnv")
        
        self.pushButtonOpenEnv.clicked.connect(self.env)
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
     

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonTrain.setText(_translate("Dialog", "Train Model"))
        self.label.setText(_translate("Dialog", "To Add Students in Database first  open sqlite and open FaceBase.db then open People table and commit changes."))
        self.label_2.setText(_translate("Dialog", "after adding a students detail  it is necessary to train the model"))
        self.pushButtonRun.setText(_translate("Dialog", "Run  Software Application"))
        self.label_3.setText(_translate("Dialog", "To save photos of the added student click Open Webcam"))
        self.pushButtonOpenWebcam.setText(_translate("Dialog", "Open Webcam"))
        self.label_4.setText(_translate("Dialog", "It is important to open the environment first"))
        self.pushButtonOpenEnv.setText(_translate("Dialog", "Open Env"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
