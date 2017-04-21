import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
from keras.preprocessing.image import img_to_array, load_img
from keras.models import load_model
import cv2
import numpy as np
def predict_number(filename):
    img=load_img(filename)
    img=img_to_array(img)
    model = load_model('/home/shafayat/PycharmProjects/ImgClass.model')
    img = img.reshape((1,) + img.shape)
    img = img / 255.0
    pr = model.predict_classes(img, 32, 1)
    label.setText('The predicted number is '+str(pr[0]))

def getfile():
    fname = QFileDialog.getOpenFileName(None, 'Open file', '\home', "Image files (*.jpg *.gif)")
    filename=str(fname)
    le.setPixmap(QPixmap(fname))
    predict_number(filename)

app=QtGui.QApplication(sys.argv)

window=QtGui.QWidget()
window.setGeometry(50,50,500,300)
window.setWindowTitle("Basic GUI")
layout = QVBoxLayout()
le=QLabel("hello")
le.setPixmap(QPixmap(os.getcwd()+"/lo.jpg"))
layout.addWidget(le)
btn=QPushButton("image")
btn.clicked.connect(getfile)
layout.addWidget(btn)
label=QLabel("The Predicted Number is ")

layout.addWidget(label)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())